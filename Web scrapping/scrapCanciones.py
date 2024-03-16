from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_csv('canciones.csv', sep="\t")
tracks = df["Name"].unique()[:3]
print(df.describe)
data = {}
list_tracks = []
list_key = []
list_camelot = []
list_explicit = []
list_popularity = []
list_happiness = []
list_danceability = []
list_energy = []
list_acousticness = []
list_instrumentalness = []
list_liveness = []
list_speechiness = []

driver = webdriver.Chrome()
counter = 0
for t in tracks:
    print(counter, "   ", t)
    counter+=1 

    driver.get('https://www.chosic.com/music-genre-finder')

    search_bar = driver.find_element(By.ID, 'search-word')
    search_bar.send_keys(t)

    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="form-suggestions"]/span[1]'))
    )

    res = driver.find_element(By.XPATH, '//*[@id="form-suggestions"]/span[1]')
    res.click()
    one = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[1]/div[2]/span[1]')) 
    )
    key = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[1]/div[2]/span[1]').get_attribute('innerText').split(':')[1].strip()
    camelot = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[1]/div[2]/span[2]').get_attribute('innerText').split(':')[1].strip()
    explicit = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[1]/div[2]/span[3]').get_attribute('innerText').split(':')[1].strip()
    two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/div')) 
    )

    progress_divs = driver.find_elements(By.CLASS_NAME, "progressbars-div")

    # Iterar sobre cada div para extraer la información
    for progress_div in progress_divs:
        # Obtener el texto del div
        div_text = progress_div.text
        
        # Dividir el texto en líneas
        lines = div_text.split('\n')
        
        # Iterar sobre cada línea para encontrar los valores de popularidad, danceability, etc.
        for line in lines:
            if "Popularity:" in line:
                popularity = line.split(':')[1].strip().split('/')[0]
            elif "Happiness:" in line:
                happiness = line.split(':')[1].strip().split('/')[0]
            elif "Danceability:" in line:
                danceability = line.split(':')[1].strip().split('/')[0]
            elif "Energy:" in line:
                energy = line.split(':')[1].strip().split('/')[0]
            elif "Acousticness:" in line:
                acousticness = line.split(':')[1].strip().split('/')[0]
            elif "Instrumentalness:" in line:
                instrumentalness = line.split(':')[1].strip().split('/')[0]
            elif "Liveness:" in line:
                liveness = line.split(':')[1].strip().split('/')[0]
            elif "Speechiness:" in line:
                speechiness = line.split(':')[1].strip().split('/')[0]

    '''
    popularity = driver.find_element(By.CLASS_NAME, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]')..get_attribute('innerText') 
    happiness = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[2]').get_attribute('innerText') 
    danceability = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[3]').get_attribute('innerText') 
    energy = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[4]').get_attribute('innerText') 
    acousticness = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[5]').get_attribute('innerText') 
    instrumentalness = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[6]').get_attribute('innerText') 
    liveness = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[7]').get_attribute('innerText') 
    speechiness = driver.find_element(By.XPATH, '//*[@id="result-analyzer"]/div[1]/div[2]/div[2]/text()[8]').get_attribute('innerText') 
    '''

    list_tracks.append(t)
    list_key.append(key)
    list_camelot.append(camelot)
    list_explicit.append(explicit)
    list_popularity.append(popularity)
    list_happiness.append(happiness)
    list_danceability.append(danceability)
    list_energy.append(energy)
    list_acousticness.append(acousticness)
    list_instrumentalness.append(instrumentalness)
    list_liveness.append(liveness)
    list_speechiness.append(speechiness)


data = {'tracks': list_tracks, 'key': list_key, 'camelot': list_camelot, 'explicit':list_explicit, 'popularity':list_popularity,
        'happiness':list_happiness, 'danceability':list_danceability, 'energy':list_energy, 'acousticness':list_acousticness, 
        'instrumentalness':list_instrumentalness, 'liveness':list_liveness, 'speechiness':list_speechiness}
dataframe = pd.DataFrame(data)
dataframe.to_csv('canciones_web.csv', index=False, sep='|')
        

