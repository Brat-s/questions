palavra = str(input("Informe sua frase >>> "))

tam_frase = len(palavra)
frase = list(palavra)
nova_frase = ""
for i in range(tam_frase-1,-1,-1):
    nova_frase += frase[i]
print(f"\n Sua frase ao contrário será {nova_frase}")
