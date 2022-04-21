from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


Web_URL = "https://www.instagram.com/accounts/login/"


class InstaCrawler:

    def query(self, url, name):
        base_url = url
        driver = webdriver.Chrome('./chromedriver')
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, 'username'))
            )
            print('Opening Instagram')
            username = driver.find_element_by_name('username')
            username.send_keys('username')

            password = driver.find_element_by_name('password')
            password.send_keys('password')

            login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
            login.click()
            print('Logging in')

            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(name)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a').click()
            print('Searching user')
            turnoff = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div'))
            )
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div').click()
            print('Opening First Image')
            pic = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[1]')
            action = ActionChains(driver)
            action.double_click(pic).perform()
            
            driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a').click()

            print('Liking All Images')
            while True:
                try:
                    pic = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[1]')
                    action = ActionChains(driver)
                    action.double_click(pic).perform()
                    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a[2]').click()
                    next = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a[2]')
                    if not next:
                        break
                except Exception:
                    continue

        finally:
            driver.quit()

insta = InstaCrawler()
insta.query(Web_URL, 'Target profile')
