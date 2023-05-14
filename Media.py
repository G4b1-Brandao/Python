nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

mediafinal = (nota1 + nota2) / 2

if mediafinal >= 7.0:
    print("A media: %.1f - Aprovado"% mediafinal)

#Adicionalmente, se existir mais de uma condição alternativa que precise ser verificada, utilizamos a condição elif, pois ela avalia as expressões intermediárias antes do comando else.

elif mediafinal == 6.0:
    print("Recuperação")
else:
    print("A media: %.1f - Reprovado"% mediafinal)