import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["order_date"] == "2019-01-01") &
		          (df["product_id"].isin(["P2154","P2556"]))]
print("Slice langsung berdasarkan kolom:\n", df_slice)
# Result akan filter berdasarkan order_date & product_id