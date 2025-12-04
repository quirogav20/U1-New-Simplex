import numpy as np

print("hello world")
print("Bienvendio al método simplex")

def simplex(c, A, b, maximizar = True):
    "Resuelve el problema por método simplex"
    if not maximizar:
        c = -c
        print("convirtiendo a maximización")

m, n = A.shape
tabla =np.zeros((m + 1, n + m + 1))   
tabla[:m, :n]= A
tabla[:m, n:n+m]= np.eye(m)
tabla[:m, -1]= b
tabla[:m, :n] = -c

print ("Tabla:")
print(tabla)

iteracion = 0
while np.any(tabla[m, :-1]< 0):
    col_pivote = np.argmin(tabla[m, :-1])
    ratios = []
    for i in range(m):
        if tabla[i, col_pivote]> 0:
            ratios.append( tabla[i, -1]/tabla[i, col_pivote])    
        else:
            ratios.append(np.inf)
    fila_pivote = np.argmin(ratios)

    pivote = tabla[fila_pivote, col_pivote]
    if pivote == 0:
        print("el problema no tiene solución")
        return None, None
        

    tabla [fila_pivote] /= pivote
    for i in range(m + 1):
        if i != fila_pivote:
            tabla[i] -= tabla[i, col_pivote] * tabla[fila_pivote]  

    iteracion += 1
    print(f"Iteración {iteracion}:")     
    print(tabla)

    solucion = np.zeros(n)
    for j in range(n):
        col = tabla[:m,j]
        if np.sum(col == 1) == 1 and np.sum(col == 0)== m -1:
            solucion[j]=tabla[np.where(col == 1)[0][0], -1]

    z = tabla[m, -1] if maximizar else -tabla[m, -1]
    print("")
    print("Solución óptima:")
    for i in range(n):
        print(f"x{i + 1} = {solucion[i]}") 
    print(f" Z {'maximo' if maximizar else 'mínimo'} = {z}")
    print("")       
    return solucion, z


