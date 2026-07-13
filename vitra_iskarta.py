import streamlit as st
import gspread
from datetime import datetime

# Secrets'tan gelen veriyi al
creds_dict = dict(st.secrets["gcp_service_account"])

# TOML içindeki """ bloğundan gelen anahtarı kullan
sheet = gspread.service_account_from_dict(creds_dict).open("VitrA_Iskarta_Tablosu").sheet1

# ... gerisi aynı ...
