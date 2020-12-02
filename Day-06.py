from selenium import webdriver
from pyperclip import paste
from time import sleep
from argparse import ArgumentParser
import sys

class botTranslate():

    def __init__(self):
        self.site = 'https://www.deepl.com/pt-BR/translator'
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def parse_args(self):
        parser = ArgumentParser(description = 'Use a bot that automates word translation actions')
        parser.add_argument('bot_operation', help = 'Actions to be performed by the bot (\'searchword\' for search meaning, \'translateword\' for translate the word)')
        parser.add_argument('-w', dest = 'wordsTranslateFile', help = 'File containing the list of translated words')
        parser.add_argument('-m', dest = 'meaningOfWordFile', help = 'File containing the list of words with meaning')

        if len(sys.argv) <= 1:
            parser.print_help(sys.stderr)
            sys.exit(1)
        
        arguments = parser.parse_args()

        if arguments.bot_operation == 'searchword' or arguments.bot_operation == 'translateword':
            return arguments
        else:
            print('Error: ', arguments.bot_operation, 'is not a valid operation.\nValid choices: searchword or translateword.')

    def main(self):
        args = self.parse_args()

        if args.bot_operation == 'searchword':
            self.searchMeaningWord() 
        else:
            self.translateWord()

    def searchMeaningWord(self):
        # implement this method
        print('test')

    def translateWord(self):
        self.browser.get(self.site)
        print('Access the site!')
        word_translate = ''
        word = str(input('What the word what do you want to translate: '))
        sleep(10)
        input_text = self.browser.find_element_by_xpath('//*[@id="dl_translator"]/div[3]/div[2]/div[1]/div[2]/div/textarea')
        input_text.click()
        input_text.send_keys(word)
        sleep(3)
        self.browser.find_element_by_xpath('//*[@id="dl_translator"]/div[3]/div[2]/div[3]/div[3]/div[6]/div[1]/button').click()
        word_translate = paste()
        sleep(2)
        self.browser.close()
        data = word + ' = ' + word_translate + ';'
        self.createFile(data)
        print('Your word: {}\nYour translate: {}'.format(word, word_translate))

    def createFile(self, data):
        fileWord = open('C:/Users/Suspir0n/Documents/word_translate.txt', 'a')
        fileWord.write(data + '\n')
        fileWord.close() 

bot = botTranslate()
bot.translateWord() 
