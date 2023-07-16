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

# 2. Хотя бы у половины питомцев есть фото.

def test_my_pets_quantity_photo(test_show_my_pets):
    # Сохраняем в переменную stat_user данные статистики пользователя
    stat_user = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Получаем количество питомцев из данных статистики пользователя
    quantity = stat_user[0].text.split('\n')
    quantity = quantity[1].split(' ')
    quantity = int(quantity[1])

    # Находим половину из полученного количества питомцев
    half_my_pets = quantity // 2

    # Добавляем неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Получаем список питомцев с фото и подсчитываем их количество
    images = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')
    images_my_pets = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            images_my_pets += 1

    # Проверяем, что количество питомцев с фото больше или равно половине всех питомцев
    assert images_my_pets >= half_my_pets
    print('\n')
    print(f'Половина количества питомцев: {half_my_pets}')
    print(f'Количество питомцев с фото: {images_my_pets}')
