"""
2048bot.py - Opens the game '2048' in the browser and deploys the simple strategy of repeatedly pressing
up, right, down, and left. Outputs the final score and number of moves obtained.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
browser.get('https://play2048.co/')
body = browser.find_element(By.TAG_NAME, 'body')

while True:
    # For detecting if the game is finished.
    game_over = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div/div[1]').text

    if not game_over:
        body.send_keys(Keys.UP)
        body.send_keys(Keys.RIGHT)
        body.send_keys(Keys.DOWN)
        body.send_keys(Keys.LEFT)
    else:
        gameover_text = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span').text
        print(gameover_text)
        break
browser.quit()