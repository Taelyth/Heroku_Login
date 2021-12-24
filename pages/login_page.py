# 1 - Bibliotecas
from selenium.webdriver.common.by import By

# 2 - Classe
class LoginPage:
    # 2.1 — Mapeamento dos Elementos da Página
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _message = {'by': By.ID, 'value': 'flash'}

    # 2.2 — Inicializador / Construtor (Java)
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://the-internet.herokuapp.com/login')

    def com_(self, username, password):
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()

    # 2.3 — Ações Realizaveis
    def vejo_mensagem(self):
        return self.driver.find_element(self._message['by'], self._message['value']).text
