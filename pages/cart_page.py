from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    def remove_item(self, product_id):
        """Menghapus item dari cart berdasarkan product_id"""
        remove_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, f"remove-{product_id}"))
        )
        remove_button.click()

    def proceed_to_checkout(self):
        """Klik tombol checkout untuk lanjut ke pembayaran"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
