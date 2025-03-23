from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    def add_to_cart(self, product_id):
        """Menambahkan produk ke keranjang berdasarkan product_id"""
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_id}"))
        )
        add_button.click()

    def go_to_cart(self):
        """Navigasi ke halaman keranjang"""
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_button.click()
