# df.head(5) || Fungsi .head(n) untuk membatasi tampilan jumlah baris teratas dari dataset
# df.tail(3) || Fungsi .tail(n) untuk membatasi tampilan jumlah baris terbawah dari dataset

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan 3 data teratas
print("Tiga data teratas:\n", df.head(3))
# Tampilkan 3 data terbawah
print("Tiga data terbawah:\n", df.tail(3))