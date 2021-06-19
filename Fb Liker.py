from selenium import  webdriver
import time
import PySimpleGUI as sg
# all done
# This Script Created By Mohamed Gamal
# What's App +201016017092

layout = [  [sg.Text('Fb Liker ')],
            [sg.Text(' Browse Your Accounts '), sg.Input(), sg.FileBrowse()],
            [sg.Text('Enter Post Link : '), sg.InputText()],
            [sg.Button(' Start '), sg.Button('Cancel')] ]
window = sg.Window('Fb Liker', layout)
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
    count2 = 0


    def commenzt():
        global link
        time.sleep(0.5)
        driver.get('https://en-gb.facebook.com/login')
        time.sleep(1)
        global count
        global count2
        file = open(values[0], 'r')
        account = file.readlines()
        acc = account[count]
        driver.find_element_by_name('email').send_keys(acc.split(':')[0])
        driver.find_element_by_name('pass').send_keys(acc.split(':')[1])
        time.sleep(1)
        # driver.find_element_by_name('login').click()
        time.sleep(1.5)
        driver.get('https://en-gb.facebook.com/login')
        if driver.current_url == ('https://www.facebook.com/'):
            enk = str(values[1])
            link = enk.replace('www', 'mbasic')
            driver.get(link)
            time.sleep(1)
            try:
                try:
                    driver.find_element_by_xpath('//span[text()="React"]').click()
                except:
                    pass
            except:
                try:
                    driver.find_element_by_xpath('//span[text()="تفاعل"]').click()
                except:
                    pass
            time.sleep(1)
            try:
                driver.find_element_by_xpath('//span[text()="Like"]').click()
                try:
                    driver.find_element_by_xpath('//span[text()="Like"]').click()
                except:
                    pass
            except:
                try:
                    driver.find_element_by_xpath('//span[text()="أعجبني"]').click()
                except:
                    pass


            driver.delete_all_cookies()
            count=count+1
            count2=count2+1
            commenzt()

        else:
            count = count + 1
            driver.delete_all_cookies()

            commenzt()
    commenzt()