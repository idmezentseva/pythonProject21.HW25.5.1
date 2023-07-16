import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


# Задание 25.3.1. Написать тест, который проверяет, что на странице со списком питомцев пользователя:
#
# 1. Присутствуют все питомцы.
# 2. Хотя бы у половины питомцев есть фото.
# 3. У всех питомцев есть имя, возраст и порода.
# 4. У всех питомцев разные имена.
# 5. В списке нет повторяющихся питомцев.(Сложное задание).

# 1. Присутствуют все питомцы.

def test_all_my_pets(test_show_my_pets):
    # Добавляем явное ожидание
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left"))
    )
    # Сохраняем в переменную stat_user данные статистики пользователя
    stat_user = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Получаем количество питомцев из данных статистики пользователя
    quantity = stat_user[0].text.split('\n')
    quantity = quantity[1].split(' ')
    quantity = int(quantity[1])
    # Добавляем явное ожидание
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td/a/div'))
    )
    # Получаем список всех строк таблицы (данные всех питомцев)
    pets_sum = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr/td/a/div')
    # Подсчитываем количество строк таблицы (количество питомцев)
    quantity_my_pets = len(pets_sum)
    # Сравниваем количество питомцев с данными статистики
    assert quantity_my_pets == quantity
