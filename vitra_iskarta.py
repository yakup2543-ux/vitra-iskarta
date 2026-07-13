import streamlit as st
import gspread
import json
from datetime import datetime

# Secrets'tan tüm bilgiyi dict olarak al
creds_dict = st.secrets["gcp_service_account"]

# private_key içindeki \n karakterlerini düzelt (bu satır hatayı kesin çözecek)
creds_dict['private_key'] = creds_dict['private_key'].replace('\\n', '\n')

# Bağlan
sheet = gspread.service_account_from_dict(creds_dict).open("VitrA_Iskarta_Tablosu").sheet1

st.title("🏭 VitrA Iskarta Otomatik Kayıt Sistemi")
# ... (geri kalan kod aynı kalacak) ...
