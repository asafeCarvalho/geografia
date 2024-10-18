print("hello\n")

# -*- coding: utf-8 -*-
# from google.colab import files
# uploaded = files.upload()

import io
import pandas as pd

# Substitua 'esta.csv' pelo nome do arquivo carregado, se necessário.
# /content/drive/MyDrive/Python/2244028_Chuvas.csv
data = pd.read_csv("/home/convidado/Documentos/extraidos-limpos/2041046_Chuvas.csv", sep=';')  # Assuming ';' is the delimiter

# Print the column names to verify
print(data.columns)

data['Data'] = pd.to_datetime(data['Data'], dayfirst=True, errors='coerce')

for indice, linha in data.iterrows() :
  print(indice, data['Data'].dt.month)
  print("fim\n\n")



# Convert the 'Data' column to datetime format (adjust column name if needed)
# If the column name is different, replace 'Data' with the actual name


# Filter data for the month of January and calculate the mean number of rainy days
# january_data = data[data['Data'].dt.month == 11]
# mean_rainy_days_january = january_data['NumDiasDeChuva'].mean()