import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Script:
    def __init__(self, driver):
        self.driver = driver

    def funpay(self):
        self.driver.get('https://funpay.com/lots/461/trade')
        time.sleep(2)
        button = self.driver.find_element('xpath','//*[@id="content"]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/button').click()

def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)

    while True:
        time.sleep(2)
        watcher = Script(driver)
        watcher.funpay()
        time.sleep(2)
        time.sleep(2)
        # time.sleep(14400)

if __name__ == "__main__":
    main()