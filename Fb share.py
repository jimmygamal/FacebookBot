
# This Script Created By Mohamed Gamal
# whaat's App +201016017092

from selenium import  webdriver
import time
import PySimpleGUI as sg
import random

layout = [  [sg.Text('Fb share ')],
            [sg.Text(' Browse Your Accounts '), sg.Input(), sg.FileBrowse()],
            [sg.Text('Enter Post Link : '), sg.InputText()],
            [sg.Button(' Start '), sg.Button('Cancel')] ]
window = sg.Window('Fb Share', layout)
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
    count3 = 0
    def commenzt():
        global c
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
        if driver.current_url == ('https://www.facebook.com/'):
            pass
        else:
            count = count + 1
            driver.delete_all_cookies()
            print('login faild')
            commenzt()
        # driver.find_element_by_name('login').click()
        time.sleep(1.5)
        count=count+1
        def creat():
                global count2
                global count3
                while count2 < 10:
                    count3 = 0
                    c = random.randrange(1,9000)
                    lists =['dd','re','df','lkd','ldkg','sdgd','dgdg','kljsfsf','djghgdkghkd','lkdfjkldg','l0kjdg','retet']
                    e = random.choice(lists)
                    driver.get('https://en-gb.facebook.com/login')
                    if driver.current_url == ('https://www.facebook.com/'):
                        driver.get('https://m.facebook.com/pages/create/?ref_type=universal_creation_hub')
                        time.sleep(2)
                        try:
                            driver.execute_script("document.querySelectorAll('[data-sigil=\"touchable no_mpc\"]')[0].click();")
                        except:
                            pass
                        time.sleep(1)
                        try:
                            driver.find_elements_by_tag_name('input')[1].send_keys('sddgsdgsg'+str(c))
                        except:
                            pass
                        try:
                            try:
                                driver.execute_script("document.querySelectorAll('[value=\"التالي\"]')[0].click();")
                            except:
                                driver.execute_script("document.querySelectorAll('[value=\"Next\"]')[0].click();")
                        except:
                            pass

                        time.sleep(2)
                        try:
                            driver.find_elements_by_tag_name('option')[2].click()
                        except:
                            pass
                        time.sleep(2)
                        try:
                            driver.find_elements_by_tag_name('option')[16].click()
                        except:
                            pass
                        time.sleep(1)
                        try:
                            try:
                                driver.execute_script("document.querySelectorAll('[value=\"Next\"]')[0].click();")
                            except:
                                driver.execute_script("document.querySelectorAll('[value=\"التالي\"]')[0].click();")
                        except:
                            pass
                        time.sleep(20)
                        try:
                            try:
                                driver.execute_script("document.querySelectorAll('[value=\"Next\"]')[0].click();")
                            except:
                                driver.execute_script("document.querySelectorAll('[value=\"التالي\"]')[0].click();")
                        except:
                            pass
                        time.sleep(5)
                        try:
                            try:
                                driver.execute_script("document.querySelectorAll('[value=\"Next\"]')[0].click();")
                            except:
                                driver.execute_script("document.querySelectorAll('[value=\"التالي\"]')[0].click();")
                        except:
                            pass
                        try:
                            try:
                                driver.execute_script("document.querySelectorAll('[value=\"Next\"]')[0].click();")
                            except:
                                driver.execute_script("document.querySelectorAll('[value=\"التالي\"]')[0].click();")
                        except:
                            pass
                        time.sleep(5)
                        count2=count2+1
                        print(count2)
                        lunk = (str(driver.current_url))
                        driver.get(lunk.replace("m.facebook.com/" , "mbasic.facebook.com/"))
                        while int(count3) < 50:
                            try:
                                driver.find_element_by_name('xc_message').send_keys(str(values[1]))
                                time.sleep(2)
                                driver.find_element_by_name('view_post').click()
                                count3 = count3+1
                            except:
                                driver.get(lunk.replace("m.facebook.com/", "mbasic.facebook.com/"))
                                driver.find_element_by_name('xc_message').send_keys(str(values[1]))
                                time.sleep(2)
                                driver.find_element_by_name('view_post').click()
                                count3 = count3 + 1

                        if count2==10 :
                            count2=0
                            driver.delete_all_cookies()
                            commenzt()


        creat()

    commenzt()

