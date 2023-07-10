from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from datetime import date, timedelta,datetime
import sys
import random
import undetected_chromedriver as uc

def get_prices():
    aujourd_hui = date.today()

    with open("http_proxies.txt", 'r') as file:
        lines = file.readlines()
    my_proxy=random.choice(lines)
    print(my_proxy)

    # Calculer la date de demain
    demain = aujourd_hui + timedelta(days=1)
    cheap=10000
    delta=14
    start_date=demain+timedelta(days=45)
    end_date=start_date+timedelta(days=16)
    driver_path=r"C:\Users\Sasha\Downloads\chromedriver_win32"
    user_agent = "sasha"
    chrome_options = Options()
    
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b4) Gecko/20050908 Firefox/1.4")
    #chrome_options.add_argument(f'--proxy-server=202.86.138.18:8080')


    # Initialiser le navigateur Selenium en mode headless

    driver=webdriver.Chrome(executable_path=driver_path,options=chrome_options)
    final_date="2023-10-01"
    final_date = datetime.strptime(final_date, "%Y-%m-%d").date()

    i=0
    results={}

   
        
    driver.get("https://www.skyscanner.fr/transport/vols/cdg/cgk/?adultsv2=1&cabinclass=economy&oym=2308&iym=2309&selectedoday=01&selectediday=01")
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    print(str(start_date) + " " + str(end_date))
    try:
        button=driver.find_element(by=By.XPATH,value='//button[contains(text(),"OK")]')
        button.click()
        
    except:
        pass
    try:
        return_month=driver.find_element(By.XPATH,value='//div[@class="month-view-calendar inbound-calendar"]')
        wait = WebDriverWait(driver, 10)  # Attendre jusqu'à 10 secondes
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "date")))
        divs_with_date = return_month.find_elements(By.XPATH, './/div[contains(@class, "date")]')
        print(len(divs_with_date))
        time.sleep(20)
        
        print("ok")
    except Exception as e:
        print(e)
            
        

    driver.quit()
    return results
get_prices()
