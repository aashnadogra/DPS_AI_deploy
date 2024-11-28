import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

#removing data after 2020 and formatting month col
def preprocess_data(data):
    data_until_2020 = data[data['JAHR'] <= 2020].copy()
    data_until_2020 = data_until_2020.dropna()
    data_until_2020['MONAT'] = data_until_2020['MONAT'].astype(str).str[-2:].astype(int)
    return data_until_2020
