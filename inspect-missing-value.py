# Data yang hilang di pandas umumnya dipresentasikan dengan NaN
# Step 1 : Methode .info() dataframe untuk mengetahui info type dari dataframe tsb
# Step 2 : Mengetahui berapa banyak nilai hilang dari tiap kolom di dataset tersebut dengan menerapkan chaining method pada dataframe yaitu .isna().sum()
# Method .isna() digunakan untuk mengecek berapa data yang bernilai NaN dan .sum() menjumlahkannya secara default untuk masing-masing kolom dataframe

import pandas as pd
# Baca file "public data covid19 jhu csse eu.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/CHAPTER%204%20-%20missing%20value%20-%20public%20data%20covid19%20.csv")
# Cetak info dari df
print(df.info())
# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)