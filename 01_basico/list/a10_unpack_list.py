frutas = ['morango', 'melancia', 'banana']
frutas2 = ['morango', 'melancia', 'banana', 'kiwi', 'uva', 'abacate']
frutas3 = ['morango', 'kiwi', 'uva', 'abacate', 'melancia', 'banana']

# unpacking
vermelho, verde, amarela = frutas
print(vermelho, verde, amarela)

#  O número de variáveis ​​deve corresponder ao número de valores na lista, caso contrário, você deve usar um asterisco para coletar os valores restantes como uma lista.
vermelho2, verde2, amarela2, *nao_sei_a_cor = frutas2
print(vermelho2, verde2,amarela2, nao_sei_a_cor)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
vermelho3, *nao_sei_a_cor, verde3, amarela3  = frutas3
print(vermelho3, nao_sei_a_cor, verde3,amarela3)