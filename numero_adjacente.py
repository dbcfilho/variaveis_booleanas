numero = int(input("Digite um número: "))
tem_sequencia_adjacente = False

while numero > 0:
    ultimo_digito = numero % 10
    numero //= 10
    if numero % 10 == ultimo_digito:
        tem_sequencia_adjacente = True

if tem_sequencia_adjacente:
    print("O número possui uma sequência adjacente de números iguais.")
else:
    print("O número não possui uma sequência adjacente de números iguais.")
