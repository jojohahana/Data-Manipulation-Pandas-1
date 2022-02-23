# Indexing for multi index 
# Untuk membuat hierarchical indexing dengan pandas dipelrukan kolom mana saja
# yang akan disusun, agar index dr dataframe menjadi sebuah hirarki yg dpt dikenali

# Menggunakan Fungsi .set_index() untuk set multi index dataset

import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")

# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id']) #Fungsi index adalah mengetahui berapa banyak macam index dari sebuah kolom 

# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)