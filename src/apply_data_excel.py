import pandas as pd
from constants import *
from s3_handler import get_client
from io import StringIO

def apply_new_data_in_excel(df, novos_dados):
    
    print(" >> apply new data in excel...")

    df = df.append(novos_dados)
    
    io = StringIO()
    df.to_csv(io)

    client = get_client()

    client.put_object(
        Body = io.getvalue(),  
        Bucket = AWS_BUCKET_NAME,
        Key = "Carga_horaria_result_2.csv"
    )