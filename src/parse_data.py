#Importando as bibliotecas necessárias
import pandas as pd
import time
from datetime import datetime

def select_required_data(json):
    
    print(" >> select required data...")

    # # Selecionando os dados desejados
    tempo_ons = json['Data']
    norte_verificada =json['norte']['cargaVerificada']
    nordeste_verificada =json['nordeste']['cargaVerificada']
    sudeste_verificada =json['sudesteECentroOeste']['cargaVerificada']
    sul_verificada =json['sul']['cargaVerificada']
    data_hora = datetime.now()
    
    # # Montando o DataFrame que adicionará os dados ao Excel
    novos_dados = []
    novos_dados = get_columns()
    
    # #Submercado Norte
    norte = get_serie(data_hora, tempo_ons, 'N', norte_verificada)
    lista = pd.DataFrame( [norte] )
    novos_dados = add_data_in_list(lista, novos_dados)

    # #Submercado Nordeste
    nordeste = get_serie(data_hora, tempo_ons, 'NE', nordeste_verificada)
    lista = pd.DataFrame( [nordeste] )
    novos_dados = add_data_in_list(lista, novos_dados)

    # #Submercado Sudeste/Centro-Oeste
    sudeste = get_serie(data_hora, tempo_ons, 'SE', sudeste_verificada)
    lista = pd.DataFrame( [sudeste] )
    novos_dados = add_data_in_list(lista, novos_dados)

    # #Submercado Sul
    sul = get_serie(data_hora, tempo_ons,'S',sul_verificada)
    lista = pd.DataFrame( [sul] )
    novos_dados = add_data_in_list(lista, novos_dados)

    return novos_dados

def get_columns():
    return pd.DataFrame(
        columns =
            [
                'Última Atualização', 
                'Submercado', 
                'Carga_Verificada',
                'Dia',
                'Mês',
                'Ano',
                'Hora',
                'Minuto'
            ]
    )

def get_serie(data_hora, tempo_ons, region, region_verified):
    
    return pd.Series(
        [
            tempo_ons,
            region,
            region_verified,
            data_hora.strftime('%d'),
            data_hora.strftime('%m'),
            data_hora.strftime('%Y'),
            data_hora.strftime('%H'),
            data_hora.strftime('%M')
        ]
    )

def add_data_in_list(lista, novos_dados):

    lista.columns = [
            'Última Atualização', 
            'Submercado', 
            'Carga_Verificada',
            'Dia',
            'Mês',
            'Ano',
            'Hora',
            'Minuto'
        ]

    return novos_dados.append(lista)