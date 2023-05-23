def conversao(op1,graus):
    if op1 == 1:
        print("Celsius para Fahrenheit")
        fa = (graus * 9/5) + 32
        return fa
    elif op1 == 2:
        print("Fahrenheint para Celsius")
        cel = (graus - 32) * 5/9
    else:
        return "Op invalida. digite 1 para celsiu para fahrenheit ou 2 para Fahrenheint para Celsius"

op = int(input("1 - Celsius para Fahrenheit // 2 - Fahrenheint para Celsius: "))
temp = float(input("Digite a Temperatura a sr convertida: "))

result = conversao(op, temp)
print("A conversão é: ", result)
