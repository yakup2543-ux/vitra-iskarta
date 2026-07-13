import streamlit as st
import requests

# API anahtarını koda gömdüm
IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycby64s83riiaJauxCdf1agLeKN_ow_tBz-kwzf_qAlWa1YgmNbUGlJ7-bfuC92fnVcTRbQ/exec"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

uploaded_file = st.file_uploader("Fotoğraf Yükle", type=['png', 'jpg', 'jpeg'])

if st.button("🚀 Kaydet"):
    if uploaded_file is not None:
        st.info("Fotoğraf yükleniyor...")
        
        # 1. Fotoğrafı ImgBB'ye yükle
        response = requests.post(
            f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}",
            files={"image": uploaded_file}
        )
        
        if response.status_code == 200:
            img_link = response.json()["data"]["url"]
            
            # 2. Veriyi link ile birlikte Google Sheets'e gönder
            data = {
                "hat": hat, 
                "urun": urun, 
                "hata": hata, 
                "neden": neden,
                "sonuc": sonuc,
                "notlar": notlar,
                "fotograf_linki": img_link
            }
            
            sheet_response = requests.post(WEBHOOK_URL, json=data)
            
            if sheet_response.status_code == 200:
                st.success("✅ Veri ve fotoğraf başarıyla kaydedildi!")
            else:
                st.error("❌ Excel'e kayıt hatası.")
        else:
            st.error("❌ Fotoğraf yüklenemedi.")
    else:
        st.warning("Lütfen bir fotoğraf seçin.")
