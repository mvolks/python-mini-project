soma = 0
cont = 0
while True:
    cont += 1
    n1 = int (input (f'Fale o {cont}° número para eu fazer a média dele: '))
    soma += n1
    confirmar = int (input( 'Deseja adicionar outro número? (digite um numero negativo para parar) '))
    if confirmar < 0:
        break
media = soma / cont
print(f'a media e: {media} ')