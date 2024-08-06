# Web Scraping Project

Project ini dibuat untuk belajar web scraping menggunakan bahasa Python. Pada project ini, Saya menggunakan dua library utama: Selenium dan BeautifulSoup.

## Tentang Proyek

Proyek ini bertujuan untuk melakukan web scraping pada halaman-halaman tertentu dari sebuah website dan mengumpulkan data yang relevan. Data yang dikumpulkan kemudian diekspor ke dalam file CSV.

## Fitur

- Menggunakan Selenium untuk mengotomatisasi pengambilan data dari web
- Menggunakan BeautifulSoup untuk memparsing HTML dan mengekstrak informasi yang diperlukan
- Mengekspor data yang dikumpulkan ke dalam file CSV

## Persyaratan

- Python 3.7 atau lebih baru
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/) (Pastikan sesuai dengan versi browser Chrome yang Anda gunakan)

## Instalasi

1. Clone repository ini ke lokal machine Anda:

    ```sh
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

2. Buat virtual environment dan aktifkan:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Untuk macOS/Linux
    .\venv\Scripts\activate  # Untuk Windows
    ```

3. Instal dependensi yang diperlukan:

    ```sh
    pip install selenium beautifulsoup4
    ```

4. Pastikan Anda memiliki Chrome WebDriver yang sesuai dengan versi Chrome yang Anda gunakan. Anda dapat mengunduhnya [di sini](https://sites.google.com/a/chromium.org/chromedriver/).

## Penggunaan

1. Ubah URL yang akan di-scrape di dalam skrip Python sesuai kebutuhan Anda.
2. Jalankan skrip:

    ```sh
    python scrape_services.py
    ```

3. Data yang dikumpulkan akan diekspor ke file CSV di lokasi yang ditentukan dalam skrip.

## Struktur Proyek

```plaintext
/
├── scrape_services.py       # Skrip utama untuk melakukan web scraping
├── requirements.txt         # Daftar dependensi proyek
├── README.md                # File ini
