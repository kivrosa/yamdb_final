https://github.com/kivrosa/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg
# yamdb_final
## Описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.   
Произведения делятся на категории, а также им может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).  
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.
Пользователи могут оставлять комментарии к отзывам.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:kivrosa/infra_sp2.git
```

```
cd infra_sp2
```

Перейдите в директорию ``` infra ``` и создайте файл ```.env``` с переменными окружения

```
cd infra
```

```
touch .env
```

Укажите необходимые переменные окружения (шаблон заполнения приведён ниже)

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Запустите проект. Для этого введите команду

```
docker-compose up -d
```

Создайте и примените миграции

```
docker-compose exec web python manage.py makemigrations
```

```
docker-compose exec web python manage.py migrate
```

Создайте суперпользователя

```
docker-compose exec web python manage.py createsuperuser
```

Реализуйте сбор статики в одной папке

```
docker-compose exec web python manage.py collectstatic --no-input
```

(При необходимости) заполните БД тестовыми данными

```
docker-compose exec web python manage.py loaddata fixtures.json
```

### Примеры запросов к API:
Примеры запросов доступны в формате ReDoc. Для просмотра перейдите по адресу

```
http://127.0.0.1:80/redoc/

```

### Использованные технологии:
1. Python 3.9  
2. Django 3.2  
3. DRF  
4. JWT + Djoser  
5. Docker

### Авторы проекта:
[Яблокова Ирина](https://github.com/YablokovaIrina)  
[Холмаков Захар](https://github.com/kivrosa)  
[Самиляк Александр](https://github.com/aisamilyak)