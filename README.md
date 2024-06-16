# DOLMA
## Серверная часть решения задачи хакатона "Лидеры цифровой трансформации"

### Связанные репозитории
- [Клиентская часть]()
- [Расширение для браузера]() для добавления чат-бота на investmoscow.ru

### Просмотр аналитики
Для просмотра аналитики перейдите по ссылке: [Аналитика](https://prod.api.invest.yapa.one/admin_tools_stats/analytics/).  
Для читаемости аналитики необходимо включить светлую тему в административной панели Django.

## Запуск проекта

### Запуск через docker-compose
Для запуска потребуется наличие Docker и Docker Compose на вашем устройстве.  
Запуск проекта осуществляется с помощью скрипта:
```shell
./start.sh
```

### Локальный запуск
1. Убедитесь, что у вас установлен Python версии 3.9 или выше.
2. Установите пакетный менеджер Poetry.

#### Установка Poetry (Linux-based)
```shell
curl -sSL https://install.python-poetry.org | python3 -
```

#### Установка Poetry (Windows Powershell)
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

3. Установите зависимости:
```shell
poetry install
```

4. Запустите проект (применение миграций, фикстур, и локальный запуск):
```shell
python manage.py migrate
python manage.py loaddata initial_data
python manage.py load_support
python manage.py load_investment_object
python manage.py runserver
```

5. Сборка Docker контейнера:
```shell
docker build -t backend -f docker/django/Dockerfile --target production_build .
```

## Описание проекта

### Инвестиционные объекты
Приложение содержит информацию по инвестиционным объектам для подбора пользователям:

- **EconomicActivity** - экономическая деятельность, разрешенная на объекте. Поддерживает ОКВЭД.
- **Infrastructure** - информация о наличии инфраструктуры на объекте.
- **Privilege** - льготы.
- **Restriction** - ограничения по видам деятельности.
- **TransactionForm** - форма сделки (аренда, продажа и т.д.).
- **InvestmentObject** - общая информация об инвестиционном объекте, который может быть нескольких типов (ObjectType):
  - **ReadyBusiness** - готовый бизнес, парсится с сайта alterainvest.ru.
  - **RealEstate** - недвижимость, парсится из xlsx файла.
  - **TenderLot** - лот тендера, парсится с сайта torgi.gov.ru.
  - **SpecializedSite** - специализированная площадка (технопарки, технополисы), парсится из xlsx файла.

### Личный кабинет
Предназначен для получения информации о бизнесе пользователя, формирования запросов на подбор объектов и оформлении подписок:

- **Sector**, **SubSector**, **TerritorialLocation** - сопроводительные объекты для создания бизнеса.
- **Business** - информация о бизнесе пользователя.
- **SelectionRequest** - запрос на подбор, содержит информацию о сообщениях, найденных объектах, поддержке и проблемах.
- **Message** - сообщения в чат-боте.
- **Subscription** - подписки на уведомления о новых объектах, мерах поддержки и событиях.

### Сервисы взаимодействия
Позволяют инвесторам общаться на форуме, оставлять отзывы об объектах и участвовать в событиях:

- **Event** - информация о предстоящих событиях (вебинары, встречи и т.д.).
- **Comment** - отзывы инвесторов об объектах.
- **Topic** - темы на форуме для обсуждений.
- **Post** - сообщения в темах.

### Поддержка
Дополнительная информация и меры поддержки для инвесторов:

- [Поддержка инвесторов](https://investmoscow.ru/business/moscow-investor)
- [Поиск мер поддержки](https://investmoscow.ru/catalog/search)

### Дополнительные функции
- Парсинг сайтов (investmoscow.ru, torgi.gov.ru, alterainvest.ru)
- Парсинг xlsx файлов
- Ролевая система
- Система оповещения пользователей о новых инвестиционных объектах
- Система оповещения пользователей о новых мерах поддержки
- Система отзывов
- Аналитика в административной панели Django
- Чат-бот для сайта investmoscow.ru
- Автоматическая актуализация данных и возможность прогружать из excel-файлов
- Оценка подобранных объектов
