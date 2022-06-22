num_1 = valor_procurado = 0
num_2 = 1
while True:
    if valor_procurado <=0:
        try:
            valor_procurado = int(input("informe um número e te direi se este pertense a sequenca de febonacci\n    >>>"))   
        except:
            print("valor impossível\n\n")
            valor_procurado = 0
            
    if valor_procurado > 0:
        print(num_1)
        if num_1 == valor_procurado:
            print("\n","- "*10,"Valor presente na sequencia Febonacci !!!\n\n")
            valor_procurado = num_1 = 0
            num_2 = 1
        elif num_1 < valor_procurado:
            num_3 = num_1

            num_1 = num_2
            
            num_2 = num_1 + num_3
        else:
            print("\n","- "*10,"Valor NÃO existe em Febonacci !!!\n\n")
            valor_procurado = num_1 = 0
            num_2 = 1
