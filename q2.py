#Programer: Bruno Teixeira Soares
#eng - Objective of the code: find if number is in febonacci sequence
#port - Objetivo do código: encontrar se número está em sequencia Febonacci

#seting values --- setando valores
num_1 = valor_procurado = 0
num_2 = 1

while True:   # main loop --- loop principal


    if valor_procurado <=0:   # if value is valid --- se valor é válido
    
        try: # geting number --- pegando número
            valor_procurado = int(input("informe um número e te direi se este pertense a sequenca de febonacci\n    >>>"))   
       
        except:    #if non numeric value inputed re-set everything --- se valor não numerico insserido resetar tudo
            print("valor impossível\n\n")
            valor_procurado = 0   
    
    if valor_procurado > 0:  # if it is valid... --- se é valido...
        print(num_1)
        if num_1 == valor_procurado:
            print("\n","- "*10,"Valor presente na sequencia Febonacci !!!\n\n")  # Printing if found --- Printar se achado
            valor_procurado = num_1 = 0
            num_2 = 1
        elif num_1 < valor_procurado:  # Procedding processing if not found --- Proceguir processando se não achado
            num_3 = num_1

            num_1 = num_2
            
            num_2 = num_1 + num_3
        else:
            print("\n","- "*10,"Valor NÃO existe em Febonacci !!!\n\n") #Print if not in febonacci --- printar se não em febonacci
            valor_procurado = num_1 = 0
            num_2 = 1
