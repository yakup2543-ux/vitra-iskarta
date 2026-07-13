import streamlit as st
import gspread
from datetime import datetime

# 1. Private Key (r""" ile hata bitti)
MY_PRIVATE_KEY = r"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCkF3FbLhXydt3u
4HRng/vHivrpKHPdGONlzyq5ZiCtzXtVfs2V+guigF2nuhoHcnObOSTPCVWblMN1
t1O6Ls28qrnnuiwrvbd8QoF0oggrvijnyZ4hKl+rho04P8MvRVi3nE50X2OvZbIB
bTKyON/X2QLkVVcO+KBdm94XN2v5K5aqGMrXWccOmrmhl7wCrZFbUdSZlsz0uiK/
87L7rM/Hv7b7VD2PsTnNCKol94yEQ4PSM9sPH0AqzM7I0ogLAIwOjkpP/bS+9WPY
aF5FqTeA3dXnuRo6/0lc+5dN7MMDNW1+b8GRVEFg8tYqmByDPkVJM2nMSMxHLQ7U
nx4pjKBTAgMBAAECggEACJ7eqq6iIonSIQGTu/h4GsSXZ/ZjF+N91tRqZzERWHAq
IZS20kE/qTrbMLubMHb30djPsTzJTZIkLqQB9w8MafQCLkVemrGt2Q5ZZLo6eanU
1lCGSTHDsuwvsRvQckRPY94HVR/JyeYq0t5cwnYwdFOHTl2ZZET1j9VndorH1mA5
TSKZNXBm7nKwtF/PCQrGDMdwyMuHciqPwmv1Abe9i3BxwW5t+qfOVeJfOuFS/kon
nfCEM3SDApXnhLc79cSEsGGEfsQZhf8yhUYN9kBjAqyopIiEe/5wtF/zaaWjFqZ0
h+VQDvfgbqLyfFyp9bWP8xLeeNEgxcm9d5jvDrYaAQKBgQDVz/GMKSisZctFkSEn
p7C/f0Qa8HlOyjHWnlLPfhXbUdNjAWbPFtQX95UezfjQ7tsuk4x2EOjRR7DaYWIk
sX67UZR92Oohst3EIza2NCFsVj/yseFK0Oe63aycst6LXkPfdSVzL4YKGlCi0epj
bdFMTdbILSjr9/t2DA6LWSRnAQKBgQDEeAOHi1lNTjOFrm1BPS+Ytv0tQ2A+nce6
BwfpPXDwzc9j0qeoPRlvCTkrCW+vfh+yQRj/IWc/vVgGWf/XMVIL218A3Qur38xW
4WRGHy+EJ3GypJ5CU8qfdrWHUBpuWOniB6qF+k9WsHwyW1geLVQp7whZE16DOYTH
mepFEQI7UwKBgETe5FlXcKiHaYCRDPLvCvnEDrX2u7xrWL5e5SG85WFt6/86Flmi
atMFht0TT5BNQACyuk3ViIjQ5OCS+cAEBGRmFMSsuE3+hXyGMzthc1qoNZUBQyaM
P/hrKwyWeSS/SnGSFGwT5MMgUtT/dNZuKzq+3+4+za2khTUzEQRFxHoBAoGBAK5+
pSvasQr+/LWrkO/ThxWM2No9sBqNChoIKpeWcVv+f0b6jtvWwGMk/vhhXiewzjgE
p03Z/hjXc3nYr2kSLfvH794VdUtG7vbvIp9BDXPDkLEIkmL4hssQpPO0SnVdVQTi
iqCpsgdDN2NDk3iOXQNwpp/FtSZElIfAhnLeQ/rlvAoGBAKJiNUjDW5glsKpAmItL
NYadatvPZps1+j6oFWpQJed6yqeKqDK4dPXm9sw2VKev4vuwhH6b84ybb/jzeIEu
a0aQK3SMZLZhyuKSA5ZlUcvnew0IXzLu9nxvTaPtjGMz8lhBqFuKaUnzjRY0i9K/
W+phSsHhZQMME2V+Rq2RV4Gd
-----END PRIVATE KEY-----"""

# 2. Credentials
credentials = {
    "type": "service_account",
    "project_id": "vitraiskarta",
    "private_key_id": "22ab8337f6c00e2b3189410fbcf2116a677c445b",
    "private_key": MY_PRIVATE_KEY,
    "client_email": "iskarta@vitraiskarta.iam.gserviceaccount.com",
    "client_id": "104208590896291725939",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/iskarta%40vitraiskarta.iam.gserviceaccount.com"
}

# 3. Google Sheets bağlantısı
sheet = gspread.service_account_from_dict(credentials).open("VitrA_Iskarta_Tablosu").sheet1

# 4. Arayüz
st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")

hat = st.text_input("Hat")
urun = st.text_input("Ürün İsmi")
hata = st.text_input("Hata Adı")
neden = st.text_input("Muhtemel Neden")
sonuc = st.text_input("Sonuç")
notlar = st.text_area("Notlar")

if st.button("🚀 Excel'e Kaydet"):
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    sheet.append_row([tarih, hat, urun, hata, neden, sonuc, notlar])
    st.success("✅ Veri başarıyla Google Sheets'e kaydedildi!")
