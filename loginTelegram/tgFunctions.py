from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def login_telegram(browser,phone_num):
    '''function with steps to login in telegram web'''
    #find field phone_number and set num of cell phone
    phone = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_name('phone_number'))
    phone.send_keys(phone_num)
    phone.send_keys(Keys.ENTER)
    #find box and click ok to confirm cell phone
    box = WebDriverWait(browser, 10).until(lambda browser: browser.find_elements_by_tag_name('button'))
    box[1].click()
    #send code that you receive in your telegram
    code = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_name('phone_code'))
    code.send_keys(input('Phone Code: '))
    #loading page
    print('sleep time: 10 seconds'), sleep(10), print('sleep time over')


def new_tab(browser):
    '''open new tab in current browser'''
    switch = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_tag_name('body'))
    #open new tab
    switch.send_keys(Keys.CONTROL + 't')
    #switch to the new tab
    browser.switch_to_window(browser.window_handles[len(browser.window_handles) - 1])


if __name__ == '__main__':
    print('##### TESTS #####')

    browser = webdriver.Firefox()
    browser.get('https://www.google.com.br/')

    while True:
        new_tab(browser)
        browser.get('https://www.google.com.br/')
