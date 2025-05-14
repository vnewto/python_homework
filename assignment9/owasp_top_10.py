import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless') #enables headless mode
options.add_argument('--disable-gpu') #optional, recommended for Windows
options.add_argument('--window-size=1920x1080') #optional, sets the window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),options=options))

try:
    #connect to the web page
    driver.get("https://owasp.org/www-project-top-ten/")

    #find div with id "main"
    main_section = driver.find_element(By.CSS_SELECTOR, 'section[id="sec-main"]')
    
    #declare empty list
    top_10_list = []

    if main_section:
        #find list items in second ul of main section
        list_items = main_section.find_elements(By.XPATH, './/ul[2]/li')
        #iterate over list items
        for item in list_items:
            #find title
            title = item.find_element(By.CSS_SELECTOR, 'a')
            print("title: ", title.text)
            #find link
            link = title.get_attribute("href")
            print("link: ", link)
            #if both arre found, add to top_10_list
            if title and link:
                top_10_list.append({"title": title.text, "link": link})

    print("top_10_list: ", top_10_list)

except Exception as e:
    print("Couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally: 
    driver.quit()

#create data frame
owasp_top_10 = pd.DataFrame(top_10_list)

#write to csv file
owasp_top_10.to_csv("owasp_top_10.csv", sep=',', header=True, index=True)