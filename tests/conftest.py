from settings import valid_email, valid_password
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield
    pytest.driver.quit()


@pytest.fixture()
def test_show_my_pets():
    pytest.driver.maximize_window()
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Нажимаем на кнопку "Мои питомцы"
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
