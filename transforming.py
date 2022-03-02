# Mengubah dataset yang ada menjadi entitas baru .
# konversi dari satu data type ke data type yang lain, transpose dataframe, atau yang lainnya
# Yang Perlu dilakukan adalah :
# Cek data type --> [nama_dataframe].dtypes
# Merubah data bertipe object menjadi datetime --> nama_dataframe["nama_kolom"] = pd.to_datetime(nama_dataframe["nama_kolom"])

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)