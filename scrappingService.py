from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# URL yang akan di-scrape
url = 'https://revampweb.tlabdemo.com/services'

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Tunggu halaman dimuat
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.card-services')))

containers = driver.find_elements(By.CSS_SELECTOR, 'a.card-services')

services = []
tags = []
url_sub_services = []

for container in containers:
    # Ambil data sebelum mengklik
    service = container.find_element(By.TAG_NAME, 'p').text
    services.append(service)
    
    tag_divs = container.find_element(By.CSS_SELECTOR, 'div.card-services-body--content--tag').find_elements(By.CSS_SELECTOR, 'div.badge.badge--white.badge--small')
    
    formatted_tags = ', '.join(tag_div.text for tag_div in tag_divs)
    tags.append(f'"{formatted_tags}"')

    url_sub_service = container.get_attribute("href")
    url_sub_services.append(url_sub_service)

# Struktur untuk menyimpan data sub_services
all_sub_services = []

for url in url_sub_services:
    driver.get(url)
    sub_services = []
    try:
        # Tunggu hingga semua sub-services card muncul
        sub_service_cards = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sub-services-card'))
        )
        
        # Perulangan untuk setiap card
        for card in sub_service_cards:
            title_element = card.find_element(By.CSS_SELECTOR, 'div.sub-services-body--content--title p')
            description_element = card.find_element(By.CSS_SELECTOR, 'p.sub-services-body--content--description')
            
            title = title_element.text
            description = description_element.text
            sub_services.append(f"{title}: {description}")
    
    except Exception as e:
        print(f"Error occurred while processing {url}: {e}")
    
    # Tambahkan sub_services ke dalam list utama
    all_sub_services.append(sub_services)

driver.quit()

# Mengekspor data ke CSV
csv_file_path = 'C:/Users/LENOVO/Desktop/Latihan-python/ServiceTLAB.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Service', 'Tag', 'Sub Services'])  # Menulis header dengan tiga kolom
    for service, tag, sub_service in zip(services, tags, all_sub_services):
        formatted_sub_services = '\n'.join(sub_service)  # Menggabungkan sub-services dengan newline
        writer.writerow([service, tag, formatted_sub_services])  # Menulis setiap service, tag, dan sub_services yang digabungkan

print(f"Data telah diekspor ke {csv_file_path}")
