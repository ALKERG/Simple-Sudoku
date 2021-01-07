from random import randint

#VARIABLES
tabla = [[0 for j in range(9)] for i in range(9)]
filas =  [0,1,2,3,4,5,6,7,8]
columnas = [0,1,2,3,4,5,6,7,8]
adicion = randint(1,9)

#FUNCTIONS  
def dibujarSudoku():
	global tabla
	for i in range(9):
		for j in range(9):
			print(tabla[i][j], end=" ")
		print("\n")

def reemplazo():
    for i in range(9):
        for j in range(9):
            nValor = tabla[i][j] + adicion
            if nValor <= 9:
                tabla[i][j] = str(tabla[i][j] + adicion)
            else:
                tabla[i][j] = str((tabla[i][j] + adicion) % 9)

#MAIN RUN
for f in filas: 
	for c in columnas: 
		tabla[f][c] = (3*(f % 3) + f // 3 + c) % 9 

print("\n")
reemplazo()
dibujarSudoku()
