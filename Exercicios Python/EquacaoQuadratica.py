'''Calcular valores definidos pelo usuário utilizando a fórmula de bhaskara'''

print('\t # B H A S K A R A #\n')
print('Os valores para a fórmula de bhaskara, são definidos como:')
print('"a" sendo o valor de nX²')
print('"b" sendo o valor de nX')
print('"c" sendo o valor de n')
print('Ex: ax² + bx + c = 0\n')
#Receber valores de ax², bx e C
recebe_a = int(input('Digite o valor de ax²: '))
recebe_b = int(input('Digite o valor de bx: '))
recebe_c = int(input('Digite o valor de c: '))
#Calculo de Delta
delta = (recebe_b * recebe_b) - 4 * recebe_a * recebe_c 
#Imprimir valor de Delta Δ
print('\nDefinindo o valor de Delta (Δ = b² - 4.a.c)')
print('Valor de Δ: ', delta)
raiz_delta = delta ** (1/2)#Calcular raiz de delta
#Calculando o valor de x' e x''
x_uma_linha = (-recebe_b + raiz_delta) / (2 * recebe_a)
x_duas_linhas = (-recebe_b - raiz_delta) / (2 * recebe_a)
#Imprimir valores de x' e x''
print('\nCalculando o valor de (x = -b +- √Δ / 2.a)')
print('Valor de -{}+-√{} / 2.{}: '.format(recebe_b, delta, recebe_a))
print('x\' = ', x_uma_linha)
print('x\'\' = ', x_duas_linhas)