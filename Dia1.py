"""lucro = 10000
custo = 9300"""

"""faturamento = lucro - custo

if faturamento >= 5000:
    print('Bom faturamento!')
elif faturamento == 700:
    print(f'Faturamento é de {faturamento}')
else:
    print('Mal funcionamento!')

print(faturamento)"""

"""listaProdutos = ['ps5', 'notebook', 'XboxOne', 'macbook']

for i in range(10):
    print('Hello World')"""

"""contador = 0

while contador <= 10:
    print('Hello World')
    contador += 1"""


"""def hello(meu_nome, idade):
    print(f'Olá {meu_nome}, sua idade é {idade}')


hello('manoel', 25)"""


def soma(*num1, num2):
    return num1 + num2


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo numero: "))

valorsomado = soma(num1, num2)

print(valorsomado)
