import streamlit as st
import requests

# YENİ URL GÜNCELLENDİ
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Kaydet"):
    data = {"action": "kayit", "hat": hat, "urun": urun, "hata": hata, "neden": neden, "sonuc": sonuc, "notlar": notlar, "fotograf_linkleri": ""}
    requests.post(WEBHOOK_URL, json=data)
    st.success("Kayıt başarılı!")

st.divider()
if st.button("🔍 Analiz Et"):
    st.write("Yapay zeka analiz ediyor, lütfen bekle...")
    try:
        response = requests.post(WEBHOOK_URL, json={"action": "analiz", "veriler": "tüm geçmiş iskarta kayıtları"})
        if response.status_code == 200:
            # Buradaki JSON yapısı Google'dan gelen cevaba göre ayarlandı
            cevap = response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
            st.write(cevap)
        else:
            st.error(f"Sunucu hatası: {response.status_code}")
    except Exception as e:
        st.error(f"Bağlantı hatası: {e}")
