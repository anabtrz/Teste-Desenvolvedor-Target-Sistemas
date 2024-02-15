#pede o numero com input e armazena em n para ser usado como limite para a sequência de Fibonacci
fibonacci = int(input("Informe um número: "))

#inicia variaveis com valores 0 e 1 para calculo da sequência
x, y = 0, 1

#inicia loop enquanto x for menor que o numero definido em fibonacci
while x < fibonacci:
    # x passa a valer y e y passa a valer x + y(fibonacci)
    x, y = y, x + y

#imprime resultado
if (x == fibonacci):
    print('Faz parte da sequência de Fibonacci')
else :
    print('Não faz parte da sequência de Fibonacci')