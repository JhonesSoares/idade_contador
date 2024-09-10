import datetime

data_atual = datetime.datetime.today().date()
#print(data_atual)

ano_atual = data_atual.year 
mes_atual = data_atual.month + 1 # INDICE JANEIRO É 0
dia_atual = data_atual.day

print()
print('Infome sua data de nascimento.')
ano_nasc = int(input('Ano: '))
mes_nasc = int(input('Mês: ')) + 1 # INDICE JANEIRO É 0
dia_nasc = int(input('Dia: '))

class IDADE:
    def __init__(self) -> None:
        pass
IDADE.anos = ano_atual - ano_nasc
IDADE.mes = mes_atual - mes_nasc
IDADE.dia = dia_atual - dia_nasc
#print(IDADE.anos)
#print(IDADE.mes)
#print(IDADE.dia)

print(f'Você tem {IDADE.anos} anos, {IDADE.mes} meses e {IDADE.dia} dias')
print()