import wget
import zipfile
from datetime import datetime
from os import remove
import urllib.error
import pandas as pd

def download_and_extract(year, month):
    date = f'{year}{month:02d}'
    zipname = f'inf_diario_fi_{date}.zip'
    url = f'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{zipname}'
    
    try:
        print(f"Attempting to download: {zipname}")
        wget.download(url, zipname)
        
        with zipfile.ZipFile(zipname, 'r') as zip_ref:
            zip_ref.extractall('data')
        zip_ref.close()
        
        remove(zipname)
        print(f"\nDownload and extraction completed for {zipname}")
        
        return date
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"\n{zipname} not found, trying the previous month.")
            previous_month = (month - 1) if month > 1 else 12
            previous_year = year if month > 1 else year - 1
            
            if previous_month != month:
                return download_and_extract(previous_year, previous_month)
            else:
                print("No valid data available for download.")
                return None
        else:
            print(f"HTTP error occurred: {e}")
            return None

current_year = datetime.now().year
current_month = datetime.now().month

date = download_and_extract(current_year, current_month)

if date:
    cnpj_list = [
    "41.610.610/0001-94", "26.218.447/0001-25", "09.342.159/0001-69", "09.136.668/0001-35",
    "09.342.159/0001-69", "09.136.662/0001-35", "09.136.668/0001-35", "17.971.054/0001-05",
    "47.611.958/0001-82", "32.319.996/0001-99", "45.615.749/0001-81", "38.068.926/0001-91",
    "35.939.857/0001-56", "43.779.069/0001-78", "47.032.813/0001-27", "33.755.733/0001-95",
    "44.409.327/0001-97", "34.462.068/0001-04", "36.327.214/0001-14", "48.349.305/0001-30",
    "28.993.760/0001-66", "44.025.282/0001-57", "14.196.835/0001-73", "03.804.917/0001-37",
    "33.755.733/0001-95"
    ]

    def scrape_all_fis(cnpj_list, date):
        df = pd.read_csv(f'data/inf_diario_fi_{date}.csv', sep=';')

        df = df.rename(columns={
            'DT_COMPTC': 'Data da Informação',
            'VL_TOTAL': 'Total da Carteira',
            'VL_QUOTA': 'Quota',
            'VL_PATRIM_LIQ': 'Patrimônio Líquido',
            'CAPTC_DIA': 'Captação no Dia',
            'RESG_DIA': 'Resgate no Dia',
            'NR_COTST': 'N total de Cotistas',
            'CNPJ_FUNDO': 'CNPJ'
        })

        df = df.drop(columns=['TP_FUNDO'])

        filtered_df = df[df['CNPJ'].isin(cnpj_list)]

        latest_entries_df = filtered_df.sort_values(by='Data da Informação').groupby('CNPJ').tail(1)

        latest_entries_df.set_index('CNPJ', inplace=True)

        pd.options.display.float_format = '{:,.2f}'.format

        return latest_entries_df
    
    final_df = scrape_all_fis(cnpj_list, date)
else:
    print("Data download failed, unable to proceed with scraping.")

final_df.to_excel('data/resultado_fundos.xlsx', index=True)