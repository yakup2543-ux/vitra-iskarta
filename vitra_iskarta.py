import streamlit as st
import requests
import base64

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# Dünkü fotoğraf yükleme sistemi
uploaded_files = st.file_uploader("Fotoğrafları Yükle", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

if st.button("🚀 Kaydet"):
    foto_verileri = []
    for uploaded_file in uploaded_files:
        # Dosyayı base64'e çevirip gönderiyoruz
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
        st.error("Bir hata oluştu!")
