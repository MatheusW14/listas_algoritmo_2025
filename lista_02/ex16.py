"""Imprima todos os pares de números primos gêmeos até um limite n utilizando
exclusivamente laços de repetição. Números primos gêmeos são primos cuja diferença é
exatamente 2.
Exemplo para n = 20:
(3, 5), (5, 7), (11, 13), (17, 19)"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def twin_primes(limit):
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            print(f"({num}, {num + 2})")


n = int(input("Digite o limite n: "))
twin_primes(n)
