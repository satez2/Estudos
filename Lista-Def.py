def main():
    lista = []

    while True:
        valor = input('Digite um valor (ou {sair} para encerrar): ')
        if valor.lower() == 'sair':
            break
        lista.append(float(valor))

    if len(lista) > 0:
        media = sum(lista) / len(lista)
        if len(lista) > 3:
            lista[3] = media
        else:
            while len(lista) <= 3:
                lista.append
            lista[3] = media 
    if len(lista) > 2:
        lista[2] = 77

    lista.sort()

    print('Lista em ordem cerescente:')
    for valor in lista:
        print(valor)

main()
