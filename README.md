# Heroku_Login
Projeto criado para acompanhar as aulas do curso [Formação em Teste de Software][Iterasys] em **Python** utilizando **Selenium**.

Neste projeto é possível rodar **testes web** tanto no [Saucelabs][Saucelabs], que é um site de testes em Cloud, assim como rodar localmente.

Ele foi criado para treinamento em como utilizar a formatação **Page Object**, onde os elementos e testes ficam separados por script/página.

---

### Pré-Requisitos
- As bibliotecas utilizadas estão no arquivo [requirements.txt](requirements.txt), e são:

```
selenium
sauceclient
pytest
pytest-xdist
pytest-randomly
```

- URL utilizada para as aulas: [HerokuApp-Login]
- Para rodar no [Saucelabs][Saucelabs] é necessário criar um arquivo `credentials.py` na raiz do projeto e nele será colocada as credenciais, onde deverá ser preenchido conforme abaixo:

```
SAUCE_USERNAME = 'Preencher com o Username do Saucelabs'
SAUCE_ACCESS_KEY = 'Access Key do Saucelabs que pode ser vista em Account > User settings'
```
- Para configurar se o teste rodará na nuvem ou local, é importante modificar o arquivo [config.py](tests/config.py), da seguinte forma:

```
baseurl = 'O valor default é http://the-internet.herokuapp.com, é possível configurar outros testes nessa url
modificando o final da url conforme feito no login_page.py'

host = 'O valor default é saucelabs, caso coloque local os testes rodarão localmente e não na cloud'

browser = 'O valor default é chrome, caso queira rodar os testes no firefox, configurar para este valor.
Apenas esses dois navegadores estão configurados'

browserversion = 'O valor default é 96.0, ele é usado apenas nos testes que rodarão no Saucelabs'

platform = 'O valor default é Windows 10, ele é usado apenas nos testes que rodarão no Saucelabs'
```


---

### Glossário

`pages` Diretório onde é adicionado os scripts de cada página testada (PageObject).

`base_page.py` Arquivo base onde é programada as ações que serão utilizadas em cada teste, como entrar, clicar, etc.

`login_page.py` Arquivo onde estão os elementos e os requisitos usados nos testes da url `/login`, seguir esse padrão para outras páginas.

`tests` Diretório contendo os testes realizados e tudo utilizado para o teste.

`vendor` Diretório para armazenar os drivers dos navegadores utilizados pelo Selenium.

`config.py` Configuração do ambiente onde rodará o teste, conforme explicado acima.

`conftest.py` Script base utilizado para rodar o teste no ambiente, ele enxerga as informações adicionadas no arquivo `config.py`.

`login_test.py` Script dos testes da página de login, ele utiliza o código criado no arquivo `login_page` para fazer as ações do teste.

---

### Créditos
[<img src="assets\Iterasys-Logo.png" width="20%"/>][Iterasys]


<!-- links -->
[Iterasys]: https://iterasys.com.br/
[HerokuApp-Login]: http://the-internet.herokuapp.com/login
[Saucelabs]: https://saucelabs.com/

<!-- imagens -->
[QANinja-Logo]: assets/Iterasys-Logo.png (Iterasys-logo)
