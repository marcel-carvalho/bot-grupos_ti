from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from tgFunctions import *

#colocar o numero do telefone com DDD ex: 021 7777-7777
phone = input('Phone number with DDD: ')
phone = '21995181636'
#login no telegram web
browser = webdriver.Firefox()
browser.get('https://web.telegram.org/#/login')
login_telegram(browser, phone)

# entrando no grupo
new_tab(browser)
browser.get('https://web.telegram.org/#/im?tgaddr=tg%3A%2F%2Fjoin%3Finvite%3DAAAAAEDrakjDNoJR0vtulw')
print('sleep time: 3 seconds'), sleep(3)
box_group = WebDriverWait(browser, 10).until(lambda browser: browser.find_elements_by_tag_name('button'))
box_group[2].click()

# coletando dados do grupo
browser.find_element_by_class_name('tg_head_btn').click()
data_group = {
    'name': None
    'users': None
}
name_group = browser.find_element_by_class_name('peer_modal_profile').text
num_users = browser.find_element_by_class_name('peer_modal_profile_description').text
print('Nome do Grupo: {}\n Numero de participantes: {}'.format(name_group, num_users))

#saindo do grupo


#browser.get('https://web.telegram.org/#/im?tgaddr=tg%3A%2F%2Fjoin%3Finvite%3DAAAAAEDrakjDNoJR0vtulw')
#browser.get('https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw')

#browser.quit()
