#import webdriver and commonkeys module which is in the selenium class 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create object of the webriver class in order to use it's functions
driver = webdriver.Chrome(executable_path='C:\\Desktop\\chromedriver')

#this further lines will do the automation by interacting with the browser and HTML elements and get you the required data. 
driver.get('https://web.whatsapp.com')
search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys('name of the person to send message',Keys.RETURN)
for i in range(1,100):
     write=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(i,Keys.RETURN)
