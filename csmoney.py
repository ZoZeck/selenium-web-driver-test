import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Script:
    def __init__(self, driver):
        self.driver = driver

    def money(self):
        self.driver.get('https://cs.money')
        while True:
            try:
                # time.sleep(2)
                available = self.driver.find_element('xpath',
                                                     '/html/body/div[1]/div/div[1]/div[3]/div/div/div[1]/div/div/div['
                                                     '1]/div[ '
                                                     '2]/div[2]/div[2]/div/div[8]/div/div/div[2]/button')
                # self.driver.execute_script("arguments[0].click();", available)  # Нажать через .click() не работает
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                print("Oops! Try again...")
            else:
                break
        self.driver.execute_script("arguments[0].click();", available)  # Нажать через .click() не работает
        time.sleep(10)
        while True:
            try:
                href = self.driver.find_elements('xpath',
                                                 '/html/body/div[3]/div/div[3]/div/div/div[2]/div[1]/div/div/div['
                                                 '1]/div/div[4]/div/a/a')
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                print("Oops! Try again...")
            else:
                break
        # self.driver.execute_script("arguments[0].click();", href)
        for trade_link in href:
            trade_link = trade_link.get_attribute("href")
            print(trade_link)
        self.steam(trade_link)

    def steam(self, trade_link):
        self.driver.get(trade_link)
        # time.sleep(5)
        while True:
            try:
                time.sleep(1)
                steam_1 = self.driver.find_element('xpath',
                                                   '/html/body/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[1]/div['
                                                   '2]/div[ '
                                                   '1]/div[3]/div[2]')
                self.driver.execute_script("arguments[0].click();", steam_1)
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                print("Oops! Try again...")
            finally:
                time.sleep(1)
                self.driver.find_element('xpath', '/html/body/div[3]/div[3]/div/div[2]/div[1]').click()
                time.sleep(1)
                steam_3 = self.driver.find_element('xpath', '//*[@id="trade_confirmbtn"]')
                # Раскомментировать нижнюю строчку что бы обмен принялся до конца!
                # self.driver.execute_script("arguments[0].click();", steam_3)
                print('Finish')
                break


def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe',
                              chrome_options=options)  # r'C:\\chromedriver\\chromedriver.exe'

    watcher = Script(driver)
    watcher.money()
    time.sleep(5)


if __name__ == "__main__":
    main()
