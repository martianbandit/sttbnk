import streamlit as st
import pandas as pd
import numpy as np
import time

# Simuler des données en temps réel
@st.cache(allow_output_mutation=True)
def get_data():
    return []

def generate_data():
    data = get_data()
    while True:
        time.sleep(1)
        data.append({
            "timestamp": pd.Timestamp.now(),
            "value": np.random.randn()
        })
        if len(data) > 100:  # conserver seulement les 100 dernières entrées
            data.pop(0)
        yield pd.DataFrame(data)

st.title("Visualisation de données en temps réel")

# Afficher les données en temps réel
data_gen = generate_data()
chart = st.line_chart()

for data in data_gen:
    chart.add_rows(data)
    st.experimental_rerun()
