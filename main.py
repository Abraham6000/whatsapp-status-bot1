from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

def start_bot():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-data-dir=/app/session")  # For persistent login
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)

    print("Launching WhatsApp Web...")
    driver.get("https://web.whatsapp.com")

    # Wait for user to scan QR if not logged in
    print("Waiting for QR scan or loading session...")
    time.sleep(30)  # Give enough time for QR scan (first time only)

    try:
        print("Finding Status tab...")
        status_button = driver.find_element(By.XPATH, '//div[@title="Status"]')
        status_button.click()
        time.sleep(3)

        print("Finding statuses...")
        statuses = driver.find_elements(By.XPATH, '//div[@aria-label="View status"]')
        for i, status in enumerate(statuses):
            try:
                print(f"Viewing status {i+1}")
                status.click()
                time.sleep(5)
                driver.find_element(By.XPATH, '//span[@data-icon="x"]').click()  # Close viewer
                time.sleep(2)
            except:
                continue

    except Exception as e:
        print(f"Something went wrong: {e}")

    driver.quit()

if __name__ == "__main__":
    while True:
        start_bot()
        print("Sleeping for 15 minutes before checking again...")
        time.sleep(900)
