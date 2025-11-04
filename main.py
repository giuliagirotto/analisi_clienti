from data_ingestion import genera_dataset_sintetico, carica_e_pulisci_dati
from clustering import segmenta_clienti
from regression import predici_spesa
from dss import assegna_strategie
from dashboard import mostra_dashboard
import streamlit as st

# 1️⃣ Genera o carica i dati
data = genera_dataset_sintetico()  # oppure carica_e_pulisci_dati('vendite.csv')

# 2️⃣ Segmenta i clienti
data, modello_cluster = segmenta_clienti(data)

# 3️⃣ Addestra modello di regressione
modello_reg = predici_spesa(data)

# 4️⃣ Assegna strategie di marketing
data = assegna_strategie(data)

# 5️⃣ Avvia dashboard interattiva
# Per lanciare: streamlit run main.py
mostra_dashboard(data)
