import unittest
from utils.config import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

class TestRemoveFromCart(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)

        # Login ke aplikasi
        self.driver.get("https://www.saucedemo.com/")
        self.login_page.login("standard_user", "secret_sauce")

    def test_remove_item_from_cart(self):
        """Tes menghapus item dari keranjang"""
        driver = self.driver

        # Tambahkan produk ke keranjang
        self.inventory_page.add_to_cart("sauce-labs-backpack")
        self.inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
        
        # Masuk ke cart dan hapus salah satu item
        self.inventory_page.go_to_cart()
        self.cart_page.remove_item("sauce-labs-bolt-t-shirt")

        # Verifikasi apakah item berhasil dihapus
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), 1, "Item tidak berhasil dihapus!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
