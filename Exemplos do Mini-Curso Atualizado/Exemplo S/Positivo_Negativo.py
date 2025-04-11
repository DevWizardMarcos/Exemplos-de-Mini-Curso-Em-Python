numero = int(input('Digite um numero : '))
if numero > 0 and numero % 2 == 0: 
    print('Esse número é positivo e par.')
elif numero == 0:
    print('Número neutro.')
else:
    print('Esse número não atende aos critérios (maior que zero e par).')