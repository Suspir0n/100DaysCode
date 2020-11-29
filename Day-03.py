import os    

username = str(input('What is your username at github: ')).lower()
language = str(input('What language do you wish search ? ')).lower()
github = str('https://github.com/')
complementation = str('?utf8=%E2%9C%93&tab=repositories&q=&type=&language=')
os.startfile(github + username + complementation + language)
