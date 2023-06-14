import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from recoverymail import get_recovery_mail_code

# verification_code = ""
# while True:
#     verification_code = get_recovery_mail_code()
#     if verification_code.isdigit():
#         break;
# print(verification_code)
    
# # Set the path to the Chrome driver executable (replace "chromedriver.exe" with the appropriate path)
webdriver_service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=webdriver_service)
driver.get("https://mailfence.com/registration/?lg=en")

forms = driver.find_elements(By.TAG_NAME, "form")
register_form = forms[0]
firstname_field = register_form.find_element(By.CSS_SELECTOR, "[placeholder='First name']")
firstname_field.send_keys("ABC")

lastname_field = register_form.find_element(By.CSS_SELECTOR, "[placeholder='Last name']")
lastname_field.send_keys("DEF")

mail_field = register_form.find_element(By.CSS_SELECTOR, "[placeholder='Username']")
mail_field.send_keys("galaxytempmail213")

password_field = register_form.find_element(By.CSS_SELECTOR, "[placeholder='Password']")
password_field.send_keys("Password123!@#")

repassword_field = register_form.find_element(By.CSS_SELECTOR, "[placeholder='Confirm']")
repassword_field.send_keys("Password123!@#")

sign_up_button = register_form.find_element(By.CLASS_NAME, "btn-full")
sign_up_button.click()


email_form = forms[1]
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='email']")))
email_field.send_keys("galaxy.supersenior@outlook.com")

continue_button = email_form.find_element(By.CLASS_NAME, "btn-full")
continue_button.click()

wait = WebDriverWait(driver, 10)
robot_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "frc-button")))
robot_button.click()
# <button type="button" class="frc-button">Click to start verification</button>
time.sleep(10)
# wait = WebDriverWait(driver, 10) 
# register_form1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
# vorname_field = register_form1.find_element(By.NAME, "vorname")
# vorname_field.send_keys("aabbbccc")

# nachname_field = register_form1.find_element(By.NAME, "nachname")
# nachname_field.send_keys("aabbbccc")

# label = register_form1.find_element(By.XPATH, '//label[@for="permit_google_captcha_usage"]')
# driver.execute_script("arguments[0].click();", label)

# checkbox1 = register_form1.find_element(By.ID, "datenschutz")
# driver.execute_script("arguments[0].checked = true;", checkbox1)

# checkbox2 = register_form1.find_element(By.NAME, "agb")
# driver.execute_script("arguments[0].checked = true;", checkbox2)

# checkbox3 = register_form1.find_element(By.NAME, "widerruf")
# driver.execute_script("arguments[0].checked = true;", checkbox3)
# time.sleep(5)
# # response = openai.Completion.create(
# #     engine='text-davinci-003',  # Choose the appropriate model variant
# #     prompt='pants, snake, pineapple. - Which of these is a plant?' + ' Reply in a word.',
# #     max_tokens=50
# # )

# # generated_text = response.choices[0].text.strip()
# # print(generated_text)
# # Submit the form if necessary
# # Close the web driver
# driver.quit()
# # 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