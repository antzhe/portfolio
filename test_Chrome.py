from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re

url = 'http://ya.ru/'
login = 'login'
password = 'password'


# Получение результатов выдачи через поисковое поле на главной странице Яндекса
def test_searching():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    search_input = driver.find_element(By.ID, 'text')  # Поииск поля для ввода
    search_input.send_keys('Автотест')  # Ввод символов в поле
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CLASS_NAME, 'search3__button'))).click()  # Ожидание кнопки Найти и клик в нее
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html")))  # Ожидание загрузки новой страницы
    assert driver.find_elements(By.CLASS_NAME, 'serp-item')  # Проверка наличия выдачи на странице
    driver.close()


# Авторизация на главной странице Яндекса через кнопку "Войти"
def test_login():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.CLASS_NAME, 'home-link2_color_black').click()  # Поиск кнопки "Войти" и клик в неё
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'passp-field-login').send_keys(
        login)  # Ожидание появления поля для логина и ввод символов в поле
    driver.find_element(By.ID, 'passp:sign-in').click()  # Клик по кнопке "Войти"
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'passp-field-passwd')))  # Ожидание появления поля для пароля
    driver.find_element(By.ID, 'passp-field-passwd').send_keys(password)  # Ввод символов в поле пароль
    driver.find_element(By.ID, 'passp:sign-in').click()  # Клик по кнопке "Войти"
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME,
                        'usermenu-link-redesign_js_inited').click()  # Ожидание загрузки кнопки профиля на главной странице и клик в неё
    driver.implicitly_wait(10)
    user_mail = driver.find_element(By.CLASS_NAME,
                                    'usermenu-redesign__user-mail').text  # Ожидание открытия профиля и сохранение в переменную имени почты пользователя
    assert re.search(fr'{login}\S+', user_mail)  # Проверки совпадения логина пользователя и его имени почты
    driver.close()


# Прверка открытия меню
def test_open_menu():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.CLASS_NAME, 'headline__personal-menu').click()  # Поиск кнопки меню и клик в неё
    driver.implicitly_wait(10)
    assert driver.find_elements(By.XPATH, "//a[@aria-expanded='true']")  # Проаверка раскрытия меню
    driver.close()


# Прверка наличия всех кнопок в меню
def test_menu():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.CLASS_NAME, 'headline__personal-menu').click()  # Поиск кнопки меню и клик в неё
    driver.implicitly_wait(10)
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__login-button")  # Кнопка Войти
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__plus")  # Кнопка Плюс
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__create_mail")  # Кнопка Почты
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__messenger")  # Кнопка Сообщения
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__favorites")  # Кнопка Избранное
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__market")  # Кнопка Корзина
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__disk")  # Кнопка Диск
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__reviews")  # Кнопка Отзывы
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__add_child")  # Кнопка Детского аккаунта
    assert driver.find_elements(By.XPATH, "//a[@data-statlog='mail.login.usermenu.search_settings']")  # Кнопка Настроек
    assert driver.find_elements(By.CLASS_NAME, "usermenu-redesign__switch-design")  # Кнопка Старой версии
    assert driver.find_elements(By.XPATH, "//a[@data-statlog='mail.login.usermenu.help']")  # Кнопка Справик
    assert driver.find_elements(By.XPATH,
                                "//a[@data-statlog='mail.login.usermenu.user_agreement']")  # Кнопка Пользовательского соглашения
    assert driver.find_elements(By.XPATH,
                                "//a[@data-statlog='mail.login.usermenu.privacy']")  # Кнопка Конфиденциальности
    assert driver.find_elements(By.XPATH, "//a[@data-statlog='mail.login.usermenu.blog']")  # Кнопка Блога
    assert driver.find_elements(By.XPATH, "//a[@data-statlog='mail.login.usermenu.company']")  # Кнопка О компании
    driver.close()


# Прверка перехода на сервис погода по клику на значок погоды под поисковой строкой
def test_weather():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.CLASS_NAME, 'informers3__weather').click()  # Поиск кнопки погоды и клик в неё
    driver.implicitly_wait(10)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)  # Переключение на вкладку с погодой
    new_window_url = driver.current_url
    assert re.search(fr'https://yandex.ru/pogoda\S+', new_window_url)  # Проверка совпадение ссылки с адресом сервиса
    driver.close()


#  Проверка перехода на поисковой запрос курса доллара по клику на значок курса доллара под поисковой строкой
def test_usd():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.XPATH, "//a[@title='USD MOEX']").click()  # Поиск кнопки курса доллара и клик в неё
    driver.implicitly_wait(10)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)  # Переключение на вкладку с запросом курса доллара
    input_value = driver.find_element(By.CLASS_NAME, 'mini-suggest__input').get_attribute('value')
    assert input_value == 'USD MOEX'  # Проверка совпадения запроса курса доллара в поисковой строке
    driver.close()


#  Проверка перехода на поисковой запрос курса евро по клику на значок курса евро под поисковой строкой
def test_eur():
    driver = webdriver.Chrome()  # Запуск браузера
    driver.maximize_window()  # Открытие браузера на весь экран
    driver.get(url)  # Открытие страницы в браузере
    driver.find_element(By.XPATH, "//a[@title='EUR MOEX']").click()  # Поиск кнопки курса доллара и клик в неё
    driver.implicitly_wait(10)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)  # Переключение на вкладку с запросом курса доллара
    input_value = driver.find_element(By.CLASS_NAME, 'mini-suggest__input').get_attribute('value')
    assert input_value == 'EUR MOEX'  # Проверка совпадения запроса курса доллара в поисковой строке
    driver.close()
