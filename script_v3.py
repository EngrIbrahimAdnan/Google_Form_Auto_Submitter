import requests, threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options(); chrome_options.add_argument("--headless"); chrome_options.add_argument("--disable-gpu")
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdiDOrhjhKsgZyfJX5ph092-1crzyiavfHgszUw3qyf85VTLg/viewform?usp=sf_link"

def identify():
    try:
        soup = BeautifulSoup(requests.get(form_url).content, "html.parser")
        [print(f"Question {i}: {q.find('div', {'role': 'heading'}).get_text(strip=True)} ({'Multiple Choice' if q.find('div', {'role': 'radio'}) else 'Short Answer' if q.find('input', {'type': 'text'}) else 'Paragraph'})") for i, q in enumerate(soup.find_all('div', {'role': 'listitem'}), 1)]
    except Exception as e: print("An error occurred while identifying question nature:", e)

def submit_form():
    global n; driver = webdriver.Chrome(options=chrome_options)
    try:
        while True:
            driver.get(form_url); WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
            [driver.find_element(By.XPATH, f"//div[@data-value='{v}']").click() for v in ["Columbia College", "2025"]]
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))).click(); n += 1; print(f"Submitted {n} forms successfully.")
    except Exception as e: print("An error occurred:", e)
    finally: driver.quit()

n = 0
identify()
[threading.Thread(target=submit_form).start() for _ in range(20)]
[thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
print("All submissions completed.")
