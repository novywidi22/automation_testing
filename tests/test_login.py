import unittest
from utils.config import get_driver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

    def test_login_success(self):
        """Tes login dengan kredensial valid"""
        self.login_page.login("standard_user", "secret_sauce")
        self.assertNotIn("error", self.driver.current_url, "Login gagal, halaman error muncul.")

    def test_login_invalid_credentials(self):
        """Tes login dengan username atau password salah"""
        self.login_page.login("invalid_user", "wrong_password")
        error_message = self.login_page.get_error_message()
        self.assertIn("Username and password do not match", error_message)

    def test_login_empty_username(self):
        """Tes login dengan username kosong"""
        self.login_page.login("", "secret_sauce")
        error_message = self.login_page.get_error_message()
        self.assertIn("Username is required", error_message)

    def test_login_empty_password(self):
        """Tes login dengan password kosong"""
        self.login_page.login("standard_user", "")
        error_message = self.login_page.get_error_message()
        self.assertIn("Password is required", error_message)

    def test_login_empty_fields(self):
        """Tes login dengan username dan password kosong"""
        self.login_page.login("", "")
        error_message = self.login_page.get_error_message()
        self.assertIn("Username is required", error_message)

    def test_locked_out_user(self):
        """Tes login dengan akun yang dikunci"""
        self.login_page.login("locked_out_user", "secret_sauce")
        error_message = self.login_page.get_error_message()
        self.assertIn("Sorry, this user has been locked out", error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
