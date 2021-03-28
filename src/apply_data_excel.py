import pandas as pd

def apply_new_data_in_excel(df, novos_dados):
    
    print(" >> apply new data in excel...")
    # #Adicionando os dados ao Excel
    df = df.append(novos_dados)
    
    # #Salvando o Excel
    df.to_excel("Carga_horaria_result.xlsx", index=False)