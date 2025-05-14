#Task 3

import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless') #enables headless mode (doesn't automatically open up webpage)
options.add_argument('--disable-gpu') #optional, recommended for Windows
options.add_argument('--window-size=1920x1080') #optional, sets the window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),options=options))

try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart") #go to this webpage to start scraping

    main_div = driver.find_element(By.CSS_SELECTOR,'main[id="content"]')
    if main_div:
        search_result_items = main_div.find_elements(By.CLASS_NAME, "cp-search-result-item") #search for li elements 
        if len(search_result_items) > 0:
            print(f"Found {len(search_result_items)} list items with the class 'cp-search-result-item'") #print number of li elements found on page
            
            results = [] #create empty list
            for item in search_result_items: #loop through list of li items
                title = item.find_element(By.CSS_SELECTOR, 'span[class="title-content"]') #find title
                print("title: ", title.text) #print title

                author_list = item.find_elements(By.CSS_SELECTOR, 'a[class="author-link"]') #find author info
                print(f"This book has {len(author_list)} authors.") #check number of authors
                if len(author_list) == 1: #if only one author, print author name
                    author = author_list[0].text
                    print("author: ", author) 
                elif len(author_list) > 1: #if more than one author, join their names together with a ";"
                    list = []
                    for author in author_list:
                        list.append(author.text)
                    sep = ";"
                    author = sep.join(list)
                    print("author: ", author) 
                else: #if no authors, print no authors found
                    print("No authors found.")
                
                format_year_div = item.find_element(By.CSS_SELECTOR, 'div[class="cp-format-info"]') #find div with book type and year
                format_year = format_year_div.find_element(By.CSS_SELECTOR, 'span[class="display-info-primary"]') #search span tag within the div
                format_year_text = format_year.text
                if format_year_text.__contains__("|"): #remove language if included
                    index = format_year_text.find(" |")
                    print(f"this book includes a language starting at index no {index}")
                    format_year = format_year_text[0:index]
                    print("format_year: ", format_year)
                else:
                    format_year = format_year_text
                    print("format_year: ", format_year) #print format and year

                #create new dictionary for each item, then add it to the results list
                result = {
                    'title': title.text,
                    'author': author,
                    'format_year': format_year
                }
                results.append(result)

            print("results dictionary: ", results) #print list of dictionaries of key value pairs

except Exception as e:
    print("Couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()

#put results into a data frame
sp_learning_books = pd.DataFrame(results)
print("sp_learning_books: \n", sp_learning_books)


#Task 4
sp_learning_books.to_csv("get_books.csv", sep=',', index=True, header=True)
sp_learning_books.to_json("get_books.json")
                