def fibo(n):

    """
   
    >>> fibo(1)
    1
    >>> fibo(10)
    55
    """
    
    if n < 1:
        print("O num deve ser maior que zero.")
        return

    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])

    return seq[n-1]

num = int(input("Digite um num int maior que zero: "))

resultado = fibo(num)
if resultado is not None:
    print(f"O {num} termo da série de Fibo é: {resultado}")
import doctest
doctest.testmod()

