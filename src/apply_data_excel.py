import pandas as pd
from s3_handler import get_client, put_csv_in_bucket
from io import StringIO

def apply_new_data_in_excel(df, novos_dados):
    
    print(" >> apply new data in excel...")

    df = df.append(novos_dados)
    
    io = StringIO()
    df.to_csv(io)

    client = get_client()
    put_csv_in_bucket(client, io.getvalue())

