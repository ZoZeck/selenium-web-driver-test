import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class Script:
    def __init__(self, driver):
        self.driver = driver

    def money(self):
        self.driver.get('https://cs.money')
        time.sleep(2)
        while True:
            try:
                items_list = self.driver.find_element(By.CLASS_NAME, 'list_wrapper__2zFtP')
                ready_item = items_list.find_elements(By.CLASS_NAME, 'actioncard_wrapper__3jY0N')
                for item in ready_item:
                    item_info = item.text.split()
                    if item_info[0] == 'Вывод':
                        item_name = item_info[2]
                        withdraw_button = item.find_element(By.XPATH, '//*[@class="actioncard_buttons__1Bf3u"]/button')
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                print("\nOops! Try again...")
            else:
                break
        action = ActionChains(self.driver)
        action.move_to_element(withdraw_button)
        action.perform()
        withdraw_button.click()
        while True:
            try:
                steam_href = self.driver.find_elements(By.XPATH,
                                                       '//*[@id="modal"]/div/div[3]/div/div'
                                                       '/div[2]/div[1]/div/div/div[1]/div/div[4]/div/a/a')
                for trade_link in steam_href:
                    trade_link = trade_link.get_attribute("href")
                    print(f'\nYour trade link - {trade_link}')
                self.steam(trade_link, item_name)
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                time.sleep(2)
                print("\nTrade offer isn't ready...")
            else:
                break

    def steam(self, trade_link, item_name):
        self.driver.get(trade_link)
        while True:
            try:
                confirm_trade = self.driver.find_element(By.XPATH, '//*[@id="you_notready"]')
                self.driver.execute_script("arguments[0].click();", confirm_trade)
                self.driver.find_element(By.XPATH, '//*[@class="btn_green_steamui btn_medium"]').click()
                scroll_down = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                final_confirm = self.driver.find_element(By.XPATH, '//*[@id="trade_confirmbtn"]')
                error_mes = self.driver.find_element(By.XPATH, '//*[@id="notready_tradechanged_message"]')
                self.driver.execute_script("arguments[0].click();", final_confirm)
                try:
                    if error_mes.text == 'Предложение изменилось.':
                        while True:
                            try:
                                time.sleep(2)
                                self.driver.execute_script("arguments[0].click();", confirm_trade)
                                time.sleep(2)
                                self.driver.find_element(By.XPATH, '//*[@class="btn_green_steamui btn_medium"]').click()
                                time.sleep(2)
                                self.driver.execute_script("arguments[0].click();", final_confirm)
                            finally:
                                break
                finally:
                    continue
            except KeyboardInterrupt:
                print('\n=== Interrupted by User')
            except:
                print("\nOops! Try again...")
            finally:
                print(f'\nFinish! Item [{item_name}] in your inventory :3\n')
                break


def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # ↓ '--headless' to run chronium whithout interface
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe',
                              chrome_options=options)
    while True:
        watcher = Script(driver)
        watcher.money()
        time.sleep(5)


if __name__ == "__main__":
    main()
