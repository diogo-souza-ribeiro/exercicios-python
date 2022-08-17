'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
vamores com 10% de folga
'''
print('\t***************')
print('\tP Y T I N T A S')
print('\t***************')

metros_quadrados = float(input('Digite o tamanho em m²: '))
lata_tinta = metros_quadrados / (18 * 6) + 0.1
galao_tinta = metros_quadrados / (3.6 * 6) + 0.1
mistura_tinta = (lata_tinta + galao_tinta) + 0.1

valor_lata_tinta = 80
valor_galao_tinta = 25

cobertura = (metros_quadrados / 6) + 0.1

print('-------------------------------')
print('\nValores com 10% de folga')
print('Latas de 18L: {:.2f}'.format(lata_tinta))
print('Galões de 3,6L: {:.2f}'.format(galao_tinta))
print('Mistura de lata e de galão: {:.2f}'.format(mistura_tinta))
