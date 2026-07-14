import streamlit as st
import requests
import base64
from openai import OpenAI

# --- CHATGPT API VE WEBHOOK AYARLARI ---
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

# Senin gönderdiğin Webhook URL'si (Değişmedi, aynen duruyor)
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")

# --- CHATGPT BUTONU ---
if st.button("🤖 ChatGPT'den Çözüm İste"):
    if hat and hata:
        with st.spinner("VitrA proses verileri ChatGPT tarafından analiz ediliyor..."):
            prompt = f"Üretim hattında bir sorun var. Hat: {hat}, Ürün: {urun}, Hata: {hata}, Neden: {neden}. Bu hatanın kök nedeni nedir ve nasıl çözülebilir? Lütfen çok kısa ve net bir aksiyon planı ver."
            try:
                # ChatGPT modeline soruyu gönderiyoruz
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                cevap = response.choices[0].message.content
                st.info("💡 **ChatGPT Çözüm Önerisi:**\n\n" + cevap)
            except Exception as e:
                st.error(f"ChatGPT Sistem Hatası: {e}")
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
