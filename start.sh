#!/bin/bash

# Функция для вывода цветного текста
function print_color() {
    local color="$1"
    local text="$2"
    case $color in
        "red") echo -e "\033[31m$text\033[0m" ;;
        "green") echo -e "\033[32m$text\033[0m" ;;
        "yellow") echo -e "\033[33m$text\033[0m" ;;
        "blue") echo -e "\033[34m$text\033[0m" ;;
        *) echo "$text" ;;
    esac
}

# Проверка, установлен ли Docker
if ! command -v docker &> /dev/null
then
    print_color "red" "Docker не установлен. Установите Docker и попробуйте снова."
    exit 1
fi

# Проверка, установлен ли Docker Compose
if ! command -v docker-compose &> /dev/null
then
    print_color "red" "Docker Compose не установлен. Установите Docker Compose и попробуйте снова."
    exit 1
fi

print_color "green" "Docker и Docker Compose установлены."
print_color "yellow" "Сейчас будет проходить настройка, пожалуйста, отвечайте на вопросы."

# Создание или перезапись файла .env в папке config
mkdir -p config
env_file="config/.env"
> "$env_file"

# Функция для запроса значения переменной
function ask_env_var() {
    local var_name="$1"
    local default_value="$2"
    local hint="$3"
    local value=""

    if [ -n "$hint" ]; then
        print_color "blue" "$var_name (Если ничего не ввести, то значение по умолчанию: $default_value) [$hint]: "
    else
        print_color "blue" "$var_name (Если ничего не ввести, то значение по умолчанию: $default_value) : "
    fi

    read -r input_value
    if [ -z "$input_value" ]; then
        value="$default_value"
    else
        value="$input_value"
    fi

    echo "$var_name=$value" >> "$env_file"
}

# Запрос значений переменных
ask_env_var "POSTGRES_PASSWORD" "postgres"
ask_env_var "POSTGRES_DB" "postgres"
ask_env_var "POSTGRES_USER" "postgres"
ask_env_var "SENTRY_DSN" "" "можно пропустить, используется для логирования ошибок"
ask_env_var "LLM_PROVIDER" "server.apps.llm.providers.GPTProvider" "server.apps.llm.providers.GPTProvider | server.apps.llm.providers.LocalProvider [выбор через что генерировать ChatGPT или llama3]"
ask_env_var "SENTRY_DEPLOYMENT" "" "можно пропустить, используется для логирования ошибок"
ask_env_var "DJANGO_DATABASE_HOST" "db" "[url базы данных]"
ask_env_var "CELERY_BROKER_URL" "amqp://guest:guest@rabbitmq:5672/"
ask_env_var "OLLAMA_HOST" "http://ollama:11434"
ask_env_var "DJANGO_SECRET_KEY" "3^qygs767umquk1a3w5x_5werlv(2p8t4=m*fw&ogp8zl1@31yex"
ask_env_var "DOMAIN_NAME" "localhost" "[название домена]"

# Обязательный ввод значений для GPTProvider
if grep -q "LLM_PROVIDER=server.apps.llm.providers.GPTProvider" "$env_file"; then
    while true; do
        print_color "blue" "OPENAI_ASSISTANT_ID [Assistant ID чат-гпт, можно запросить у https://t.me/NikolayPavlin]: "
        read -r assistant_id
        if [ -n "$assistant_id" ]; then
            echo "OPENAI_ASSISTANT_ID=$assistant_id" >> "$env_file"
            break
        else
            print_color "red" "Это значение обязательно для ввода."
        fi
    done

    while true; do
        print_color "blue" "OPENAI_API_KEY [API ключ openai, можно запросить у https://t.me/NikolayPavlin]: "
        read -r api_key
        if [ -n "$api_key" ]; then
            echo "OPENAI_API_KEY=$api_key" >> "$env_file"
            break
        else
            print_color "red" "Это значение обязательно для ввода."
        fi
    done
else
    echo "OPENAI_ASSISTANT_ID=" >> "$env_file"
    echo "OPENAI_API_KEY=" >> "$env_file"
fi

ask_env_var "DADATA_API_TOKEN" "" "[API ключ dadata, нужен для автоматической генерации данных по бизнесам, можно запросить у https://t.me/NikolayPavlin]"

# Email settings
ask_env_var "EMAIL_HOST" "fake" "[данные для отправки писем]"
ask_env_var "EMAIL_PORT" "1025" "[данные для отправки писем]"
ask_env_var "EMAIL_HOST_USER" "fake" "[данные для отправки писем]"
ask_env_var "EMAIL_HOST_PASSWORD" "fake" "[данные для отправки писем]"
ask_env_var "EMAIL_USE_TLS" "0" "[данные для отправки писем]"
ask_env_var "DEFAULT_FROM_EMAIL" "fake" "[данные для отправки писем]"

print_color "yellow" "Начинаем загрузку контейнеров..."
docker compose pull

print_color "blue" "Хотите загрузить бэкап данных из ./backup/backup.sql? [y/N]: "
read -r load_backup

if [ "$load_backup" == "y" ] || [ "$load_backup" == "Y" ]; then
    print_color "yellow" "Запускаем контейнеры для загрузки бэкапа..."
    docker compose up -d db
    print_color "yellow" "Ждем 10 секунд для инициализации контейнера базы данных..."
    sleep 10
    print_color "yellow" "Загружаем бэкап данных..."
    docker exec -i $(docker-compose ps -q db) psql -U $POSTGRES_USER -d $POSTGRES_DB < ./backup/backup.sql
    print_color "green" "Бэкап данных успешно загружен."
fi

print_color "yellow" "Выполняем provision..."
docker compose run --rm web provision
print_color "green" "Собраны статические файлы и применены миграции"

print_color "yellow" "Запускаем остальные контейнеры..."
docker compose up -d
# Проверка, если выбран локальный провайдер, запуск модели

if grep -q "LLM_PROVIDER=server.apps.llm.providers.LocalProvider" "$env_file"; then
    print_color "yellow" "Запускаем модель ollama для локального провайдера..."
    docker exec -d $(docker-compose ps -q ollama) ollama run llama3
    print_color "green" "Модель ollama успешно запущена."
fi

print_color "green" "Настройка завершена."
print_color "green" "Frontend доступен на localhost:80, а backend на localhost:8000"
print_color "green" "Для остановки контейнеров используйте docker compose down"
