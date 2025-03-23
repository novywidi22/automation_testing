import unittest
from utils.config import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestAddToCartNegative(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

        self.login_page.login("standard_user", "secret_sauce")

    def test_add_invalid_product(self):
        """Test menambahkan produk yang tidak ada"""
        self.inventory_page.add_to_cart("invalid-product")
        cart_count = self.inventory_page.get_cart_count()
        self.assertEqual(cart_count, 0)

    def test_add_same_product_twice(self):
        """Test menambahkan produk yang sama dua kali"""
        self.inventory_page.add_to_cart("sauce-labs-backpack")
        self.inventory_page.add_to_cart("sauce-labs-backpack")
        cart_count = self.inventory_page.get_cart_count()
        self.assertEqual(cart_count, 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
