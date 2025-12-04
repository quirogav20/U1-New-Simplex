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

def main():
    while True:
        print("--------------------------------")
        print("         Método Simplex")
        print("--------------------------------")
        print("1. MAXIMIZACIÓN")
        print("2. MINIMIZACIÓN")
        print("3. SALIR")

        option = input("Seleccione una opción (1-3): ")

        if option == '3':
            print("Saliendo del programa.")
            break

        if option not in ['1', '2']:
            print("Opción inválida. Intente de nuevo.")
            continue
        maximizar = (option == '1')
        n =int(input("Ingrese el número de variables: "))
        
        print("Ingrese los coeficientes de la función objetivo:" )
        c = np.array([float(input(f"c{i + 1}: ")) for i in range(n)])
        m = int(input("Ingrese el número de restricciones: "))
        A = []
        b = []
        tipos=[]
        print ("Ingresa cada restricción: ")
        for i in range(m):
            print(f"Restricción {i + 1}:")
            fila = [float(input(f" Coed. x{j+1}: "))for j in range (n)]
            tipo = input (" Tipo de restricción ('<=', '>=', '='): ").strip()
            while tipo not in ['<=', '>=', '=']:
                tipo = input(" Tipo inválido. Utiliza '<=', '>=', o '=': ").strip()
            lado = float (input(" Lado derecho: "))
            if tipo == '>=':
                fila = [-x for x in fila]
                lado = -lado
            A.append(fila)
            b.append(lado)
            tipos.append(tipo)
        A= np.array(A)
        b= np.array(b)
        print ("--------------------------------")
        print(f"{'MAXIMIZAR' if maximizar else 'MINIMIZAR'}: Z = {' + '.join([f'{c[i]:.1f}x{i+1}' for i in range(n)])}")
        print("Sujeto a:")
        for i in range(m):
            if tipos[i] == '>=':
                coefs = [-A[i,j] for j in range(n)]
                print(f"  {' + '.join([f'{coefs[j]:.1f}x{j+1}' for j in range(n)])} >= {-b[i]:.1f}")
            else:
                print(f"  {' + '.join([f'{A[i,j]:.1f}x{j+1}' for j in range(n)])} {tipos[i]} {b[i]:.1f}")
        print(f"  {', '.join([f'x{i+1}' for i in range(n)])} >= 0")
        
        resultado = simplex(c, A, b, maximizar)
        if resultado[0] is None:
            print("No se pudo resolver el problema.")

           

