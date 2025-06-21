# instagram-follower-scraper
Instagram Takipçi Verileri Çekme / Instagram Follower Data Scraper

Açıklama / Description

Türkçe:
Bu proje, Playwright kütüphanesini kullanarak Instagram kullanıcılarının takipçi (followers) ve takip edilen (following) sayılarını çekmeyi sağlar. Kullanıcı adı ve şifre ile giriş yapar, hedef hesabı arar ve ilgili sayıları terminale yazar.

English:
This project leverages the Playwright library to fetch the number of followers and following counts for Instagram accounts. It logs in using credentials, searches for the target user, and prints the metrics to the console.

Özellikler / Features

Türkçe:

Instagram’a giriş (kullanıcı adı ve şifre)

Hedef kullanıcı arama

Takipçi (followers) ve takip edilen (following) sayılarını çekme

Basit ve öz terminal çıktısı

English:

Log in to Instagram (username and password)

Search for a target user

Scrape follower and following counts

Simple, concise console output

Gereksinimler / Requirements

Türkçe:

Python 3.8+

Playwright kütüphanesi

know_user.py dosyasında username ve password tanımlı

English:

Python 3.8 or higher

Playwright library installed

know_user.py file containing username and password variables

Kurulum / Installation

# Depoyu klonlayın / Clone the repository
git clone https://github.com/kullanici/proje-adi.git
cd proje-adi

# Sanal ortam oluşturun / Create a virtual environment
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Gerekli paketleri yükleyin / Install dependencies
pip install playwright
playwright install

Kullanım / Usage

# Kullanıcı adı/şifre bilgilerini ins_giriş.py içine ekleyin
# Add your username and password in ins_giriş.py

# Script'i çalıştırın / Run the script
python ins_following.py

# Terminale hedef kullanıcı adını girin / Enter the target username in the prompt
# Örnek / Example: Target User Account: erdincozcan

İpuçları / Tips

Türkçe:

Giriş sonrası çerez veya bildirim popuplarını otomatik kapatmak için ek kod ekleyebilirsiniz.

text_content() çıktısını sadece sayıya dönüştürmek için regex kullanın.

Daha ileri analizler için tüm takipçi listesini scroll ile çekip CSV’ye kaydedebilirsiniz.

English:

You can add code to auto-dismiss cookie or notification popups after login.

Use regex to parse and extract numeric values from the text_content() output.

For advanced analysis, scroll through the full follower list and save it to a CSV file.

Lisans / License

Türkçe:
Bu proje MIT lisansı altında yayınlanmıştır.

English:
This project is released under the MIT License.

