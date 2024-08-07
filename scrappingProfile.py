from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# URL yang akan di-scrape
url = 'https://revampweb.tlabdemo.com/about'

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Tunggu halaman dimuat
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.container-app')))
soup = BeautifulSoup(driver.page_source, 'html.parser')
get_vision = soup.select_one('p.box-vision__content')
vision = get_vision.get_text(strip=True)
get_mission = soup.select('div.list-mission')

mission_info_list = []
for mission in get_mission:
    info_elements = mission.select('div.list-mission__info')
    for info in info_elements:
            mission_info_list.append(info.get_text(strip=True))

get_brand_dna = soup.select('div.brand-dna-slide')
brand_dna = []
for slide in get_brand_dna:
    title_bna = slide.select_one('div.brand-dna-slide--text h6')
    description_bna = slide.select_one('div.brand-dna-slide--text p')
        
    if title_bna and description_bna:
        title_text = title_bna.get_text(strip=True)
        description_text = description_bna.get_text(strip=True)
        brand_dna.append(f"{title_text}: {description_text}")

get_core_value = soup.select('div.card-core-value')
core_value = []
for slide_core in get_core_value:
    title_core = slide_core.select_one('span.badge.badge--neutral')
    description_core = slide_core.select_one('div.card-core-value__body')
    if title_core and description_core:
        title_text = title_core.get_text(strip=True)
        description_text = description_core.get_text(strip=True)
        core_value.append(f"{title_text}: {description_text}")

csv_file_path = 'C:/Users/LENOVO/Desktop/Latihan-python/ProfileTLAB.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
        # Menulis header
    writer.writerow(['Vision', 'Mission', 'Brand DNA', 'Core Value'])
        
        # Menggabungkan item dengan \n dan menambahkan tanda kutip
    vision_text = f"\"{vision}\""
    mission_text = "\n".join([f"\"{item}\"" for item in mission_info_list])
    brand_dna_text = "\n".join([f"\"{item}\"" for item in brand_dna])
    core_value_text = "\n".join([f"\"{item}\"" for item in core_value])
        
        # Menulis baris data
    writer.writerow([vision_text, mission_text, brand_dna_text, core_value_text])
    
print(f"Data telah diekspor ke {csv_file_path}")
