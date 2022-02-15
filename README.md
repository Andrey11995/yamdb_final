# Проект YaMDb
![push](https://github.com/Andrey11995/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)
## Описание:

### Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. Произведениям могут быть присвоены жанры и категории из списка предустановленных. Пользователи оставляют к произведениям отзывы и ставят оценку в диапазоне от одного до десяти, из оценок формируется рейтинг произведения. На одно произведение пользователь может оставить только один отзыв.

## Проект доступен на сервере:
### http://yatube.sytes.net/redoc/

## Наполнение env-файла:

- DB_ENGINE=django.db.backends.postgresql - используемая БД
- DB_NAME=postgres - имя БД
- POSTGRES_USER - логин для подключения к БД
- POSTGRES_PASSWORD - пароль для подключения к БД
- DB_HOST - название сервиса (контейнера)
- DB_PORT -  порт для подключения к БД


## Как запустить проект в контейнерах:

Клонировать репозиторий и перейти в директорию с файлом docker-compose.yaml:

```
git clone https://github.com/Andrey11995/yamdb_final
```

```
cd yamdb_final/infra/
```

Собрать проект в контейнеры и запустить:

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Собрать статические файлы:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```
Потребуется ввести почту, имя пользователя и пароль.


## Наполнение базы данных

### Для наполнения базы данных применить следующую команду:

```
docker-compose exec web python manage.py load_data
```


## Алгоритм регистрации пользователей

1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).


## Авторы

### Над проектом работали:

1. Яков Крис — Тимлид
2. Максим Бубневич — Разработчик
3. Андрей Завьялов — Разработчик


## Технологии

#### Python
#### Django REST Framework
#### SQLite
#### Gunicorn, Nginx
#### Docker, Docker-compose
#### CI и CD
