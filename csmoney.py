import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Script():
    def __init__(self, driver):
        self.driver = driver

    def money(self):
        self.driver.get('https://cs.money')
        try:
            time.sleep(5)
            third = self.driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[8]/div/div/div[2]/button')
            self.driver.execute_script("arguments[0].click();", third)  # Нажать на third, click() не работает
            time.sleep(10)
            elems = self.driver.find_elements('xpath',
                                              '/html/body/div[3]/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div/a/a')
            for elem in elems:
                print(elem.get_attribute("href"))
                link = elem.get_attribute("href")
        except:
            time.sleep(5)
            third = self.driver.find_element('xpath','/html/body/div[1]/div/div[1]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[8]/div/div/div[2]/button')
        finally:
            self.steam(link)

    def steam(self, link):
        self.driver.get(link)
        time.sleep(5)
        try:
            time.sleep(1)
            steam_1 = self.driver.find_element('xpath', '/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]')
        except:
            time.sleep(1)
            steam_1 = self.driver.find_element('xpath', '/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]')
        self.driver.execute_script("arguments[0].click();", steam_1)
        time.sleep(1)
        steam_2 = self.driver.find_element('xpath','/html/body/div[3]/div[3]/div/div[2]/div[1]').click()
        time.sleep(1)
        steam_3 = self.driver.find_element('xpath','//*[@id="trade_confirmbtn"]')
        self.driver.execute_script("arguments[0].click();", steam_3)

def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    driver = webdriver.Chrome(executable_path=r'C:\\chromedriver\\chromedriver.exe', chrome_options=options)

    watcher = Script(driver)
    watcher.money()
    # watcher.steam()

if __name__ == "__main__":
    main()