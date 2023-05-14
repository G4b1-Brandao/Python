A = input("Informe um valor: ")
C = input("Informe um segundo valor: ")

if(A>C):
    aux = A;
    A=C;
    C=aux;

print("O valor da variável A agora é: ", A)
print("O valor da variável C agora é: ", C)

