import streamlit as st
import requests
import google.generativeai as genai

# Ayarları yap
IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

# Giriş alanları
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

uploaded_files = st.file_uploader("Fotoğrafları Seç (Max 15)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# 1. Kayıt Butonu
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

# 2. Analiz Butonu
st.divider()
st.subheader("🔍 Hata Analiz Modülü")
if st.button("Analiz Et"):
    st.write("Veriler analiz ediliyor...")
    data_response = requests.get(WEBHOOK_URL)
    if data_response.status_code == 200:
        gecmis_veriler = data_response.json()
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Elimizdeki geçmiş iskarta kayıtları şunlar: {gecmis_veriler}. Yeni bir hata analizi yapmam gerekiyor. Bu verilere göre nasıl bir öneride bulunursun?"
        response = model.generate_content(prompt)
        st.write("### 🤖 Yapay Zeka Analizi:")
        st.write(response.text)
