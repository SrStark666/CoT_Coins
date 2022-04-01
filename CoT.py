import requests
from time import sleep
from colorama import Fore
from os import system as limp

##Criando o menu com a cor magenta
def banner():
    print(f"""{Fore.MAGENTA}
        [1]Bitcoin
        [2]Euro
        [3]Dolár
        [4]Sair
        """)

limp("cls")
banner()
choic = 0

try:
    choice = int(input(f"{Fore.YELLOW}==> "))
    choic = choice + choic

except:
    print(f"{Fore.RED}Erro na digitação!!")

media = [] ##Lista que vai armazenar as cotações
soma = 0

try:
    while True:
        if choice == 1:
            btc_requery = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL") 
            convert_btc = btc_requery.json() ##Transformando o response em json
            btc = convert_btc["BTCBRL"]["bid"] ##Obtendo o valor do bitcoin
            btc_n = convert_btc["BTCBRL"]["code"] ##Obtendo o nome do bitcoin
            fl_convert = float(btc) ##Convertendo o valor do bitcoin em decimal
            media.append(fl_convert)  
            

            print(f"{Fore.GREEN}Nome:{btc_n}\nValor:{btc}\n")
            sleep(1)
            limp("cls")
        

        elif choice == 2:
            euro_requery = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
            convert_euro = euro_requery.json() ##Transformando o response em json
            euro = convert_euro["EURBRL"]["bid"]  ##Obtendo o valor do bitcoin
            euro_n = convert_euro["EURBRL"]["code"] ##Obtendo o nome do euro
            fl_convert = float(euro) ##Convertendo o valor do euro em decimal 
            media.append(fl_convert) ##Adicionando o valor convertido na lista media

            print(f"{Fore.GREEN}Nome:{euro_n}\nValor:{euro}\n")
            sleep(1)
            limp("cls")
            

        elif choice == 3:
            us_requery = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")  
            convert_usd = us_requery.json() ##Transformando o response em json
            dolar = convert_usd["USDBRL"]["bid"]  ##Obtendo o valor do dolar
            dolar_n = convert_usd["USDBRL"]["code"] ##Obtendo o nome do dolar
            fl_convert = float(dolar) ##Convertendo o valor do dolar em decimal 
            media.append(fl_convert) ##Adicionando o valor convertido na lista media

            print(f"{Fore.GREEN}Nome:{dolar_n}\nValor:{dolar}\n")
            sleep(1)
            limp("cls")
            

        elif choice == 4:
            break

except KeyboardInterrupt: ##Quando o usuario interromper o programa com CTR+C ele irá ignorar 
    pass                  ##e pular a linha com o pass

limp("cls")
maxvalue = max(media) ##capturando o maior valor armazenado em media
minvalue = min(media) ##capturando o menor valor armazenado em media

for i in media:
    soma += i
div = soma/len(media)

if choic == 1: ##Formatando e printando as informações 
    print(f"{Fore.GREEN}[0]Dados obtidos[0]\n") 
    print(f"{Fore.GREEN}Nome:{btc_n}\nUltimo valor registrado:{btc}\n")
    print(f"Maior cotação:{maxvalue}")
    print(f"Menor cotação: {minvalue}")
    print(f"{Fore.GREEN}A média da variação do BTC foi:{div}")

elif choic == 2:
    print(f"{Fore.GREEN}[0]Dados obtidos[0]\n")
    print(f"{Fore.GREEN}Nome:{euro_n}\nValor:{euro}\n")
    print(f"Maior cotação:{maxvalue}")
    print(f"Menor cotação: {minvalue}")
    print(f"{Fore.GREEN}A média da variação do EUR foi:{div}")


elif choic == 3:
    print(f"{Fore.GREEN}[0]Dados obtidos[0]\n")
    print(f"{Fore.GREEN}Nome:{dolar_n}\nValor:{dolar}\n")
    print(f"Maior cotação:{maxvalue}")
    print(f"Menor cotação: {minvalue}")
    print(f"{Fore.GREEN}A média da variação do USD foi:{div}")


input() ##input para caso o usuário executar pelo cmd
