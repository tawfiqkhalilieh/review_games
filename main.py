from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils.review_game import review_game

game_ids: list[str] = []
pages: list[str] = []

while True:
    page = input("Please enter a chess.com page: ")
    # example: https://www.chess.com/member/hikaru
    if not page:
        break
    pages.append(page)

driver: webdriver.Chrome = webdriver.Chrome()
driver.maximize_window()

for page in pages:
    lst: list = []
    driver.get("https://www.chess.com/member/tawfiqqqqq")
    time.sleep(5)
    ids = driver.find_elements(By.CLASS_NAME, 'archived-games-link')
    lst = [ str(id.get_attribute('href')).split("/")[-1] for id in ids]

    game_ids.extend(lst)

driver.quit()

for ch in game_ids:
    review_game(ch)