# Hincal - Handy investment calculation

## Серверная часть решения задачи хакатона "Лидеры цифровой трансформации"
## Связанные репозитории
* [Клиентская часть](https://github.com/Afaneor/hincal-frontend)

## Сборка
Убедитесь, что у вас установлен python версии 3.9 или выше

Установка пакетного менеджера poetry (Linux-based)
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
Установка пакетного менеджера poetry (Windows Powershell)
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Установка зависимостей
```shell
poetry install
```
Запуск проекта (применение миграций, фикстур, и локальный запуск)
```python3
python manage.py migrate
python manage.py loaddata personal_cabinet
python manage.py load_investment_site
python manage.py createsuperuser
python manage.py runserver
```
Сборка docker контейнера (ваш сервер, скорее всего не на ARM, поэтому явно указываем архитектуру)
```shell
docker build -t backend -f docker/django/Dockerfile --target production_build .
```
