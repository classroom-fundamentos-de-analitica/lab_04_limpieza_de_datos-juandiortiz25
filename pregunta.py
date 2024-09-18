"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

# python -m venv .venv
# .venv\Scripts\activate
# python.exe -m pip install --upgrade pip
# pip3 install pyarrow pandas

import pandas as pd
from datetime import datetime

def clean_date(date):
    parts = date.split('/')
    if len(parts[2]) == 4:  # Asumimos formato DD/MM/YYYY
        return pd.to_datetime(date, dayfirst=True).strftime('%Y-%m-%d')
    else:  # Asumimos formato YYYY/MM/DD
        return pd.to_datetime(date, format='%Y/%m/%d').strftime('%Y-%m-%d')

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.copy()
    
    # Eliminamos nulos
    df.dropna(axis=0, inplace=True)

    # Clean columna sexo
    df["sexo"] = df["sexo"].str.lower()
    
    # Clean columna tipo_de_emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    
    # Clean columna idea_negocio
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    
    # Clean columna barrio
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    
    # Clean columna estrato
    df["estrato"] = df["estrato"].astype(int)
    
    # Clean columna comuna_ciudadano
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    
    # Clean columna fecha_de_beneficio
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(clean_date)
    
    # Clean columna monto_del_credito
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "").str.replace("$ ", "").str.replace(".00", "").astype(int)
    
    # Clean columna línea_credito
    df["línea_credito"] = df["línea_credito"].str.lower().str.replace("-", " ").str.replace("_", " ").str.replace(". ", ".")
    
    # Eliminamos duplicados
    df.drop_duplicates(inplace=True)

    return df
