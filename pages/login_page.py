# 1 - Bibliotecas
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# 2 - Classe
class LoginPage(BasePage):
    # 2.1 — Mapeamento dos Elementos da Página
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _message = {'by': By.ID, 'value': 'flash'}
    _login_form = {'by': By.ID, 'value': 'login'}

    # 2.2 — Inicializador / Construtor (Java)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._entrar('http://the-internet.herokuapp.com/login')

        # validando se o formulário de ‘login’ está visível
        assert self._aparecer(self._login_form)

    def com_(self, username, password):
        # Programação sem Page Objetct:
        # self.driver.find_element(self._username_input['by'],
        #                          self._username_input['value']).send_keys(username)
        # self.driver.find_element(self._password_input['by'],
        #                          self._password_input['value']).send_keys(password)
        # self.driver.find_element(self._login_button['by'],
        #                          self._login_button['value']).click()

        # Programação com Page Object
        self._escrever(self._username_input, username)
        self._escrever(self._password_input, password)
        self._clicar(self._login_button)

    # 2.3 — Ações Realizaveis
    def vejo_mensagem(self):
        # return self.driver.find_element(self._message['by'], self._message['value']).text
        return self._encontrar(self._message).text
