# Importing required libraries
# pip install selenium
import self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

# Setting up the webdriver
driver = webdriver.Chrome()
#maximizing the window
driver.maximize_window()

# Navigating to the embark official site
driver.get("https://lassana.com/")
time.sleep(5)

#Access categories
categories= driver.find_element("xpath","(//div[@id='departmentsContainer'])[1]")
categories.click()
time.sleep(3)

#Hover on gifts from the navigation
gifts=driver.find_element("xpath","(//div[@id='departmentsRow'])[8]")
hover = ActionChains(driver).move_to_element(gifts)
hover.perform()
time.sleep(3)

#Select gifts from the navigation
giftSelector=driver.find_element("xpath","(//p[@id='departments2ndRow__title'])[4]")
giftSelector.click()
time.sleep(3)

#scroll down
driver.execute_script("scroll(0,1400)")
time.sleep(3)

#Select the cake to send
cakeSelection = driver.find_element("xpath","(//img[@alt='carouselItem'])[14]")
cakeSelection.click()
time.sleep(3)

#Increase the quantity
quantity=driver.find_element("xpath","(//div[@id='productQuantityChangeButton'])[2]")
quantity.click()
time.sleep(3)

#Add items to cart
addToCart=driver.find_element("xpath","(//div[@id='whiteButton'])[1]")
addToCart.click()
time.sleep(3)

#Check cart items
cart=driver.find_element("id","headerRightShopCartIcon")
cart.click()
time.sleep(3)

#Navigate to cart page
goToCart=driver.find_element("xpath","(//div[@class='footer__row2__whiteBtn'])[1]")
goToCart.click()
time.sleep(3)

#Add cake wording
addWording=driver.find_element("xpath","(//span[@class='lv-summarypg-cake-wording-edit-text'])[1]")
addWording.click()
cakeWording=driver.find_element("id","cakeWording")
cakeWording.send_keys("Happy B'day Papa!")
cakeWording.send_keys(Keys.RETURN)
time.sleep(2)

#continue
checkout=driver.find_element("id","lv-cartsummary-row3row8")
checkout.click()
time.sleep(3)

#Add recipient details
inputName=driver.find_element("xpath","(//input[@placeholder='Recipient Name'])[1]")
inputName.send_keys("Jayantha")
inputAddress=driver.find_element("xpath","(//textarea[@placeholder='Recipient Address'])[1]")
inputAddress.send_keys("89 , Aruppola")

#scroll down
driver.execute_script("scroll(0,400)")
time.sleep(3)

#Add city
inputCity=driver.find_element("xpath","(//div[@class='lv-reccity-cont'])[1]")
inputCity.click()
time.sleep(3)

#Handled elements which are not interactable
actions = ActionChains(driver)
actions.send_keys("Kandy")
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(3)

#Add phone number
inputPhoneNumber=driver.find_element("id","recCont1")
inputPhoneNumber.click()
inputPhoneNumber.send_keys("0772921475")
time.sleep(3)

#Add sender details
senderName=driver.find_element("id","detailCustName")
senderName.click()
time.sleep(3)
actions.send_keys("Ruwini")
actions.perform()
time.sleep(3)

#Add sender email
senderEmail=driver.find_element("id","detailCustEmail")
senderEmail.click()
time.sleep(3)
actions.send_keys("ru123@gmail.com")
actions.perform()
time.sleep(3)


#scroll down
driver.execute_script("scroll(0,900)")

#Add phone number
senderPhoneNumber=driver.find_element("id","detailCustMobNumb")
senderPhoneNumber.click()
time.sleep(3)
actions.send_keys("0770254903")
actions.perform()
time.sleep(3)

#Check anonymusSender checkbox
anonymousSender=driver.find_element("xpath","(//input[@name='isbeAnonyms'])[1]").click()

#Click continueToShopping Button
continueToShippingBtn=driver.find_element("xpath","(//button[@id='greenButton'])[1]").click()
time.sleep(7)

driver.execute_script("scroll(0,500)")
time.sleep(5)

#Select Deliver Month
selectMonth=driver.find_element("xpath","//button[@class='react-calendar__navigation__label']").click()
time.sleep(5)

#Select April as month
AprilMonthSelection=driver.find_element("xpath","//abbr[@aria-label='April 2024']").click()
time.sleep(3)

#Select date
dateSelection=driver.find_element("xpath","//abbr[@aria-label='April 28, 2024']").click()
time.sleep(3)
driver.execute_script("scroll(0,900)")

#Add delivery instructions
deliveryInstructions=driver.find_element("xpath","//body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/textarea[1]")
deliveryInstructions.click()
time.sleep(3)
deliveryInstructions.send_keys("Call the recipient before the delivery")

#Add personal message
personalMessage=driver.find_element("xpath","(//textarea[@placeholder='Personal Message'])[1]")
time.sleep(3)
personalMessage.click()
personalMessage.send_keys("Happy Birthday , We Love You Papa :)")
time.sleep(3)

#Select review button
reviewBtn=driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(3)

#Select payment option
paymentBtn=driver.find_element("xpath","(//div[@id='lv-pay-method2'])[1]").click()
time.sleep(3)

#Check agreement & Terms
agreeBtn=driver.find_element("xpath","//input[@id='agree']").click()
time.sleep(3)

#Select continue Button
continueBtn=driver.find_element("xpath","(//p[normalize-space()='Continue to Payments'])[1]").click()
time.sleep(5)

#Select Payment method
cardSelection=driver.find_element("xpath","//label[1]//div[1]").click()
#Wait till payment gateway loads
time.sleep(20)

