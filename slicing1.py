# Slicing adalah filter ke dataframe/series berdasarkan kriteria tertentu dari nilai kolomnya ataupun kriteria index-nya.
# Methode .loc & .iloc untuk melakukan slicing
# .iloc[] akan mengakses pada index nya atau slicing pada index
# .loc[] akan mengakses berdasarkan labelnya 

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == 18055) &
		          (df["product_id"].isin(["P0029","P0040","P0041","P0116","P0117"]))]
print("Slice langsung berdasarkan kolom:\n", df_slice)