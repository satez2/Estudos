sp = 0
si = 0
cp = 0
ci = 0

while True:
        
    valor = int(input("Digite um numero ou [0] para sair: "))
        
    if valor == 0:
        break  
        
    if valor % 2 == 0:  
        sp += valor
        cp += 1
    else:  
        si += valor
        ci += 1

if cp > 0:
    mp = sp / cp
    print(f"Média dos números pares: {mp:.0f}")
else:
    print("Nenhum número par foi fornecido.")
    
if ci > 0:
    mi = si / ci
    print(f"Média dos números ímpares: {mi:.0f}")
else:
    print("Nenhum número ímpar foi fornecido.")
