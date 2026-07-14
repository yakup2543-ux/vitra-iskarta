# Analiz Modülü (Hata ayıklayıcı versiyon)
st.divider()
st.subheader("🔍 Hata Analiz Modülü")
if st.button("Analiz Et"):
    st.write("Veriler analiz ediliyor...")
    
    # 1. Sheets verilerini çek
    data_response = requests.get(WEBHOOK_URL)
    if data_response.status_code != 200:
        st.error(f"Sheets verisi alınamadı! Hata kodu: {data_response.status_code}")
    else:
        gecmis_veriler = data_response.json()
        st.write("Veriler başarıyla alındı, Gemini'a gönderiliyor...")
        
        # 2. Gemini bağlantısı
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {"contents": [{"parts": [{"text": f"VitrA üretim hattı uzmanısın. Şu geçmiş iskarta verilerini incele: {gecmis_veriler}. Bu veriler ışığında bir öneride bulun."}]}]}
        
        ai_response = requests.post(url, json=payload)
        
        if ai_response.status_code == 200:
            cevap = ai_response.json()['candidates'][0]['content']['parts'][0]['text']
            st.write("### 🤖 Yapay Zeka Uzmanı Cevabı:")
            st.write(cevap)
        else:
            # Hatanın gerçek nedenini ekrana yazdır
            st.error(f"Gemini bağlantı hatası! Kod: {ai_response.status_code}")
            st.write(f"Detay: {ai_response.text}")
