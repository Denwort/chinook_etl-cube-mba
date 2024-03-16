from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_csv('generos.csv', sep="\t")
genres = df["Name"].unique()
print(df.describe)
data = {}
list_genre = []
list_parent_genre = []
list_description = []
list_related_genre = []
list_popular_artist = []

driver = webdriver.Chrome()
counter = 0
for g in genres:
    print(counter, "   ", g)
    counter+=1 

    driver.get('https://www.chosic.com/list-of-music-genres/')

    search_bar = driver.find_element(By.ID, 'search-word-genral')
    search_bar.send_keys(g)

    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="form-suggestions"]/span[1]'))
    )

    res = driver.find_element(By.XPATH, '//*[@id="form-suggestions"]/span[1]')
    res.click()
    header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'suggest-song-name')) 
    )
    parent_genre = driver.find_element(By.XPATH, '//*[@id="result-p"]/div[3]/a').get_attribute('innerText')
    description = driver.find_element(By.XPATH, '//*[@id="result-p"]/p').get_attribute('innerText')
    related_genre = driver.find_element(By.XPATH, '//*[@id="result-p"]/ul/li[1]/a').get_attribute('innerText')
    popular_artist = driver.find_element(By.XPATH, '//*[@id="result-artists"]/div/div/div[1]/div/div/a').get_attribute('innerText')

    list_genre.append(g)
    list_parent_genre.append(parent_genre)
    list_description.append(description)
    list_related_genre.append(related_genre)
    list_popular_artist.append(popular_artist)

data = {'genre': list_genre, 'parent_genre': list_parent_genre, 'description': list_description, 'related_genre':list_related_genre, 'popular_artist':list_popular_artist}
dataframe = pd.DataFrame(data)
dataframe.to_csv('generos_web.csv', index=False, sep='|')
        

