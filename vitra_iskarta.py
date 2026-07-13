import streamlit as st
import gspread
from datetime import datetime

# JSON dosyasını doğrudan okuyoruz
# Not: gcp_keys.json dosyasının vitra_iskarta.py ile aynı klasörde olduğundan emin ol.
sheet = gspread.service_account(filename="gcp_keys.json").open("VitrA_Iskarta_Tablosu").sheet1

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
