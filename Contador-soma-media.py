ct = 0
soma = 0
maior_que_20 = 0
while True:
    valor = float(input('Digite um numero ou prescione [-0] pra sair: '))

    if valor == -0:
        break

    soma += valor
    ct +=1

    if valor > 20:
        maior_que_20 += 1

    if ct > 0:
        media = soma/ct

print(f'soma = {soma}\nmedia = {media:.2f}\nct = {ct}\n')
