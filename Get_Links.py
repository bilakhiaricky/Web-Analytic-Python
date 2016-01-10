# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 10:50:38 2015

@author: Ricky
"""

import time,os,codecs
from selenium import webdriver


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
username.send_keys("xxxxxxxx") 
password.send_keys("xxxxxxxxx") 
login_attempt = driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/table/tbody/tr/td[1]/input') 
login_attempt.submit() 


button1=driver.find_element_by_css_selector('#submit')
button1.click() #click on the button
time.sleep(2) #sleep
#main url of the item
outFolder='Indeed_DataScience_Resumes_Final'

# if the folder doesn't exist, make it 
if not os.path.exists(outFolder): # use path.exists() from the os library to check if something exists
    os.mkdir(outFolder) # use mkdir() from the os library to make a new directory

fileread1=tuple(open('user_name.txt','r'))
fileread2=tuple(open('user_id.txt','r'))
user_count=0

fileReader=open('resume_link.txt')

for line in fileReader: # this syntax allows us to read the file line-by-line
        
        link=line.strip() # .strip() removes white spaves and line-change characters from the beginning and end of a string
        
       # print 'Donwloading: ', link
        
        
        url=link

#open the browser and visit the url
        driver.get(url)
        
        time.sleep(2)
        html= driver.current_url
       # print html
        driver.get(html)
        html2=driver.page_source
        
        name=fileread1[user_count].strip()
        user_id = fileread2[user_count].strip()
        filename=name+"-"+user_id+".html"
        #open a new file in the pre-specified folder, write the html  , and close it.
        fileWriter=codecs.open(outFolder+'/'+filename, 'w','utf-8')
        fileWriter.write(html2)
        fileWriter.close()
        user_count+=1
        print user_count
fileReader.close()


