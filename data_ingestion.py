# Librerie di base
import pandas as pd
import numpy as np

def carica_e_pulisci_dati(vendite.csv: str) -> pd.DataFrame:
    """
    Carica il dataset da file CSV, rimuove valori mancanti e calcola la spesa totale.
    """
    data = pd.read_csv(vendite.csv)
    data.dropna(inplace=True)
    data['SpesaTot'] = data['Quantità'] * data['PrezzoUnitario']
    return data

def genera_dataset_sintetico(n_clienti=500) -> pd.DataFrame:
    """
    Crea un dataset realistico simulato con n_clienti record.
    """
    np.random.seed(42)
    data = pd.DataFrame({
        'ClienteID': np.arange(1, n_clienti + 1),
        'Categoria': np.random.choice(['TV', 'Notebook', 'Smartphone', 'Elettrodomestico'], n_clienti),
        'Quantità': np.random.randint(1, 6, n_clienti),
        'PrezzoUnitario': np.random.uniform(100, 1200, n_clienti)
    })
    data['SpesaTot'] = data['Quantità'] * data['PrezzoUnitario']
    data.to_csv('vendite.csv', index=False)
    return data
