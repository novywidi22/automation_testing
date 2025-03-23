from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        """Melakukan login ke website"""
        self.driver.get("https://www.saucedemo.com/")

        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

        password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

    def get_error_message(self):
        """Mendapatkan pesan error jika login gagal"""
        try:
            error_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
            return error_element.text
        except:
            return None  # Jika tidak ada error message
