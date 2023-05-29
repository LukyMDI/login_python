from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from flask import Flask, render_template

app = Flask(__name__)

chrome_options = Options()
# chrome_options.add_argument("--headless")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/execute')
def execute():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    driver.get('https://app.minea.com/pt/auth/login')

    campo_usuario = driver.find_element('name', 'email')
    campo_senha = driver.find_element('name', 'password')
    # checkbox = driver.find_element('id', 'checkbox')

    # if not checkbox.is_selected():
    #     checkbox.click()

    campo_usuario.send_keys('adspy19913@valanides.com')
    campo_senha.send_keys('Spy123')

    campo_senha.submit()

    while True:
        pass


if __name__ == '__main__':
    app.run()
