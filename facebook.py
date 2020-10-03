#import the libraries/modules which are required
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from secret import email,password


#create the object of the Options class to use the functions in that class.
option = Options()

#use the created object to call the functions 
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(options=option, executable_path='C:\\Users\\Desktop\\chromedriver')
driver.get('https://www.facebook.com')

time.sleep(1)

emailid=driver.find_element_by_xpath('//*[@id="email"]')
emailid.send_keys(email)

password=driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(password)
password.send_keys(Keys.RETURN)

time.sleep(1)

messenger=driver.find_element_by_name('mercurymessages').click()
new_mess=driver.find_element_by_id('u_0_f').click()
type=driver.find_element_by_xpath('//*[@id="js_16"]/div[1]/div/div/div/div/div').send_keys('enter the name here',Keys.ENTER)
messaas = driver.find_element_by_xpath('//*[@id="cch_f51ab88cd1b1fc"]/div/div/div[2]/div').send_keys('send message', Keys.ENTER)
#*
# try:
 #   search=driver.find_element_by_class_name('_58al')
  #  


#except:
   # print("Error occured")
