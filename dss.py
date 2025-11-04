//Decision Support System
import numpy as np

def suggerisci_strategia(row, media_spesa, media_freq):
    """
    Regole di inferenza per assegnare una strategia di marketing a ciascun cliente.
    """
    S = row['SpesaTot']
    F = row['Quantità']

    if S > 1.2 * media_spesa and F > media_freq:
        return "Fidelizzazione Premium"
    elif S < media_spesa and F > media_freq:
        return "Promozione Mirata"
    elif S < media_spesa and F < media_freq:
        return "Acquisizione"
    else:
        return "Mantenimento"

def assegna_strategie(data):
    """
    Calcola le strategie per ogni cliente in base alla spesa media e frequenza media.
    """
    media_spesa = data['SpesaTot'].mean()
    media_freq = data['Quantità'].mean()
    data['Strategia'] = data.apply(lambda r: suggerisci_strategia(r, media_spesa, media_freq), axis=1)
    return data
