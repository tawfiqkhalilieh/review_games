from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from uuid import uuid4
from utils.convert_image_text import convert_image_text


def review_game(game_id: int):
    driver: webdriver.Chrome = webdriver.Chrome()

    driver.get("https://chess.com")
    driver.maximize_window()

    driver.find_element(By.ID, 'menu-cta').click()

    time.sleep(5)

    driver.find_element(By.ID, 'registration_username').send_keys( str(uuid4())[:23] )
    driver.find_element(By.ID, 'registration_email').send_keys(f'{ str(uuid4())[:15] }@gmail.com')
    driver.find_elements(By.CLASS_NAME, 'authentication-skill-level-selection-name')[-1].click()

    def create_account():
        driver.find_element(By.ID, 'registration_password').send_keys('passwordAA0')
        captcha_input = driver.find_elements(By.ID, 'registration_captcha')
        if captcha_input:
            captcha = driver.find_element(By.CLASS_NAME, 'captcha_image')    
            with open('captcha.png', 'wb') as file:
                file.write(captcha.screenshot_as_png)
            captcha_input[-1].send_keys(convert_image_text())
            
        time.sleep(2)

        driver.find_element(By.ID, 'registration_submit').click()

    create_account()

    while driver.current_url != 'https://www.chess.com/home':
        create_account()

    driver.get(f'https://www.chess.com/analysis/game/live/{game_id}?tab=review')

    time.sleep(10)

    driver.quit()