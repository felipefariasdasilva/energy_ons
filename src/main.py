from s3_handler import get_file
from energy_crawler import request_data
from parse_data import select_required_data
from apply_data_excel import apply_new_data_in_excel

def main(event= None, context= None):
    
    print(" >> iniciando serviço de crawler...")

    df = get_file()
    json = request_data()
    dados = select_required_data(json)
    apply_new_data_in_excel(df, dados)


if __name__=='__main__':
    main()