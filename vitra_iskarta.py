import streamlit as st
import google.generativeai as genai
import requests

# Ayarlar
IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"
GEMINI_API_KEY = "AQ.Ab8RN6LEjAkKg-iXYf4kO9N5fs0qhkDaI3ZVZhX0zTsW4NIszw"

# Yapay Zeka Kurulumu
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

# Form
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Kaydet"):
    data = {"hat": hat, "urun": urun, "hata": hata, "neden": neden, "sonuc": sonuc, "notlar": notlar}
    requests.post(WEBHOOK_URL, json=data)
    st.success("Kayıt başarılı!")

st.divider()
st.subheader("🔍 Otomatik Analiz")
if st.button("Analiz Et"):
    st.write("Veriler analiz ediliyor, lütfen bekleyin...")
    try:
        # Sheets verisini çek
        response = requests.get(WEBHOOK_URL)
        gecmis_veriler = response.text
        
        # Gemini'a sor
        prompt = f"VitrA üretim hattı uzmanısın. Şu verileri incele ve profesyonel bir çözüm önerisi sun: {gecmis_veriler}"
        response = model.generate_content(prompt)
        
        # Cevabı göster
        st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
