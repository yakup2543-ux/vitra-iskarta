import streamlit as st
import gspread
from datetime import datetime

# Dosyayı doğrudan kullanıyoruz
gc = gspread.service_account(filename="gcp_keys.json")
sheet = gc.open("VitrA_Iskarta_Tablosu").sheet1

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
