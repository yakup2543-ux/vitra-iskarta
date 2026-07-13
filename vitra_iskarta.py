import streamlit as st
import requests

IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

uploaded_files = st.file_uploader("Fotoğrafları Seç (Max 15)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if st.button("🚀 Kaydet"):
    if uploaded_files:
        st.info("Fotoğraflar yükleniyor, lütfen bekleyin...")
        img_links = []
        
        for file in uploaded_files:
            response = requests.post(f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}", files={"image": file})
            if response.status_code == 200:
                img_links.append(response.json()["data"]["url"])
        
        data = {
            "hat": hat, "urun": urun, "hata": hata, "neden": neden, 
            "sonuc": sonuc, "notlar": notlar, "fotograf_linkleri": img_links
        }
        
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            st.success(f"{len(img_links)} adet fotoğraf başarıyla kaydedildi!")
        else:
            st.error("❌ Kayıt sırasında hata oluştu.")
    else:
        st.warning("Lütfen en az bir fotoğraf seçin.")
