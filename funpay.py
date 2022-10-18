import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Script:
    def __init__(self, driver):
        self.driver = driver

    def funpay_auto_update(self):
        self.driver.get('https://funpay.com/lots/461/trade')
        time.sleep(2)
        button = self.driver.find_element('xpath',
                                          '//*[@id="content"]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/button').click()

    def funpay_auto_sell(self):
        items = ['Golden', 'Skull', 'Mask', 'for', 'The', 'Trickster']
        selling_item = []
        while True:
            new_sale = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/a[1]')
            sales_gonk = self.driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[2]/a/span')
            # if sales_gonk.text == '1':
            for i in new_sale.text.split():
                if i in items:
                    selling_item.append(i)
                    item = ' '.join(selling_item)
            print(item)
            with open(f'{item}.txt', 'r') as txt:
                code_to_send = txt.readlines()[0]
                print(code_to_send, '----send')
                txt.close()
            with open(f'{item}.txt', 'r') as txt:
                code_to_save = txt.readlines()[1:]
                print(code_to_save, '----save')
                txt.close()
            with open(f'{item}.txt', 'w') as txt:
                for i in code_to_save:
                    txt.write(i)
                txt.close()
                print('----fin')
            time.sleep(2)
            # driver.get('https://funpay.com/orders/trade')
            # driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/a[1]').click()
            time.sleep(2)
            self.driver.get('https://funpay.com/en/chat/?node=47476840')
            JS_ADD_TEXT_TO_INPUT = """
                      var elm = arguments[0], txt = arguments[1];
                      elm.value += txt;
                      elm.dispatchEvent(new Event('change'));
                      """
            text = '''🟪🟪Благодарю за покупку🟪🟪\n
                    Ключ —  "1234565547"\n
                    После завершения проверки аккаунта:
                    1️⃣ Пожалуйста, зайдите в раздел "Мои покупки", выберите соответствующий заказ и нажмите кнопку "Подтвердить выполнение заказа";
                    2️⃣ Если Вам не сложно — оставьте отзыв о моей работе!'''
            chat = self.driver.find_element(By.XPATH, '//*[@id="comments"]/textarea')
            self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, chat, text)
            self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[3]/div[4]/form/div[3]/button/i').click()



def main():
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)

    while True:
        time.sleep(2)
        watcher = Script(driver)
        # watcher.funpay_auto_update()
        watcher.funpay_auto_sell()
        time.sleep(2)
        time.sleep(2)
        time.sleep(7200)

if __name__ == "__main__":
    main()