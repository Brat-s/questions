fonte = [[0,'',0],[0,'',0],[0,'',0],[0,'',0],[0,'',0]]
fonte[0][0] = 67836.43
fonte[0][1] = 'SP'

fonte[1][0] = 36678.66
fonte[1][1] = 'RJ'

fonte[2][0] = 29229.88
fonte[2][1] = "MG"

fonte[3][0] = 27165.48
fonte[3][1] = "ES"

fonte[4][0] = 19849.53
fonte[4][1] = "Outros"

soma_total = fonte[0][0]+fonte[1][0]+fonte[2][0]+fonte[3][0]+fonte[4][0]

for i in range(0,4,1):
    fonte[i][2] = (fonte[i][0]*100)/soma_total
    print(f"{fonte[i][1]} = {fonte[i][2]}%")

