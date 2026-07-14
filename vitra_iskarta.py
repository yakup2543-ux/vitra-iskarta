import streamlit as st
import requests
import base64
import google.generativeai as genai

# --- API VE WEBHOOK AYARLARI ---
GEMINI_API_KEY = "AQ.Ab8RN6J_xUYuM2Kj6n-PojxIyXWl7Fb25FZ4nklsoVzPxnFxoQ" 
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Senin gönderdiğin Webhook URL'si
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")

# --- YENİ EKLENEN YAPAY ZEKA BUTONU ---
if st.button("🤖 Yapay Zekadan Çözüm İste"):
    if hat and hata:
        with st.spinner("Proses verileri analiz ediliyor..."):
            prompt = f"Üretim hattında bir sorun var. Hat: {hat}, Ürün: {urun}, Hata: {hata}, Neden: {neden}. Bu hatanın kök nedeni nedir ve nasıl çözülebilir? Lütfen çok kısa ve net bir aksiyon planı ver."
            try:
                response = model.generate_content(prompt)
                st.info("💡 **Yapay Zeka Çözüm Önerisi:**\n\n" + response.text)
            except Exception as e:
                st.error("Yapay zeka ile bağlantı kurulamadı. API anahtarını doğru girdiğinden emin ol.")
    else:
        st.warning("Lütfen yapay zekaya sormadan önce en azından Hat ve Hata Adı kısımlarını doldur!")
# --------------------------------------

sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar (Yapay zeka önerisini buraya ekleyebilirsiniz)")

uploaded_files = st.file_uploader("Fotoğrafları Yükle", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

if st.button("🚀 Kaydet"):
    foto_verileri = []
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.getvalue()
            base64_foto = base64.b64encode(bytes_data).decode('utf-8')
            foto_verileri.append(base64_foto)
    
    data = {
        "hat": hat, "urun": urun, "hata": hata, 
        "neden": neden, "sonuc": sonuc, "notlar": notlar,
        "fotograflar": foto_verileri
    }
    
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 200:
        st.success("✅ Kayıt ve fotoğraflar başarıyla gönderildi!")
    else:
        st.error("Bir hata oluştu! Sistemin Google Sheets ile bağlantısını kontrol et.")
