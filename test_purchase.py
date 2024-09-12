from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_purchase():
    # Настройка браузера
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Открыть сайт saucedemo
        driver.get('https://www.saucedemo.com/')
        time.sleep(2)

        # Авторизация
        username_input = driver.find_element(By.ID, 'user-name')
        password_input = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-button')

        username_input.send_keys('standard_user')
        password_input.send_keys('secret_sauce')
        login_button.click()
        time.sleep(2)

        # Добавить товар в корзину
        add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_to_cart_button.click()
        time.sleep(2)

        # Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_icon.click()
        time.sleep(2)

        # Проверить, что товар добавлен в корзину
        cart_item = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
        assert cart_item.text == 'Sauce Labs Backpack', "Товар не был добавлен в корзину"

        # Перейти к оформлению покупки
        checkout_button = driver.find_element(By.ID, 'checkout')
        checkout_button.click()
        time.sleep(2)

        # Заполнить данные для оформления
        first_name_input = driver.find_element(By.ID, 'first-name')
        last_name_input = driver.find_element(By.ID, 'last-name')
        postal_code_input = driver.find_element(By.ID, 'postal-code')

        first_name_input.send_keys('Test')
        last_name_input.send_keys('User')
        postal_code_input.send_keys('12345')

        continue_button = driver.find_element(By.ID, 'continue')
        continue_button.click()
        time.sleep(2)

        # Завершить покупку
        finish_button = driver.find_element(By.ID, 'finish')
        finish_button.click()
        time.sleep(2)

        # Проверить успешное завершение покупки
        complete_message = driver.find_element(By.CLASS_NAME, 'complete-header')
        assert complete_message.text.lower() == 'thank you for your order!', "Покупка не была завершена успешно"

        print("Тест завершен успешно: Покупка прошла.")

    finally:
        # Закрыть браузер
        driver.quit()

if __name__ == "__main__":
    test_purchase()
