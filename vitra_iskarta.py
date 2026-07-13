import streamlit as st
from datetime import datetime
from twilio.rest import Client

# Sayfa Ayarları
st.set_page_config(page_title="Iskarta WhatsApp Sistemi", layout="centered")

st.title("🏭 VitrA Iskarta Mobil Bildirim Sistemi")

# Twilio Bilgileri (Streamlit Secrets'tan çekecek)
TWILIO_ACCOUNT_SID = st.secrets["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = st.secrets["TWILIO_AUTH_TOKEN"]
TWILIO_WHATSAPP_NUMARASI = "whatsapp:+14155238886"
SENIN_WHATSAPP_NUMARAN = "whatsapp:+905438227318" 

# Veri Giriş Alanları
tarih = st.text_input("Tarih", datetime.now().strftime("%d.%m.%Y %H:%M"))
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

st.info("Not: Girilen veriler anında yetkili WhatsApp hattına raporlanacaktır.")

# Gönderim Butonu
if st.button("🚨 Iskarta Raporunu WhatsApp ile Gönder"):
    if not hat or not hata:
        st.error("Hat ve Hata Adı boş bırakılamaz!")
    else:
        try:
            mesaj_icerigi = (
                f"🚨 *YENİ ISKARTA BİLDİRİMİ* 🚨\n\n"
                f"📅 *Tarih:* {tarih}\n"
                f"🏗️ *Hat:* {hat}\n"
                f"📦 *Ürün:* {urun}\n"
                f"❌ *Hata Adı:* {hata}\n"
                f"🔍 *Muhtemel Neden:* {neden}\n"
                f"✅ *Sonuç:* {sonuc}\n"
                f"📝 *Notlar:* {notlar}"
            )
            
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            
            message = client.messages.create(
                body=mesaj_icerigi,
                from_=TWILIO_WHATSAPP_NUMARASI,
                to=SENIN_WHATSAPP_NUMARAN
            )
            
            st.success("✅ Iskarta verisi başarıyla WhatsApp üzerinden iletildi!")
            st.balloons()
            
        except Exception as e:
            st.error(f"Mesaj gönderilirken hata oluştu: {e}")
