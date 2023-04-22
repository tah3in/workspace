from selenium import webdriver
import time

# ایجاد یک instance از مرورگر Chrome
driver = webdriver.Chrome('/path/to/chromedriver')

# باز کردن صفحه اصلی اینستاگرام
driver.get('https://www.instagram.com/')

# صفحه ورود به اکانت کاربری
username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')
login_button = driver.find_element_by_xpath('//button[@type="submit"]')

# ورود به اکانت با اطلاعات کاربری
username_input.send_keys('نام کاربری')
password_input.send_keys('گذرواژه')
login_button.click()

# صفحه اینستاگرام پس از ورود به اکانت
time.sleep(5) # شکیبا باشید تا صفحه بالا بیاید
profile_link = driver.find_element_by_xpath('//a[@href="/profile/"]')
profile_link.click()

# صفحه پروفایل
followers_link = driver.find_element_by_xpath('//a[@href="/profile/followers/"]')
followers_link.click()

# لیست فالوورها
followers_list = driver.find_elements_by_xpath('//div[@role="dialog"]//ul/div/li')

# اسکرول کردن تا انتهای لیست فالوورها
for i in range(1, len(followers_list)):
    driver.execute_script("arguments[0].scrollIntoView();", followers_list[i])
    time.sleep(1)
