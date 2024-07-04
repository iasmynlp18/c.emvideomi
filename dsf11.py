n1 = float(input('Qual é a altura da parede? '))
n2 = float(input('Qual é a largura da parede? '))

area = (n2*n1)
qtinta = (area/2)
print(f'Sua parede tem a dimensão de {n1} x {n2} e sua área é de {area}m2.')
print(f'A quantidade necessária para pintar toda a parede é de {qtinta:.1f} litros de tinta.')