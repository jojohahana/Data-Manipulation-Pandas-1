# Fungsi .read_excel() adalah fungsi yang digunakan untuk membaca file excel dengan esktensi file .xls atau .xlsx

import pandas as pd
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas

