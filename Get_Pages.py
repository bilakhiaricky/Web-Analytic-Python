# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 10:50:38 2015

@author: Ricky
"""

import re,urllib2
import time,sys
import codecs
from selenium import webdriver
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

filewrite=codecs.open('user_name.txt','w','utf-8')
filewrite2=codecs.open('resume_link.txt','w','utf-8')
filewrite1=codecs.open('user_id.txt','w','utf-8')
#extract the set of users in a given html page and add them to the given set

#main url of the item
url='http://www.indeed.com/resumes?q=%22data+scientist%22&co=US'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#sleep for 2 seconds
time.sleep(2)

button=driver.find_element_by_css_selector('#userOptionsLabel')
button.click() #click on the button
time.sleep(2) #sleep
username = driver.find_element_by_css_selector("#signin_email")
password = driver.find_element_by_css_selector("#signin_password")
username.send_keys("xxxxxxxxx") 
password.send_keys("xxxxxxxxxxx") 
login_attempt = driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/table/tbody/tr/td[1]/input') 
login_attempt.submit() 


button1=driver.find_element_by_css_selector('#submit')
button1.click() #click on the button
time.sleep(2) #sleep


myHTML1=driver.page_source

user_link=re.finditer('data-tn-link="" href="(.*?)"',myHTML1)#get all the matches
user_name=re.finditer('itemprop="url">(.*?)<',myHTML1)
user_id=re.finditer('<li id="(.*?)"',myHTML1)  
for user_link_1 in user_link:
       user_link_final=user_link_1.group(1)
       #print user_link_final
       filewrite2.write("http://www.indeed.com"+str(user_link_final) + '\n')
#filewrite2.close()
for user_name_1 in user_name:
       user_name_final=user_name_1.group(1)
       user_name_final=re.sub(r'[^\w\d]',"_",user_name_final)
       #print user_name_final
       filewrite.write(user_name_final + '\n')     
for user_id_1 in user_id:
       user_id_final=user_id_1.group(1)
       user_id_final=re.sub(r'[^\w\d]',"_",user_id_final)
       #print user_name_final
       filewrite1.write(user_id_final + '\n')
print 'page 1 done'


page=2
while True:
    #get the css path of the 'next' button
    cssPath='#pagination > a.instl.confirm-nav.next'
    
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break

    #click the button to go the next page, then sleep    
    button.click()
    time.sleep(2)
    print 'page',page,'done'
    page+=1
    myHTML1=driver.page_source
    #parse the page
    user_link=re.finditer('data-tn-link="" href="(.*?)"',myHTML1)#get all the matches
    user_name=re.finditer('itemprop="url">(.*?)<',myHTML1)
    user_id=re.finditer('<li id="(.*?)"',myHTML1)  
    for user_link_1 in user_link:
       user_link_final=user_link_1.group(1)
       #print user_link_final
       filewrite2.write("http://www.indeed.com"+str(user_link_final) + '\n')
#filewrite2.close()
    for user_name_1 in user_name:
       user_name_final=user_name_1.group(1)
       user_name_final=re.sub(r'[^\w\d]',"_",user_name_final)
       #print user_name_final
       filewrite.write(user_name_final + '\n')     
    for user_id_1 in user_id:
       user_id_final=user_id_1.group(1)
       user_id_final=re.sub(r'[^\w\d]',"_",user_id_final)
       #print user_name_final
       filewrite1.write(user_id_final + '\n') 
filewrite2.close()
filewrite.close()
filewrite1.close()

    
