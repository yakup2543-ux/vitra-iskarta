import streamlit as st
import requests

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# 15'e kadar fotoğraf girişi
st.subheader("📸 Fotoğraf Linkleri")
foto_listesi = []
for i in range(1, 16):
    link = st.text_input(f"Fotoğraf {i} Linki", key=f"foto_{i}")
    if link:
        foto_listesi.append(link)

if st.button("🚀 Kaydet"):
    data = {
        "hat": hat, "urun": urun, "hata": hata, 
        "neden": neden, "sonuc": sonuc, "notlar": notlar,
        "fotograflar": foto_listesi
    }
    requests.post(WEBHOOK_URL, json=data)
    st.success("✅ Kayıt başarılı!")
