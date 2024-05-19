frutas = {'maça', 'uva', 'pera'}
frutas2 = {'banana', 'melao', 'laranja'}

# Para adicionar um item a um conjunto use o método add()
frutas.add('jaca')
print(frutas)

# Para adicionar itens de outro conjunto ao conjunto atual, use o método update()
frutas.update(frutas2)
print(frutas)
