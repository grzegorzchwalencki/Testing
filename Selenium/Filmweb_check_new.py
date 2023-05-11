# Import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# Open browser and navigate to website filmweb.pl
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.filmweb.pl/")

# Accept GDPR (RODO)
element = driver.find_element(By.ID, "didomi-notice-agree-button" )
element.click()

# Accept advertisement
driver.implicitly_wait(5)
advert_1 = driver.find_element(By.CLASS_NAME, "ws__skipButton")
sleep(3)
advert_1.click()

driver.implicitly_wait(5)

# Find elements and move mouse
ranking = driver.find_element(By.XPATH, '//a[@id="rankingsMenuLink"]')
move_mouse = webdriver.ActionChains(driver)
move_rank = move_mouse.move_to_element(ranking)
move_rank.perform()

news = driver.find_element(By.XPATH, '//a[@href="/ranking/premiere"]')
move_news = move_mouse.move_to_element(news).click()
move_news.perform()

sleep(5)

driver.quit()

