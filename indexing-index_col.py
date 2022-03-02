# Menggunakan function index_col untuk menentukan kolom menjadi index
# dan kolom dataframe akan berkurang karena salah satu kolom menjadi index


# Membuat Order Date & Order Id menjadi index column
import pandas as pd
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", index_col=["order_date", "order_id"]) #kolom order_date & order_id
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))