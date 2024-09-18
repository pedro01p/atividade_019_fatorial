# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
n=int(input("adicione um numero inteiro"))
f=1
while n > 1:
    f*=n
    n-=1
print(F"seu fatorial é {f}")