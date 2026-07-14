import streamlit as st
import requests

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzsff54__0p1WaNqBrnlL_2xlcm_nQoa1l_-WdGsTE9hCgljEOZvHIv2htfz47eU-Er-Q/exec"

st.title("🏭 VitrA Iskarta Analiz Sistemi")

if st.button("🔍 Analiz Et"):
    st.write("Veri bekleniyor...")
    try:
        response = requests.post(WEBHOOK_URL, json={"action": "analiz", "veriler": "tüm geçmiş iskarta kayıtları"})
        
        # Hata ayıklama: Cevabın ham halini görelim
        st.write("Ham Cevap:")
        st.code(response.text)
        
        # Şimdi JSON olup olmadığına bakalım
        cevap_json = response.json()
        st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
        st.write(cevap_json['candidates'][0]['content']['parts'][0]['text'])
        
    except Exception as e:
        st.error(f"Hata detayı: {e}")
