from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()


# Задание 25.3.1. Написать тест, который проверяет, что на странице со списком питомцев пользователя:
#
# 1. Присутствуют все питомцы.
# 2. Хотя бы у половины питомцев есть фото.
# 3. У всех питомцев есть имя, возраст и порода.
# 4. У всех питомцев разные имена.
# 5. В списке нет повторяющихся питомцев.(Сложное задание).

# 3. У всех питомцев есть имя, возраст и порода.

def test_my_pets_information(test_show_my_pets):
    # Сохраняем в переменную stat_user данные статистики пользователя
    stat_user = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Получаем количество питомцев из данных статистики пользователя
    quantity = stat_user[0].text.split('\n')
    quantity = quantity[1].split(' ')
    quantity = int(quantity[1])

    # Добавляем неявное ожидание
    pytest.driver.implicitly_wait(10)
    # Находим элемент, соответствующий имени питомца и определяем его номер в списке
    names = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]')
    names_count = 0

    # Добавляем неявное ожидание
    pytest.driver.implicitly_wait(3)
    # Находим элемент, соответствующий породе питомца и определяем его номер в списке
    breeds = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[2]')
    breeds_count = 0

    # Добавляем неявное ожидание
    pytest.driver.implicitly_wait(3)
    # Находим элемент, соответствующий возрасту питомца и определяем его номер в списке
    ages = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[3]')
    ages_count = 0

    # Перебираем все имеющиеся в списке элементы, соответствующие имени, породе и возрасту
    for k in range(len(names)):
        if names[k].text != '':
            names_count += 1
        if breeds[k].text != '':
            breeds_count += 1
        if ages[k].text != '':
            ages_count += 1

    # Сравниваем количество найденных элементов с количеством питомцев
    assert names_count == quantity
    assert breeds_count == quantity
    assert ages_count == quantity
