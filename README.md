# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
## Цель: выработать навык работы с CRUD запросами.
## Задача "Имитация работы с БД":

Создайте новое приложение **FastAPI** и сделайте *CRUD* запросы.

Создайте словарь **`users = {'1': 'Имя: Example, возраст: 18'}`**

**Реализуйте 4 CRUD запроса:**

>1. **get** запрос по маршруту **`'/users'`**, который возвращает словарь **users**.
>
>2. **post** запрос по маршруту **`'/user/{username}/{age}'`**, который добавляет в словарь по максимальному по значению
>    ключом значение строки **`"Имя: {username}, возраст: {age}"`**. И возвращает строку **`"User <user_id> is registered"`**.
>4.
>5. **put** запрос по маршруту **`'/user/{user_id}/{username}/{age}'`**, который обновляет значение из словаря **users**
>   под ключом **user_id** на строку **`"Имя: {username}, возраст: {age}"`**. И возвращает строку **`"The user <user_id> is updated"`**
>7. **delete** запрос по маршруту **`'/user/{user_id}'`**, который удаляет из словаря **users** по ключу **user_id** **2**.
**Выполните каждый из этих запросов по порядку. Ответы должны совпадать:**
1. ***GET '/users'***
*{
"1": "Имя: Example, возраст: 18"
}*
2. ***POST '/user/{username}/{age}'*** # username - UrbanUser, age - 24
**`"User 2 is registered"`**
3. ***POST '/user/{username}/{age}'*** # username - NewUser, age - 22
"User 3 is registered"
4.***PUT '/user/{user_id}/{username}/{age}'*** # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. ***DELETE '/user/{user_id}'*** # user_id - 2
"User 2 has been deleted"
6. ***GET '/users'***
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}
## Пример результата выполнения программы:
**Как должен выглядеть Swagger:**

![image](https://github.com/user-attachments/assets/3e50591e-7dc2-4266-b75b-33108fcf6ba6)


## Примечания:
Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.

**Файл module_16_3.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.**