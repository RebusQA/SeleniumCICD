import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

""" Создаю фикстуру для инициализации драйвера под тесты """
@pytest.fixture(scope="function", autouse=True)
def driver(request):

    # Данные опции позволяют запускаться драйверу, браузеру внутри сред, где нет интерфейса
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Инициализирую драйвер
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()