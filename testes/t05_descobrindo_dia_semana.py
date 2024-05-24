import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

dia = int(input('digite o dia denascimento '))
mes = int(input('digite o mes denascimento '))
ano = int(input('digite o ano denascimento '))

data = datetime.datetime(ano, mes, dia)
dia_semana = data.strftime('%A')
print(f'O dia da semana que você nasceu foi: {dia_semana}')
