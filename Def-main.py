def main():
    soma_idade = 0 
    menores_idade = 0
    contador = 0

    while contador < 20:
        idade = int(input(f'Digite a idade da pessoa {contador + 1}: '))
        soma_idade += idade
        if idade < 18:
            menores_idade += 1
        contador += 1

    print(f'Soma das idades: {soma_idade}')
    print(f'Quantidade de pessoas menores de idade: {menores_idade}')

main()



soma = 0

menor = 0

for i in range(20):
    idade = int(input("Digita sua idade: "))
    soma += idade
    if idade < 18:
        menor += 1

print(f'No total, a soma das 20 pessoas deu {soma} anos')
print(f"{menor} pessoas tem menos de 18 anos")
