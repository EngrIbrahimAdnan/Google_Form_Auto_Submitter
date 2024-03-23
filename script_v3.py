# Import necessary libraries
import requests, threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Define the URL of the Google Form
form_url = "..."

# Function to identify and print the questions in the form
def identify():
    try:
        # Fetch the HTML content of the form
        soup = BeautifulSoup(requests.get(form_url).content, "html.parser")
        # Extract and print each question along with its type
        [print(f"Question {i}: {q.find('div', {'role': 'heading'}).get_text(strip=True)} ({'Multiple Choice' if q.find('div', {'role': 'radio'}) else 'Short Answer' if q.find('input', {'type': 'text'}) else 'Paragraph'})") for i, q in enumerate(soup.find_all('div', {'role': 'listitem'}), 1)]
    except Exception as e:
        # Print an error message if any exception occurs
        print("An error occurred while identifying question nature:", e)

# Function to submit the form
def submit_form():
    global n
    # Initialize a Chrome webdriver instance
    driver = webdriver.Chrome(options=chrome_options)
    try:
        while True:
            # Open the form URL
            driver.get(form_url)
            # Wait for the first input field to be visible
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[1]")))
            # Fill in the first input field with a sample name
            driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Jacklyn Hudson")
            # Select options for the second and third questions
            [driver.find_element(By.XPATH, f"//div[@data-value='{v}']").click() for v in ["Columbia College", "2025"]]
            # Click the submit button
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))).click()
            # Increment submission count and print success message
            n += 1
            print(f"Submitted {n} forms successfully.")
    except Exception as e:
        # Print an error message if any exception occurs
        print("An error occurred:", e)
    finally:
        # Quit the webdriver instance
        driver.quit()

# Initialize submission count
n = 0
# Identify questions in the form
identify()
# Start form submission threads
[threading.Thread(target=submit_form).start() for _ in range(20)]
# Wait for all threads to complete
[thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
# Print completion message
print("All submissions completed.")
