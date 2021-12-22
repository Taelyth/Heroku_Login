import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    # variável local para armazenar o caminho do ChromeDriver

    # print(os.getcwd()) C:\Users\jaque\PycharmProjects\Heroku_Login\tests
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        # se existe um chromedriver dentro do projeto, instancie com ele
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        # se não existe, tente usar o chromedriver publico no ambiente
        driver_ = webdriver.Chrome()

    def sair():
        driver_.quit()

    # sinalizando o fim da execução para o ambiente
    request.addfinalizer(sair)
    return driver_


def test_login_valido(driver):
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

    assert driver.find_element(By.CSS_SELECTOR, '.success').is_displayed()
