import os

import pytest
from selenium import webdriver

import credentials
from . import config  # . = mesmo pacote / diretório


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='http://the-internet.herokuapp.com',
        help='URL base do site alvo do teste'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='Onde vamos executar nossos testes: localhost ou saucelabs'
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Navegador utilizado nos testes'
    )
    parser.addoption(
        '--browserversion',
        action='store',
        default='96.0',
        help='Versão do browser'
    )
    parser.addoption(
        '--platform',
        action='store',
        default='Windows 10',
        help='Sistema operacional a ser utilizado durante os testes'
    )


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoptions('--baseurl')
    config.host = request.config.getoptions('--host')
    config.browser = request.config.getoptions('--browser')
    config.browserversion = request.config.getoptions('--browserversion')
    config.platform = request.config.getoptions('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name   # nome do teste
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce:options': {
                'name': test_name
            }
        }
        _credentials = os.environ[credentials.SAUCE_USERNAME] + ':' + os.environ[credentials.SAUCE_ACCESS_KEY]
        _url = 'https://' + _credentials + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)
    else:   # execução local / localhost
        if config.browser == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
            if os.path.isfile(_chromedriver):
                driver_ = webdriver.Chrome(_chromedriver)
            else:
                driver_ = webdriver.Chrome()
        elif config.browser == 'firefox':
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox(_geckodriver)
            else:
                driver_ = webdriver.Firefox()
