from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Aktifkan jika ingin mode headless
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver