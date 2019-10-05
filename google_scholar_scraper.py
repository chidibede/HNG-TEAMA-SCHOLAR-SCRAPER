''' A Python Web Scraper'''

# Import the neccessary modules needed
import time
from selenium import webdriver
import pandas as pd

''' Scrape the first 20 pages (pages 1 - 20)'''

# Create a dataframe to store the names of the professors and their h-indices
COMPUTER_PROFESSORS = pd.DataFrame(columns=['Name', 'H-Index'])

# Set the browser to be used (We will be using Mozilla Firefox)
FIREFOX = webdriver.Firefox(executable_path='.\\Drivers\\geckodriver.exe')

# Set the url of website to search and set the search phrase
SEARCH_PHRASE = "Computer Science Professors"
URL = 'https://scholar.google.com/citations?view_op=search_authors&mauthors={}&hl=en&oi=drw'.format(SEARCH_PHRASE)

# set a timeout and load page
FIREFOX.set_page_load_timeout(20)
FIREFOX.get(URL)

# Number of pages to search
PAGES = range(1, 20)

# Click on each link and extract data
for page in PAGES:
    for i in range(1, 11):
        i = str(i)
        try:
            FIREFOX.find_element_by_css_selector('#gsc_sa_ccl > div:nth-child({}) > div > div > h3 > a'.format(i)).click()
            time.sleep(10)
            h_index = FIREFOX.find_element_by_css_selector('#gsc_rsb_st > tbody > tr:nth-child(2)')
            name = FIREFOX.find_element_by_css_selector('#gsc_prf_in')
            COMPUTER_PROFESSORS = COMPUTER_PROFESSORS.append({'Name': name.text, 'H-Index':h_index.text.split()[1]}, ignore_index=True)
            print(name.text)
            time.sleep(10)
            FIREFOX.back()
            time.sleep(10)
        # This will handle the 500 server error and try to restablish contact
        # Where this fails, we take the current url for the next script
        except:
            FIREFOX.implicitly_wait(5)
            CURRENT_URL = FIREFOX.current_url
            # This will be used in the next script incase of 500 server error
            print(CURRENT_URL)
            FIREFOX.get(CURRENT_URL)

    # Export the dataframe to csv file, the last csv is the accumulated csv
    COMPUTER_PROFESSORS.to_csv("Computer_Professors{}.csv".format(str(page)), index=False)
    FIREFOX.implicitly_wait(10)

     # click on the next page
    FIREFOX.find_element_by_css_selector('#gsc_authors_bottom_pag > div > button.gs_btnPR.gs_in_ib.gs_btn_half.gs_btn_lsb.gs_btn_srt.gsc_pgn_pnx').click()
    time.sleep(10)

# Sleep and close the browser
time.sleep(20)
NEXT_URL = FIREFOX.current_url
print(NEXT_URL) # This is incase of 500 server error
FIREFOX.quit()

''' Scrape the last 5 pages '''
# Create a dataframe to store the names of the professors and their h-indices
COMPUTER_PROFESSORS = pd.DataFrame(columns=['Name', 'H-Index'])

# Set the browser to be used (We will be using Mozilla Firefox)
FIREFOX = webdriver.Firefox(executable_path='.\\Drivers\\geckodriver.exe')

# Set the url to the url of the last page scraped
NEXT_URL = 'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=Computer+Science+Professors&after_author=NyIDAO1-__8J&astart=190'

# set a timeout
FIREFOX.set_page_load_timeout(20)
FIREFOX.get(NEXT_URL)

# Number of pages to search
PAGES = range(20, 26)

# Click on each link and extract data
for page in PAGES:
    for i in range(1, 11):
        i = str(i)
        try:
            FIREFOX.find_element_by_css_selector('#gsc_sa_ccl > div:nth-child({}) > div > div > h3 > a'.format(i)).click()
            time.sleep(10)
            h_index = FIREFOX.find_element_by_css_selector('#gsc_rsb_st > tbody > tr:nth-child(2)')
            name = FIREFOX.find_element_by_css_selector('#gsc_prf_in')
            COMPUTER_PROFESSORS = COMPUTER_PROFESSORS.append({'Name': name.text, 'H-Index':h_index.text.split()[1]}, ignore_index=True)
            print(name.text)
            time.sleep(10)
            FIREFOX.back()
            time.sleep(10)
        except:
            pass

    # Export the dataframe to csv file, the last csv is the accumulated csv
    COMPUTER_PROFESSORS.to_csv("Computer_Professors{}.csv".format(str(page)), index=False)
    FIREFOX.implicitly_wait(10)

    # click on the next page
    FIREFOX.find_element_by_css_selector('#gsc_authors_bottom_pag > div > button.gs_btnPR.gs_in_ib.gs_btn_half.gs_btn_lsb.gs_btn_srt.gsc_pgn_pnx').click()
    time.sleep(10)

# Sleep and close the browser
time.sleep(20)
FIREFOX.quit()
