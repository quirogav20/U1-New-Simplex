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

    

