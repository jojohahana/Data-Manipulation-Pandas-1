# Untuk data yang besar (big data), umumnya digunakan Google BigQuery. Layanan ini dapat digunakan jika telah memiliki Google BigQuery account.
# Fungsi .read_gbq() digunakan untuk membaca Google BigQuery table menjadi dataframe pandas.

import pandas as pd
# Query
query = """
select * 
from `bigquery-public-data.covid19_jhu_csse_eu.summary`
LIMIT 1000;
"""

# Baca data dari Google Biq Query
df_covid19_eu_summary = pd.read_gbq(query, project_id="XXXXX")
# Tampilkan data teratas
df_covid19_eu_summary.head(5)