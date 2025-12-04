import numpy as np

print("hello world")
print("Bienvendio al método simplex")

def simplex(c, A, b, maximizar = True):
    "Resuelve el problema por método simplex"
    if not maximizar:
        c = -c
        print("convirtiendo a maximización")

