## **Описание проекта YaMDb:**


[Yamdb_workflow](https://github.com/MrBrus/yamdb_final/yamdb_workflow.yml)

http://mrbrusyamdbproject.hopto.org


1) Проект YaMDb собирает отзывы (Review)
пользователей на произведения (Titles). 
2) Категории (Category) произведений могут быть следующими: 
«Книги», «Фильмы», «Музыка». 
Список категорий может быть 
расширен администратором.
3) Произведению может быть присвоен жанр (Genre) 
из списка предустановленных. 
Новые жанры может создавать только администратор.
4) Пользователи оставляют к произведениям текстовые отзывы 
(Review) и ставят произведению оценку в диапазоне 
от одного до десяти (целое число); 
из пользовательских оценок формируется 
усреднённая оценка произведения — рейтинг 
(целое число). 
На одно произведение пользователь может 
оставить только один отзыв.


#### 1. Установка docker и docker-compose

Если у вас уже установлены docker и docker-compose, этот шаг можно пропустить, иначе можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### 2. Запуск контейнера
```bash
docker-compose up
```
### 3. Выключение контейнера
```bash
docker-compose down
```


## Использование
#### Создание суперпользователя Django
```bash
docker-compose run web python manage.py createsuperuser
```

#### Пример инициализации стартовых данных:
```bash
docker-compose run web python manage.py loaddata fixtures.json
```

Полный список эндпойнтов, методы и параметры запросов описаны в докуметации, которая будет доступна после установки проекта:
```
127.0.0.1:8000/redoc/ 
```

### Пример использования API

**GET /titles/** - получить список всех произведений  
Ответ (200):  
Ключ|Значение|Описание
----|--------|--------
"id"|number|ID произведения
"name"|"string"|Название
"year"|number|Год выпуска
"rating"|number|Рейтинг на основе отзывов
"description"|"string"|Описание
"genre"|Array of objects|Жанр
||"name"|Название жанра
||"slug"|Поле "slug" 
"category"|objects|Категория
||"name"|Название категории объекта
||"slug"|Поле "slug"

### Список технологий:
* python 3.8
* [django](https://www.djangoproject.com/)
* [drf](https://www.django-rest-framework.org/)
* [posgresql](https://www.postgresql.org/)
* [docker](https://www.docker.com/)