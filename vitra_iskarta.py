import streamlit as st
import requests

# Ayarlar
IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"
GEMINI_API_KEY = "AQ.Ab8RN6LEjAkKg-iXYf4kO9N5fs0qhkDaI3ZVZhX0zTsW4NIszw"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

# Form Alanları
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# Kayıt Butonu
if st.button("🚀 Kaydet"):
    data = {"hat": hat, "urun": urun, "hata": hata, "neden": neden, "sonuc": sonuc, "notlar": notlar}
    requests.post(WEBHOOK_URL, json=data)
    st.success("Kayıt başarılı!")

# Analiz Modülü
st.divider()
st.subheader("🔍 Otomatik Analiz")
if st.button("Analiz Et"):
    st.write("Veriler analiz ediliyor, lütfen bekleyin...")
    
    # 1. Sheets'ten verileri al
    try:
        data_response = requests.get(WEBHOOK_URL)
        gecmis_veriler = data_response.text
        
        # 2. Doğrudan API'ye bağlan
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"VitrA uzmanı olarak şu geçmiş iskarta verilerini incele ve çözüm önerisi sun: {gecmis_veriler}"}]
            }]
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            sonuc = response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
            st.write(sonuc)
        else:
            st.error(f"Bağlantı Hatası: {response.status_code}")
            st.write(response.text) # Hatanın detayını görmek için
    except Exception as e:
        st.error(f"Hata: {e}")
