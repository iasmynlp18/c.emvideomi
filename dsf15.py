n1 = float(input('Quantos quilometros foram percorridos pelo carro alugado? '))
n2 = int(input('Por quantos dias esse carro foi alugado? '))

kmr = (n1 * 0.15)
dia = (n2 * 60)
tot = dia+kmr
print(f'O total a pagar pelo carro alugado foi de R${tot:.2f}. ')