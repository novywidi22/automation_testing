from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Tunggu hingga 10 detik jika perlu

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
        success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
        assert success_message == "Thank you for your order!", "Checkout tidak berhasil!"
