import unittest
from utils.config import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://www.saucedemo.com/")
        self.login_page.login("standard_user", "secret_sauce")

    def test_logout(self):
        """Tes logout pengguna dari aplikasi"""
        driver = self.driver
        
        # Klik tombol menu sidebar
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        
        # Tunggu hingga tombol logout muncul, lalu klik
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
        
        # Verifikasi pengguna berhasil logout
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/", "Logout gagal!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
