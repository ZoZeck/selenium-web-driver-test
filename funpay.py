import stdiomask
import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Script:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        print('\nPlease login!')
        self.driver.get('https://funpay.com/account/login')
        time.sleep(2)
        login = input('Введите login: ')
        password = stdiomask.getpass(prompt='Введите password: ')
        self.driver.find_element('xpath',
                            '/html/body/div[1]/div[1]/section/div[2]/div/div/div/form/div[2]/input[1]').send_keys(login)
        self.driver.find_element('xpath',
                            '/html/body/div[1]/div[1]/section/div[2]/div'
                            '/div/div/form/div[2]/input[2]').send_keys(password)
        self.captcha()

    def captcha(self):
        print('\nPlease enter captcha!')
        b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        time.sleep(2)
        self.driver.find_element('xpath', '//*[@id="content"]/div/div/div/form/div[4]/div').click()
        element = self.driver.find_element('xpath', '/html/body/div[2]/div[4]/iframe')
        time.sleep(2)
        self.driver.switch_to.frame(element)
        captcha = self.driver.find_element('xpath', '/html/body/div/div/div[2]/div[2]/div/table')
        image_name = captcha.get_attribute('class')
        while True:
            if image_name == 'rc-imageselect-table-33':
                number = input('Введите номер картинки или ok/stop: ')
                if number in b:
                    if number == '1':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]').click()
                    elif number == '2':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[2]').click()
                    elif number == '3':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[3]').click()
                    elif number == '4':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[1]').click()
                    elif number == '5':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[2]').click()
                    elif number == '6':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[3]').click()
                    elif number == '7':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[1]').click()
                    elif number == '8':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[2]').click()
                    elif number == '9':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[3]').click()
                elif number == 'ok':
                    self.driver.find_element('xpath', '//*[@id="recaptcha-verify-button"]').click()
                    break
                elif number == 'stop':
                    break
            elif image_name == 'rc-imageselect-table-44':
                number = input('Введите номер картинки или ok/stop: ')  # //*[@id="recaptcha-verify-button"]
                if number in b:
                    if number == '1':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]').click()
                    elif number == '2':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[2]').click()
                    elif number == '3':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[3]').click()
                    elif number == '4':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[4]').click()
                    elif number == '5':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[1]').click()
                    elif number == '6':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[2]').click()
                    elif number == '7':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[3]').click()
                    elif number == '8':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[2]/td[4]').click()
                    elif number == '9':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[1]').click()
                    elif number == '10':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[2]').click()
                    elif number == '11':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[3]').click()
                    elif number == '12':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[3]/td[4]').click()
                    elif number == '13':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[4]/td[1]').click()
                    elif number == '14':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[4]/td[2]').click()
                    elif number == '15':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[4]/td[3]').click()
                    elif number == '16':
                        self.driver.find_element('xpath', '//*[@id="rc-imageselect-target"]/table/tbody/tr[4]/td[4]').click()
                elif number == 'ok':
                    self.driver.find_element('xpath', '//*[@id="recaptcha-verify-button"]').click()
                elif number == 'stop':
                    break
        self.driver.switch_to.default_content()
        self.driver.find_element('xpath', '/html/body/div[1]/div[1]/section/div[2]/div/div/div/form/button').click()


    def funpay(self):
        self.driver.get('https://funpay.com/lots/461/trade')
        time.sleep(2)
        button = self.driver.find_element('xpath',
                                          '//*[@id="content"]/div/div/div[2]/div/div[1]/div[2]'
                                          '/div/div[1]/button').click()

    def message_handler(self):
        now = datetime.datetime.now()
        time.sleep(2)
        message = self.driver.find_element('xpath', '//*[@id="site-message"]')
        print(message.text, f'Time {now.hour}h:{now.minute}m\n')


def main():
    options = Options()
    # ПОЛЬЗОВАТЕЛЬ ДОЛЖЕН БЫТЬ АВТОРИЗОВАН В Default профиле Chrome!
    options.add_argument('user-data-dir=C:\\Users\\coolm\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # Если надо что бы окно браузера не запускалось.
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)

    while True:
        watcher = Script(driver)
        driver.get('https://funpay.com/')
        check = driver.find_element('xpath','/html/body/div/div[1]/header/div/nav/div[2]/div[2]/div/ul[2]/li[1]/a')
        if check.text == 'Войти':
            time.sleep(5)
            watcher.login()
        elif check.text == 'Log In':
            time.sleep(5)
            watcher.login()
        else:
            print('\nFunpay auto update....')
            watcher.funpay()
            watcher.message_handler()
            time.sleep(1800)


if __name__ == "__main__":
    main()
