import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from twilio.rest import Client
import json

# --- GOOGLE SHEETS AYARLARI ---
# Secret olarak JSON içeriğini buraya güvenli bir şekilde ekleyeceğiz
creds_dict = {
    "type": "service_account",
    "project_id": st.secrets["gcp_service_account"]["project_id"],
    "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
    "private_key": st.secrets["gcp_service_account"]["private_key"],
    "client_email": st.secrets["gcp_service_account"]["client_email"],
    "client_id": st.secrets["gcp_service_account"]["client_id"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
}

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("VitrA_Iskarta_Tablosu").sheet1

# --- TWILIO AYARLARI ---
TWILIO_ACCOUNT_SID = st.secrets["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = st.secrets["TWILIO_AUTH_TOKEN"]
TWILIO_WHATSAPP_NUMARASI = "whatsapp:+14155238886"
SENIN_WHATSAPP_NUMARAN = "whatsapp:+905438227318"

# --- ARAYÜZ ---
st.title("🏭 VitrA Iskarta Otomatik Kayıt & Bildirim")
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Kaydet ve WhatsApp'a Bildir"):
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # 1. Sheets'e Yaz
    sheet.append_row([tarih, hat, urun, hata, neden, sonuc, notlar])
    
    # 2. WhatsApp Bildirimi
    msg = f"🚨 *Yeni Iskarta!*\n📅 {tarih}\n🏗️ {hat}\n❌ {hata}\n✅ {sonuc}"
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    twilio_client.messages.create(body=msg, from_=TWILIO_WHATSAPP_NUMARASI, to=SENIN_WHATSAPP_NUMARAN)
    
    st.success("✅ Veri Sheets'e işlendi ve WhatsApp'a bildirildi!")
