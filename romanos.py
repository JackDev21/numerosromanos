# Convertir numeros romanos a numeros entre 0 y 3999 (incluidos)

"""
I - Uno
V - Cinco
X - Diez
C - Cien
D - Quinientos
M - Mil

El numero 0 devuelve una cadena vacía

"""

def convertir_romano(numero):

    if not isinstance (numero, str):
        return "Error: no has escrito un numero entero"

    if numero < 1 or numero > 3999:
        return "Error: el numero debe estar entre 1 y 3999"
    
    return "Todo: Convertir"

print (convertir_romano("56t"))
print (convertir_romano("56"))
print (convertir_romano("-3"))
print (convertir_romano("4000"))
print (convertir_romano("3333"))