import streamlit as st
import requests

# Yeni URL'ni yerleştirdim
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycby64s83riiaJauxCdf1agLeKN_ow_tBz-kwzf_qAlWa1YgmNbUGlJ7-bfuC92fnVcTRbQ/exec"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# 15 taneye kadar fotoğraf yükleme
uploaded_files = st.file_uploader("Fotoğraf Yükle (Max 15)", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

if st.button("🚀 Excel'e Kaydet"):
    # Dosya isimlerini liste olarak alıyoruz
    foto_isimleri = [f.name for f in uploaded_files]
    
    data = {
        "hat": hat, "urun": urun, "hata": hata, "neden": neden, 
        "sonuc": sonuc, "notlar": notlar, "fotograflar": foto_isimleri
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            st.success("✅ Veri ve dosyalar başarıyla kaydedildi!")
        else:
            st.error("❌ Kayıt hatası, lütfen tekrar deneyin.")
    except Exception as e:
        st.error(f"❌ Bağlantı hatası: {e}")
