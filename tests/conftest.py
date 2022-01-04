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
def driver(request):  # Inicialização dos testes — similar a um Before / Setup
    if config.baseurl is '':
        config.baseurl = request.config.getoption('--baseurl')
    if config.host is '':
        config.host = request.config.getoption('--host').lower()
    if config.browser is '':
        config.browser = request.config.getoption('--browser').lower()
    config.browserversion = request.config.getoption('--browserversion').lower()
    config.platform = request.config.getoption('--platform').lower()
    if config.host == 'saucelabs':
        test_name = request.node.name  # nome do teste
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce:options': {
                'name': test_name
            }
        }
        # _credentials = os.environ[credentials.SAUCE_USERNAME] + ':' + os.environ[credentials.SAUCE_ACCESS_KEY]
        _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)
    else:  # execução local / localhost
        if config.browser == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
            if os.path.isfile(_chromedriver):
                driver_ = webdriver.Chrome(_chromedriver)
            else:
                driver_ = webdriver.Chrome()
        elif config.browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.binary_location = os.path.expanduser('~\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox(executable_path=_geckodriver, options=options)
            else:
                driver_ = webdriver.Firefox()

    def sair():  # Finalização dos testes — similar ao After ou TearDown
        # sinalização de passou ou falhou conforme o retorno da requisição
        if config.host == 'saucelabs':
            sauce_result = 'failed' if request.node.rep_call.failed else 'passed'

            driver_.execute_script('sauce:job-result={}'.format(sauce_result))

        driver_.quit()

    request.addfinalizer(sair)
    return driver_


@pytest.hookimpl(hookwrapper=True, tryfirst=True)  # Imprementação do gatilho de comunicação com o SauceLabs
def pytest_runtest_makereport(item, call):
    # parâmetros para geração do relatório / informações dos resultados
    outcome = yield
    rep = outcome.get_result()

    # definir atributos para o relatório
    setattr(item, 'rep_' + rep.when, rep)
