#Faça um programa qe leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Exemplo: Digite um número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')