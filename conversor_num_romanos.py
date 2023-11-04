number = int(input())

milesimos = int(number/1000)
sobra_milesimos = int(number%1000)

quinhentos = int(sobra_milesimos/500)
sobra_quinhentos = int(sobra_milesimos%500)

cem = int(sobra_quinhentos/100)
sobra_cem = int(sobra_quinhentos%100)

cinquenta = int(sobra_cem/50)
sobra_cinquenta = int(sobra_cem%50)

décimos = int(sobra_cinquenta/10)
sobra_décimos = int(sobra_cinquenta%10)

cincos = int(sobra_décimos/5)
sobra_cincos = int(sobra_décimos%5)

uns = int(sobra_cincos/1)

lista_numeros = []

lista_numeros.extend((milesimos, quinhentos, cem, cinquenta, décimos, cincos, uns))

if 0 < lista_numeros[0] <= 3:
    M_imp = 'M'*milesimos
    print(M_imp, end='')
 
if 0 < lista_numeros[2] <= 3 and lista_numeros[1] == 1:
    D_imp = 'D' + 'C'*lista_numeros[2]
    print(D_imp, end='')
elif lista_numeros[1] == 1 and lista_numeros[2] ==0:
    D_imp = 'D'
    print(D_imp, end='')

if 0 < lista_numeros[2] <= 3 and lista_numeros[1] == 0:
    C_imp = 'C'*cem
    print(C_imp, end='')

elif lista_numeros[2] > 3:
    if lista_numeros[1] == 0:
        C_imp = 'C'*(lista_numeros[2]-3) + 'D' 
        print(C_imp, end='')
    elif lista_numeros[1] ==1:
        C_imp = 'CM'
        print(C_imp, end='')

if 0 < lista_numeros[3] <= 3:
    if lista_numeros[3] == 1 and lista_numeros[4] == 0:
        L_imp = 'L'*cinquenta
        print(L_imp)

if 0 < lista_numeros[4] <= 3 and lista_numeros[3] == 0:
    X_imp = 'X'*décimos
    print(X_imp, end='')
elif lista_numeros[4] > 3:
    if lista_numeros[4] == 4 and lista_numeros[3] == 1:
        X_imp = 'XC'
        print(X_imp, end='')
    elif lista_numeros[4] == 4:
        X_imp = 'XL'
        print(X_imp, end='')

if 1 <= lista_numeros[4] <= 3 and lista_numeros[3] == 1:
    X_imp = 'L' + 'X'*décimos
    print(X_imp, end='')

if lista_numeros[5] == 1:
    if 0 <= lista_numeros[6] <= 3:
        V_imp = 'V' + 'I'*(lista_numeros[6])
        print(V_imp, end='')
    elif lista_numeros[5] == 1 and lista_numeros[6] == 4:
        X_imp = 'IX'
        print(X_imp, end='')
elif 1 <= lista_numeros[6] <= 3:
    I_imp = 'I'*uns
    print(I_imp, end='')
elif lista_numeros[6] > 3:
    I_imp = 'IV'
    print(I_imp, end='')


    
