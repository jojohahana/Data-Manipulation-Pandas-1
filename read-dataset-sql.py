# Example case jika membaca query dari sql untuk ditranslate menjadi pandas frame
# Fungsi yang digunakan adalah .read_sql() dan .read_sql_query()

import mysql.connector
import pandas as pd
# Membuat koneksi ke database financial di https://relational.fit.cvut.cz/dataset/Financial
my_conn = mysql.connector.connect(host="relational.fit.cvut.cz",
                                port=3306,
                                user="guest",
                                passwd="relational",
                                database="financial",
                                use_pure=True)
# Query untuk membaca tabel Loan
my_query = """
select * from loan;
"""

# Fungsi .read_sql_query
# Pakai .read_sql_query utk membaca table
df_loan = pd.read_sql_query(my_query, my_conn) #bisa juga menggunakan fungsi .read_sql
# 5 data teratas
df_loan.head(5)