from time import sleep

def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    if passo == 0:
        passo = 1

    if inicio < fim:
        for i in range(inicio, fim + 1, abs(passo)):
            print(i, end=' ', flush=True)
            sleep(0.3)
    else:
        for i in range(inicio, fim - 1, -abs(passo)):
            print(i, end=' ', flush=True)
            sleep(0.3)

    print('\nFim da contagem!')
    print('-' * 30)

contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
