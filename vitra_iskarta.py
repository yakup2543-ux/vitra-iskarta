import streamlit as st
import requests

# Ayarlar
IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"
GEMINI_API_KEY = "AQ.Ab8RN6JsXZFLqyb6eJpFgh5gdKRYlmZT5RMDIsPhIAey-mDHww"

# 1. Başlıklar ve Girişler (Önce bunlar olmalı)
st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

uploaded_files = st.file_uploader("Fotoğrafları Seç (Max 15)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# 2. Kaydetme Butonu
if st.button("🚀 Kaydet"):
    if uploaded_files:
        st.info("Fotoğraflar yükleniyor...")
        img_links = []
        for file in uploaded_files:
            response = requests.post(f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}", files={"image": file})
            if response.status_code == 200:
                img_links.append(response.json()["data"]["url"])
        
        data = {"hat": hat, "urun": urun, "hata": hata, "neden": neden, "sonuc": sonuc, "notlar": notlar, "fotograf_linkleri": img_links}
        requests.post(WEBHOOK_URL, json=data)
        st.success("Kayıt başarılı!")
    else:
        st.warning("Lütfen fotoğraf seçin.")

# 3. Analiz Modülü (En sona)
st.divider()
st.subheader("🔍 Hata Analiz Modülü")
if st.button("Analiz Et"):
    st.write("Veriler analiz ediliyor...")
    data_response = requests.get(WEBHOOK_URL)
    
    if data_response.status_code == 200:
        gecmis_veriler = data_response.json()
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {"contents": [{"parts": [{"text": f"VitrA üretim hattı uzmanısın. Şu geçmiş verileri incele: {gecmis_veriler}. Yeni hatayı nasıl çözerim?"}]}]}
        
        ai_response = requests.post(url, json=payload)
        
        if ai_response.status_code == 200:
            cevap = ai_response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
            st.write(cevap)
        else:
            st.error(f"Hata kodu: {ai_response.status_code}")
