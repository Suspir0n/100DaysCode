from selenium import webdriver
from time import sleep

class WhatsappBot:
    def __init__(self):
        self.menssege = '''Good night Guys, I'm creating a simple saber bot
                           how to work hehe. NOTE: If you are seeing this message
                           because it worked hehe'''
        self.group = "#100DaysOfCode"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def sendMenssege(self):
        self.driver.get('https://web.whatsapp.com/')
        sleep(40)
        group = self.driver.find_element_by_xpath('//span[@title="#100DaysOfCode"]')
        sleep(3)
        group.click()
        chat_box = self.driver.find_element_by_class_name('DuUXI')
        sleep(3)
        chat_box.send_keys(self.menssege)
        button_send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        sleep(3)
        button_send.click()
        sleep(5)

bot = WhatsappBot()
bot.sendMenssege()