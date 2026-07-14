import streamlit as st
import requests

# Apps Script URL'in
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Kayıt Sistemi")

# Form Girişleri
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# Kaydetme Fonksiyonu
if st.button("🚀 Kaydet"):
    if not hat or not urun:
        st.warning("Lütfen Hat ve Ürün İsmi alanlarını doldur.")
    else:
        data = {
            "hat": hat,
            "urun": urun,
            "hata": hata,
            "neden": neden,
            "sonuc": sonuc,
            "notlar": notlar
        }
        try:
            requests.post(WEBHOOK_URL, json=data)
            st.success("✅ Kayıt başarılı bir şekilde Sheets'e gönderildi!")
        except Exception as e:
            st.error(f"Kayıt sırasında bir hata oluştu: {e}")
