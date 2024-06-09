# DOLMA

## Серверная часть решения задачи хакатона "Лидеры цифровой трансформации"
## Связанные репозитории

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
python manage.py load_investment_object
python manage.py load_support
python manage.py runserver
```
Сборка docker контейнера (ваш сервер, скорее всего не на ARM, поэтому явно указываем архитектуру)
```shell
docker build -t backend -f docker/django/Dockerfile --target production_build .
```


# Описание проекта.
### Инвестиционные объекты
Приложение содержит всю основную информацию по объектам среди которых 
осуществляется подбор для пользователя.

EconomicActivity - экономическая деятельность. Сфера деятельности которая 
разрешена на площадке, объекте. Сфера деятельности бизнеса. Поддерживает ОКВЭД
Infrastructure - инфраструктура. Информация о наличии инфраструктуры на объекте.
Privilege - льготы.
Restriction - ограничения по видам деятельности.
TransactionForm - форма сделки. Аренда, продажи и тд.
InvestmentObject - инвестиционный объект. Общая информация об инвестиционном 
объекте. Сам по себе инвестиционный объект может быть нескольких типов 
(ObjectType). В зависимости от типа на InvestmentObject ссылаются разные 
сущности:
1) ReadyBusiness - готовый бизнес. Парсится с сайта alterainvest.ru
2) RealEstate - недвижимость. Парсится из xlsx файла. Также написан парсинг для
сайта investmoscow.ru, но не используется.
3) TenderLot - лот тендера. Парсится с сайта torgi.gov.ru
4) SpecializedSite - специализированная площадка (технопарки, технополисы).
Парсится из xlsx файла. Также написан парсинг для сайта investmoscow.ru, 
но не используется.

Выделение общего объекта связано с тем, чтобы разрозненные элементы имели общие 
характеристики по которым был бы осуществлен поиск. Кроме того общий объект
позволяет предоставлять однообразную информацию в одном месте, а также 
сравнивать объекты друг с другом даже если такие объекты по своей сути очень 
отличаются.


### Личный кабинет
Личный кабинет предназначен для получения информации о бизнесе пользователя,
для формирования запросов на подбор объектов и оформлении подписок.

Sector, SubSector, TerritorialLocation - сопроводительные объекты для создания
бизнеса.
Business - бизнес. Информация о бизнесе, которым владеет пользователь. 
Используется в поиске. Также можно указывать информацию о потенциальном 
бизнесе (который планируется создаваться).
SelectionRequest - запрос на подбор. Грубо говоря объект активного сеанса 
чат бота. Содержит в себе информацию о сообщениях которые были отправлены 
и получены пользователем, информацию о том, какие объекты/меры поддержки/проблемы
были найдены в рамках запроса. Также на основе этого объекта формируется отчет 
в формате pdf.
Message - сообщение. Сообщение, которое пользователь отправляет и получает в 
чат боте.
SelectedEntity - подобранные сущности в рамках запроса. Хранение информации об 
объектах, которые были подобраны ИИ.
Subscription - подписка. Объект, который позволяет пользователям получать 
уведомления на email или в telegram о добавлении новых инвестиционных
объектов, мер поддержки, сообщений на форуме и событий.

### Сервисы взаимодействия.
Сервисы взаимодействия позволяет общаться инвесторам на форуме, оставлять
отзывы об объектах, а так жее следить и принимать участие в событиях,
которые могут быть организованы.

Event - событие. Содержит информацию о предстоящем событии, которое может быть 
различных типов: вебинар, встреча и др.
Feedback - отзыв. Информация инвесторов о том или ином объекте инвестирования.
Позволяет другим инвесторам получать оценку объекта от других пользователей 
сервиса.
Topic - тема. В системе организован форум, чтобы инвесторы могли делиться опытом
получать информацию, находить новые знакомства и идеи.
Post - сообщение в теме. Сообщение, которое оставляет пользователь в теме.

### Поддержка.
https://investmoscow.ru/business/moscow-investor
Problem - проблемы, с которыми сталкивается инвестор (FAQ)

https://investmoscow.ru/catalog/search
ServiceSupport - меры поддержки.

В системе дополнительно реализован:
- Парсинг сайта investmoscow, torgi.gov, alterainvest.
- Парсинг предоставленных xlsx файлов.
- Ролевая система.
- Система оповещения пользователей о новых инвестиционных объектах.
