import streamlit as st
import requests

IMGBB_API_KEY = "ba2e57de6032d83a9c332f9b493ce6f1"
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"

st.title("🏭 VitrA Çoklu Fotoğraf Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
# ... diğer alanlar aynı ...

# "accept_multiple_files" ile birden çok dosya seçebileceksin
uploaded_files = st.file_uploader("Fotoğrafları Seç (Max 15)", type=['png', 'jpg'], accept_multiple_files=True)

if st.button("🚀 Kaydet"):
    if uploaded_files:
        st.info("Fotoğraflar yükleniyor, bekleyin...")
        img_links = []
        
        for file in uploaded_files:
            response = requests.post(f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}", files={"image": file})
            if response.status_code == 200:
                img_links.append(response.json()["data"]["url"])
        
        data = {"hat": hat, "urun": urun, "fotograf_linkleri": img_links}
        requests.post(WEBHOOK_URL, json=data)
        st.success(f"{len(img_links)} adet fotoğraf başarıyla kaydedildi!")
