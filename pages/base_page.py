class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Este é o selenium

    def _entrar(self, url):
        self.driver.get(url)

    def _encontrar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _clicar(self, locator):
        self._encontrar(locator).click()

    def _escrever(self, locator, texto):
        self._encontrar(locator).send_keys(texto)

    def _aparece(self, locator, timeout=1):
        pass
