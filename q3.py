import xml.etree.ElementTree as xee
tree = xee.parse("dados (2).xml")
root = tree.getroot()
maior = divizor = soma = 0
menor = 100000
pior_dia = melhor_dia = ""
print(root.tag)
for x in root.findall('row'):
    dia = x.find('dia').text
    valor = x.find('valor').text
    if not valor.find('0',0):
        print("OwO")
    else:
        print(dia,valor)
        numero = float(valor)
        if numero>maior:
            maior = numero
            melhor_dia = dia
        if numero<menor:
            menor = numero
            pior_dia = dia
        divizor += 1
        soma += numero
media = soma/divizor
 
print(f"O maior valor foi R${maior} no dia {melhor_dia}\n já o menor valor foi R${menor} do dia {pior_dia}\n Com uma média de R${media}")
