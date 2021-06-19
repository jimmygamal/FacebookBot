#Creat By Mohamed Gamal
#Buy Me a cup of tea if you want VC 01016017092
# what's App +201016017092
#El7etan
#all Done
from selenium import  webdriver
import time
import PySimpleGUI as sg




layout = [  [sg.Text('Fb Commenter ')],
            [sg.Text(' Browse Your Accounts '), sg.Input(), sg.FileBrowse()],
            [sg.Text('Enter Post Link : '), sg.InputText()],
            [sg.Text(' Browse Your Cooment text '), sg.Input(), sg.FileBrowse()],
            [sg.Text('Change ip After : '), sg.InputText()],
            [sg.Button(' Start '), sg.Button('Cancel')] ]

window = sg.Window('Fb Commenter', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    time.sleep(1)
    count = 0
    count2 = 0
    count3 = 0

    def commenzt():
        global link
        time.sleep(0.5)
        driver.get('https://en-gb.facebook.com/login')
        time.sleep(1)
        global count
        global count2
        global  count3
        file  = open(values[0] ,encoding='utf-8')
        account = file.readlines()
        acc = account[count]
        driver.find_element_by_name('email').send_keys(acc.split(':')[0])
        driver.find_element_by_name('pass').send_keys(acc.split(':')[1])
        time.sleep(1)
        #driver.find_element_by_name('login').click()
        time.sleep(1.5)
        driver.get('https://en-gb.facebook.com/login')
        if driver.current_url == ('https://www.facebook.com/'):
            if count3 == values[3]:
                os.system('ipconfig -release')
                time.sleep(1.5)
                os.system('ipconfig -renew')
                time.sleep(2)
                count3=0
            file2 = open(values[2] ,encoding="utf8")
            comment = file2.readlines()
            fcomm = comment[count2]
            enk = str(values[1])
            link = enk.replace('www','mbasic')
            driver.get(link)
            time.sleep(0.5)
            driver.find_element_by_name('comment_text').send_keys(fcomm)
            try:
                driver.execute_script("document.querySelectorAll('[value=\"Comment\"]')[0].click();")
            except:
                driver.execute_script("document.querySelectorAll('[value = \"تعليق\"]')[0].click();")
            time.sleep(2)

            driver.delete_all_cookies()
            print('comment done')
            count=count+1
            count2=count2+1
            count3 = count3+1
            commenzt()
        else:
                count=count+1
                count3 = count3+1
                driver.delete_all_cookies()
                print('login faild')
                commenzt()
    commenzt()