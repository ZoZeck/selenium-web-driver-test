import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Script:
    def __init__(self, driver):
        self.driver = driver

    def hh(self):
        while True:
            try:
                self.driver.get('https://spb.hh.ru/applicant/resumes?hhtmFromLabel=header&hhtmFrom=negotiations_item')
                self.driver.find_element('xpath',
                            '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div[1]/div[3]/div[2]/div/div['
                            '6]/div/div/div/div[1]/span/button').click()
            except:
                print('Not enough time has passed')
                time.sleep(1800)
            else:
                break
        time.sleep(1)
        self.driver.find_element('xpath', '/html/body/div[11]/div/div[1]/div[2]/div[1]/button').click()
        print('Резюме поднято!')

def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # r'C:\\chromedriver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)

    watcher = Script(driver)
    while True:
        watcher.hh()

if __name__ == "__main__":
    main()