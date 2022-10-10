from selenium import webdriver
from selenium.webdriver.common.by import By

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path='/Users/yennyalanis/Desktop/Automation/python-selenium-automation/chromedriver',options=c)
driver.implicitly_wait(0.5)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Continue button

driver.find_element(By.XPATH, "//input[@id='continue']")

#Need help link

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link

driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

#Other issues with sign-in link

driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")

#Create amazon account button

driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

#Conditions of use link

driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#Privacy of notice link

driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
