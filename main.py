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

driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/")
driver.find_element(By.ID, "username").send_keys("saddsadadddsddda312222")
driver.find_element(By.ID, "password").send_keys("saddsadadddsddda312222AA0")
driver.find_element(By.ID, "toggle-password-visibility").click()

input("Click Once you login")
# https://www.chess.com/games/archive/thelolman2?gameOwner=other_game&gameTypes%5B0%5D=chess960&gameTypes%5B1%5D=daily&gameType=live&page=1

for page in pages:
    lst: list = []
    driver.get(page)
    time.sleep(10)
    ids = driver.find_elements(By.CLASS_NAME, "archive-games-link")
    lst = [str(id.get_attribute("href")).split("/")[-1].split("?")[0] for id in ids]

    game_ids.extend(lst)

driver.quit()

print(game_ids)

game_ids = list(set(game_ids))

for ch in game_ids:
    try:
        review_game(ch)
    except Exception as e:
        print(ch)
