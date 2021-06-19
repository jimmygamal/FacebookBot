#This Script Created By Mohamed Gamal
# What's APp +201016017092
from selenium import  webdriver
import time
import PySimpleGUI as sg
count2 = 0

layout = [  [sg.Text('Fb Group Joiner  ')],
            [sg.Text(' Browse Your Accounts '), sg.Input(), sg.FileBrowse()],
            [sg.Text(' Browse Your Groups IDs '), sg.Input(), sg.FileBrowse()],
            [sg.Button(' Start '), sg.Button('Cancel')] ]
window = sg.Window('Fb Group Joiner ', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            sg.popup_ok('Created By / Mohamed Gamal')
            break
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    time.sleep(1)
    count = 0

    def commenzt():

        global c
        global link
        time.sleep(0.5)
        driver.get('https://en-gb.facebook.com/login')
        time.sleep(1)
        global count
        file = open(values[0], 'r')
        account = file.readlines()
        acc = account[count]
        driver.find_element_by_name('email').send_keys(acc.split(':')[0])
        driver.find_element_by_name('pass').send_keys(acc.split(':')[1])
        driver.find_element_by_name('login').click()
        time.sleep(1)
        try:
            driver.find_element_by_name('approvals_code').send_keys(acc.split(':')[2])
            driver.find_element_by_id('checkpointSubmitButton').click()
            time.sleep(0.5)
            driver.find_element_by_id('checkpointSubmitButton').click()
        except:
            pass
        time.sleep(1)
        count=count+1

        driver.get('https://en-gb.facebook.com/login')
        def join ():
            global count2
            driver.get('https://en-gb.facebook.com/login')

            if driver.current_url == ('https://www.facebook.com/'):
                file = open(values[1], 'r')
                ids = file.readlines()
                id = ids[count2]
                a =count2
                c= a+1
                print(c)
                if c >= ids.__len__():
                    count2 = 0
                    driver.delete_all_cookies()
                    print(ids.__len__())
                    print(count2)
                    commenzt()
                driver.get('https://mbasic.facebook.com/groups/'+ id)
                try:
                    try:
                        time.sleep(0.4)
                        driver.execute_script('document.querySelectorAll(\'[value="Join Group"]\')[0].click();')
                    except:
                        driver.execute_script('document.querySelectorAll(\'[value="انضمام إلى المجموعة"]\')[0].click();')
                    try:
                        driver.execute_script('document.querySelectorAll(\'[value="Send Response"]\')[0].click();')

                    except:
                        driver.execute_script('document.querySelectorAll(\'[value="إرسال رد"]\')[0].click();')
                except:
                    print('a7a')
                    count2 = count2 + 1
                    join()
                count2 = count2 + 1

                join()
            else:
                driver.delete_all_cookies()
                commenzt()
        join()
    commenzt()