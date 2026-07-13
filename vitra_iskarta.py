import streamlit as st
import requests

# URL'ni koda ekledim
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxMtneYbmVe89daXIx2JC6hVbiVpnCbC1gyyXxJsfCmrVylK1UsrkRzjRSLqNM_0U1y8g/exec"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Excel'e Kaydet"):
    data = {
        "hat": hat, 
        "urun": urun, 
        "hata": hata, 
        "neden": neden, 
        "sonuc": sonuc, 
        "notlar": notlar
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            st.success("✅ Veri başarıyla kaydedildi!")
        else:
            st.error(f"❌ Hata kodu: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Bağlantı hatası: {e}")
