
# _ _|               _)       _)  |      |              ___|                          
#   |   __ \ \ \   /  |   __|  |  __ \   |   _ \      \___ \    __|   __|  _` |  __ \ 
#   |   |   | \ \ /   | \__ \  |  |   |  |   __/            |  (     |    (   |  |   |
# __\| ||  _|  \_/   _|_)___/ _| _.__/  _| \___|      _____/  \___| _|   \__,_|  .__/ 
#  |\/ |   _ \ \ \   /  |   _ \   __|                                           _|    
#  |   |  (   | \ \ /   |   __/ \__ \                                                 
# _|  _| \___/   \_/   _| \___| ____/     
# Versão : 1.0
# Data : 27-02-2026
# Autor : Seu nome 

import datetime



headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'
}
base_url = "https://www.adorocinema.com/filmes/melhores"
filmes = []
data_hoje = datetime.date.today().strftime("%d-%m-%Y")
inicio = datetime.datetime.now()
card_temp_min = 1
card_temp_max = 3
pag_temp_min = 2
pag_temp_max = 4
paginalimite = 5
bancoDados = "filmes.db"
saidaCSV = f"filmes_adorocinema_{data_hoje}.csv"
