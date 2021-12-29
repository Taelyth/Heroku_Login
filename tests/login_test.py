import os

import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def login(request):
    # variável local para armazenar o caminho do ChromeDriver

    # print(os.getcwd()) C:\Users\jaque\PycharmProjects\Heroku_Login\tests
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        # se existe um chromedriver no projeto, instancie com
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        # se não existe, tente usar o chromedriver publico no ambiente
        driver_ = webdriver.Chrome()

    loginpage = LoginPage(driver_)

    def sair():
        driver_.quit()

    # sinalizando o fim da execução para o ambiente
    request.addfinalizer(sair)
    return loginpage


# def old_test_login_valido(driver):
#     driver.get('http://the-internet.herokuapp.com/login')
#     driver.find_element(By.ID, 'username').send_keys('tomsmith')
#     driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
#     driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
#
#     #assert 'You logged into a secure area!' in driver.find_element(By.CSS_SELECTOR, '.success').text
#     assert 'You logged into a secure area!' in driver.find_element(By.ID, 'flash').text

parametros = [
    ('tomsmith', 'SuperSecretPassword!', 'You logged into a secure area!'),
    ('tomsmith', 'a', 'Your password is invalid!'),
    ('a', 'a', 'Your username is invalid!')
]


@pytest.mark.parametrize('username, password, resultado_esperado', parametros)
def testar_login(login, username, password, resultado_esperado):
    # Preencher o usuário e senha clicar no botão
    login.com_(username, password)
    # Validar a mensagem
    assert resultado_esperado in login.vejo_mensagem()


def testar_login_simples(login):
    login.com_('tomsmith', 'SuperSecretPassword!')
    assert 'You logged into a secure area!' in login.vejo_mensagem()
