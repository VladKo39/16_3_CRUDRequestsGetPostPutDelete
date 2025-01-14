from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
#app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def main_page() -> dict:
    #Создание маршрута к главной странице - "/".
    # По нему должно выводиться сообщение "Главная страница".
    return {"message": "Главная страница  module_16_3"}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')

async def post_user(
username: Annotated[str, Path(min_length=5, max_length=20,description="Enter Username",
pattern="^[A-Za-z\\s]+$",title='New User',example="UrbanUser")],
age:Annotated[int, Path(ge=18, le=120,description="Enter age",example=24)]
)-> dict:
    #,example="Vladislav"
    #,example=57
    #маршрут к страницам пользователей передавая данные в адресной строке - "/user"
    user_id = str(int(max(users, key=int)) + 1)

    users[user_id] = f'Имя: {username}, возраст: {age}'

    return {'message':
            f'Пользователь зарегистрирован. Имя: {username}, Возраст: {age}'}


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[int, Path(ge=1, le=100,
                                 description='Enter User ID', example='1')],
    username: Annotated[str, Path(min_length=5, max_length=20,
                                  description='Enter username',
                                  example='UrbanProfi')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age',
                             example=28)]
) -> dict:

    if str(user_id) not in users:
        raise HTTPException(status_code=404,
                            detail=f'Пользователь id= {user_id} не найден')
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь Id= {user_id} изменен.'



@app.delete("/users/{user_id}")
async def delete_user(
user_id: Annotated[int, Path(ge=1, le=100,
                             description='Enter User ID', example='1')]
)->str:

    if str(user_id) not in users:
        raise HTTPException(status_code=404,
                            detail=f"Пользователь с id= {user_id} не найден")
    deleted_user = users.pop(str(user_id))
    return f"Пользователь {deleted_user} удалён."
