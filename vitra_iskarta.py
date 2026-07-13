import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- GOOGLE SHEETS AYARLARI ---
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)
sheet = client.open("VitrA_Iskarta_Tablosu").sheet1

# --- ARAYÜZ ---
st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Excel'e (Sheets) Kaydet"):
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # Sheets'e Yaz
    sheet.append_row([tarih, hat, urun, hata, neden, sonuc, notlar])
    
    st.success("✅ Veri başarıyla Google Sheets'e kaydedildi!")
