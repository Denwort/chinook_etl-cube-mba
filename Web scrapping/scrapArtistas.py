from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_csv('artistas.csv', sep="\t")
artists = df["Name"].unique()
print(df.describe)
data = {}
list_names = []
list_listeners = []
list_scroobies = []

driver = webdriver.Chrome()
counter = 0
for a in artists:
    print(counter, "   ", a)
    counter+=1 

    driver.get('https://www.last.fm/search/artists')

    search_bar = driver.find_element(By.CLASS_NAME, 'search-field')
    search_bar.send_keys(a)

    search_btn = driver.find_element(By.CLASS_NAME, 'search-submit')
    search_btn.click()

    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "artist-results"))
    )
    res = driver.find_element(By.XPATH, '//*[@id="mantle_skin"]/div[3]/div/div[1]/ul/li[1]/div/h4/a')
    res.click()
    try:
        header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[2]/div/ul/li[1]/div/p/abbr')) 
        )
        listeners = driver.find_element(By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[2]/div/ul/li[1]/div/p/abbr').get_attribute('innerHTML')
        scroobies = driver.find_element(By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[2]/div/ul/li[2]/div/p/abbr').get_attribute('innerHTML')
    except:
        header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[1]/div/ul/li[1]/div/p/abbr')) 
        )
        listeners = driver.find_element(By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[1]/div/ul/li[1]/div/p/abbr').get_attribute('innerHTML')
        scroobies = driver.find_element(By.XPATH, '//*[@id="mantle_skin"]/header/div[1]/div[1]/div/ul/li[2]/div/p/abbr').get_attribute('innerHTML')
    list_names.append(a)
    list_listeners.append(listeners)
    list_scroobies.append(scroobies)

data = {'artist': list_names, 'listeners': list_listeners, 'scroobies': list_scroobies}
dataframe = pd.DataFrame(data)
dataframe.to_csv('artistas_web.csv', index=False, sep='|')
        

