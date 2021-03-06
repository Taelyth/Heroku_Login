from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Este é o selenium

    def _entrar(self, url):
        # self.driver.get(url)
        if url.startswith('http'):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)
            # imagine que o endereço viesse como '/login', ficaria endereço base + /login

    def _encontrar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _clicar(self, locator):
        self._encontrar(locator).click()

    def _escrever(self, locator, texto):
        self._encontrar(locator).send_keys(texto)

    def _aparecer(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._encontrar(locator).is_displayed()
            except NoSuchElementException:
                return False
