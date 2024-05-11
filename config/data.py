import os
from dotenv import load_dotenv

""" Класс для хранения данных в скрытом формате, т.е. логин и пароль будут скрыты от глаз.
 Файл .env закину в ignor и опрокину все значения в нём, в secret, в github """

load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")