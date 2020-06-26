from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\Desktop\\chromedriver')
driver.get('https://web.whatsapp.com')
search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys('name of the person to send message',Keys.RETURN)
for i in range(1,100):
     write=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(i,Keys.RETURN)
