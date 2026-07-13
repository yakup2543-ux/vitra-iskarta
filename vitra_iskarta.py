import streamlit as st
import gspread
import json
from datetime import datetime

# 1. JSON dosyasını açıp sözlük (dict) olarak yüklüyoruz
with open("gcp_keys.json") as f:
    credentials = json.load(f)

# 2. KRİTİK ADIM: Private key içindeki \n yazısını alıp GERÇEK satır atlamasına çeviriyoruz.
# Bu satır hatayı %100 kesecek olan satırdır.
credentials["private_key"] = credentials["private_key"].replace("\\n", "\n")

# 3. Temizlenmiş sözlüğü gspread'e veriyoruz
sheet = gspread.service_account_from_dict(credentials).open("VitrA_Iskarta_Tablosu").sheet1

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Excel'e Kaydet"):
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    sheet.append_row([tarih, hat, urun, hata, neden, sonuc, notlar])
    st.success("✅ Veri başarıyla Google Sheets'e kaydedildi!")
