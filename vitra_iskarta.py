import streamlit as st
import requests

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

# Form Alanları
hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

# Verileri Sheets'e Gönderen Basit Fonksiyon
if st.button("🚀 Kaydet"):
    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbz2BVBq3px0t5fM8qjfP_HwGpkrMO9syOOv26zPH_FdkCNgjemHQTsFrcV4jrjzW06BUQ/exec"
    data = {"hat": hat, "urun": urun, "hata": hata, "neden": neden, "sonuc": sonuc, "notlar": notlar}
    requests.post(WEBHOOK_URL, json=data)
    st.success("Kayıt başarılı!")

# Hata Analiz Modülü (Yeni ve Hatasız)
st.divider()
st.subheader("🔍 Hata Analiz Modülü")
st.write("Verileri analiz etmek için aşağıdaki butona tıkla, Gemini açılacak:")

if st.button("🤖 Gemini ile Analiz Et"):
    # Google'ın ana sayfasına doğrudan yönlendirir
    st.markdown("### Yapay Zekaya Şunu Yapıştır:")
    st.code("Ben bir VitrA çalışanı olarak geçmiş iskarta verilerimi analiz ettirmek istiyorum. Sana verilerimi veriyorum, lütfen hataları incele ve çözüm önerisi sun.")
    st.link_button("Gemini'ı Aç", "https://gemini.google.com/")
