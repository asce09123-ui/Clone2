from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

print("=== TikTok View Bot untuk Termux ===")

# Setup Firefox options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    print("Membuka Firefox...")
    driver = webdriver.Firefox(options=options)
    
    print("Membuka website...")
    driver.get("https://vipto.de")
    
    # Tunggu hingga halaman loading
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    print(f"Berhasil! Title: {driver.title}")
    print(f"URL: {driver.current_url}")
    
    # Simpan screenshot untuk debug
    driver.save_screenshot("screenshot.png")
    print("Screenshot disimpan sebagai screenshot.png")
    
    # Tunggu sebentar lalu close
    time.sleep(5)
    driver.quit()
    print("Browser ditutup. Test berhasil!")
    
except Exception as e:
    print(f"ERROR: {str(e)}")
    print("\nTips troubleshooting:")
    print("1. Pastikan Firefox terinstall: pkg install firefox")
    print("2. Pastikan geckodriver terinstall")
