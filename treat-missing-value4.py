# Handle missing value 
# 3. Mengisi missing value dengan nilai lain, yang dapat berupa : nilai statistik seperti mean atau median
# MENGGANTI MISSING VALUE DENGAN MEAN / MEDIAN 

import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/CHAPTER%204%20-%20missing%20value%20-%20public%20data%20covid19%20.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/CHAPTER%204%20-%20missing%20value%20-%20public%20data%20covid19%20.csv")
# Cetak nilai mean dan median awal 
print("Awal: mean = %f, median = %f." % (df["active"].mean(), df["active"].median()))
# Isi missing value kolom active dengan median
df_median = df["active"].fillna(df["active"].median())
# Cetak nilai mean dan median awal setelah diisi dengan median
print("Fillna median: mean = %f, median = %f." % (df_median.mean(), df_median.median()))
# Isi missing value kolom active dengan mean
df_mean = df["active"].fillna(df["active"].mean())
# Cetak nilai mean dan median awal setelah diisi dengan mean
print("Fillna mean: mean = %f, median = %f." % (df_mean.mean(), df_mean.median()))