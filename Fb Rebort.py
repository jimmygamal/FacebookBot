from selenium import  webdriver
import time
import PySimpleGUI as sg
#This script Created by Mohamed Gamal
#What's App +201016017092
layout = [  [sg.Text('Fb Reborter ')],
            [sg.Text(' Browse Your Accounts '), sg.Input(), sg.FileBrowse()],
            [sg.Text('Enter Profile Or Page  Link : '), sg.InputText()],
            [sg.Text('Enter What You Want 1 or 2 : '), sg.InputText()],
            [sg.Button(' Start '), sg.Button('Cancel')] ]

window = sg.Window('Fb Reborter', layout)

while True:

    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            sg.popup_ok('Created By / Mohamed Gamal')
            break
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    time.sleep(1)
    driver.get('https://en-gb.facebook.com/login')
    count2 = 0
    count = 0
    def block():
        global count2
        time.sleep(0.5)
        driver.get('https://en-gb.facebook.com/login')
        time.sleep(1)
        global count
        file = open(values[0],encoding='utf-8')
        account = file.readlines()
        acc = account[count]
        driver.find_element_by_name('email').send_keys(acc.split(':')[0])
        driver.find_element_by_name('pass').send_keys(acc.split(':')[1])
        time.sleep(1)
        # driver.find_element_by_name('login').click()
        time.sleep(1.5)
        driver.get('https://en-gb.facebook.com/login')
        if driver.current_url == ('https://www.facebook.com/'):
            if count2 == 7:
                myText = 'please change Ip and click Ok '
                language = 'en'
                ooutput = gTTS(text=myText, lang=language, slow=False)
                ooutput.save('ooutput.mp3')
                playsound.playsound('ooutput.mp3', False)
                sg.popup_ok(' please change Ip and click Ok ')
                count2=0

            if values[2] == '1':
                enk = str(values[1])
                link = enk.replace('www', 'mbasic')
                driver.get(link)
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath('//a[text()="More"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="المزيد"]').click()

                time.sleep(1)
                try:
                    driver.find_element_by_xpath('//a[text()="Find Support or Report Profile"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="البحث عن دعم أو الإبلاغ عن ملف شخصي"]').click()
                try:
                    driver.find_element_by_xpath('//span[text()="Fake Account"]').click()
                except:
                    driver.find_element_by_xpath('//span[text()="حساب زائف"]').click()
                driver.find_element_by_name('action').click()
                try:
                    driver.find_element_by_xpath('//span[text()="Report profile"]').click()
                except:
                    driver.find_element_by_xpath('//span[text()="الإبلاغ عن ملف شخصي"]').click()
                driver.find_element_by_name('action').click()
                time.sleep(0.9)
                driver.get(link)
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath('//a[text()="More"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="المزيد"]').click()

                time.sleep(1)
                try:
                    driver.find_element_by_xpath('//a[text()="Find Support or Report Profile"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="البحث عن دعم أو الإبلاغ عن ملف شخصي"]').click()
                try:
                    driver.find_element_by_xpath('//span[text()="Fake Name"]').click()
                except:
                    driver.find_element_by_xpath('//span[text()="اسم زائف"]').click()
                driver.find_element_by_name('action').click()
                time.sleep(0.5)
                driver.find_element_by_name('action').click()
                time.sleep(0.5)
                time.sleep(0.9)
                driver.get(link)
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath('//a[text()="More"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="المزيد"]').click()

                time.sleep(1)
                try:
                    driver.find_element_by_xpath('//a[text()="Find Support or Report Profile"]').click()
                except:
                    driver.find_element_by_xpath('//a[text()="البحث عن دعم أو الإبلاغ عن ملف شخصي"]').click()
                try:
                    driver.find_element_by_xpath('//span[text()="انتحال شخصية شخص ما"]').click()
                except:
                    driver.find_element_by_xpath('//span[text()="Pretending to Be Someone"]').click()
                driver.find_element_by_name('action').click()
                time.sleep(0.5)
                try:
                    driver.find_element_by_xpath('//span[text()="شخصية شهيرة"]').click()
                except:
                    driver.find_element_by_xpath('//span[text()="Celebrity"]').click()
                time.sleep(0.5)
                driver.find_element_by_name('action').click()
                try:
                    driver.execute_script("document.querySelectorAll('[value=\"REPORT_CONTENT\"]')[0].click();")
                except:
                    pass
                driver.find_element_by_name('action').click()

                driver.delete_all_cookies()
                count2=count2+1
                count = count + 1
                block()
            if values[2] == '2':
                enk = str(values[1])
                link = enk.replace('www', 'mbasic')
                driver.get(link)
                time.sleep(0.5)
                driver.execute_script("document.getElementsByClassName('cw')[3].click();")#more
                time.sleep(0.5)
                driver.execute_script("document.getElementsByClassName('bz')[1].click();")#rebort
                time.sleep(0.5)
                driver.execute_script("document.getElementsByTagName('table')[4].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"fake\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue2
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"MARK_AS_SCAM\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Submit\"]')[0].click();")#submit
                time.sleep(0.5)
                driver.get(link)
                time.sleep(1)
                driver.execute_script("document.getElementsByClassName('cw')[3].click();")  # more
                time.sleep(0.5)
                driver.execute_script("document.getElementsByClassName('bz')[1].click();")  # rebort
                time.sleep(0.5)
                driver.execute_script("document.getElementsByTagName('table')[3].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"pornographic\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue2
                time.sleep(0.5)
                try:
                    driver.execute_script("document.querySelectorAll('[value=\"REPORT_CONTENT\"]')[0].click();")
                except:
                    pass
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Submit\"]')[0].click();")#submit
                driver.get(link)
                time.sleep(1)
                driver.execute_script("document.getElementsByClassName('cw')[3].click();")  #more
                time.sleep(0.5)
                driver.execute_script("document.getElementsByClassName('bz')[1].click();")  #rebort
                time.sleep(0.5)
                driver.execute_script("document.getElementsByTagName('table')[3].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")  # continue
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"hatespeech\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue2
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"gender\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")#continue3
                time.sleep(0.5)
                try:
                    driver.execute_script("document.querySelectorAll('[value=\"REPORT_CONTENT\"]')[0].click();")
                except:
                    pass
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Submit\"]')[0].click();")#submit
                driver.get(link)
                time.sleep(1)
                driver.execute_script("document.getElementsByClassName('cw')[3].click();")  # more
                time.sleep(0.5)
                driver.execute_script("document.getElementsByClassName('bz')[1].click();")  # rebort
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"harassment\"]')[0].click();")
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Continue\"]')[0].click();")  # continue
                time.sleep(0.5)
                try:
                    driver.execute_script("document.querySelectorAll('[value=\"REPORT_CONTENT\"]')[0].click();")
                except:
                    pass
                time.sleep(0.5)
                driver.execute_script("document.querySelectorAll('[value=\"Submit\"]')[0].click();")#submit
                driver.delete_all_cookies()
                print('comment done')
                count2 = count2 + 1
                count = count + 1
                block()

        else:
            if count2 == 14:
                myText = 'please change Ip and click Ok '
                language = 'en'
                ooutput = gTTS(text=myText, lang=language, slow=False)
                ooutput.save('ooutput.mp3')
                playsound.playsound('ooutput.mp3', False)
                sg.popup_ok(' please change Ip and click Ok ')
                count2 = 0
            count2=count2+1
            print(count2)
            count = count + 1
            driver.delete_all_cookies()
            block()

    block()


