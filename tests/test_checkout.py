from utils.config import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

driver = get_driver()
login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)
cart_page = CartPage(driver)
checkout_page = CheckoutPage(driver)

login_page.login("standard_user", "secret_sauce")
inventory_page.add_to_cart("sauce-labs-backpack")
inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")

inventory_page.go_to_cart()
cart_page.proceed_to_checkout()

checkout_page.enter_checkout_info("John", "Doe", "12345")
checkout_page.finish_checkout()

print("Test Checkout: Sukses!")
driver.quit()
