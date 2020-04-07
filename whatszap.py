from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui,time 


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
name = input('Para quem é essa mensagem:')
msg = input('Escreva a msg aqui:')
numero = int(input('Quantas mensagens'))
input('Veja se vc esta Logado')

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_1Plpp')

for i in range(numero):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    time.sleep(3)
    button.click()






