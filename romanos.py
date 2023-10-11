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
    
    try:
        numero = int (numero)
    except ValueError:
        return "Error: no has escrito un numero entero"

    if numero < 1 or numero > 3999:
        return "Error: el numero debe estar entre 1 y 3999"
    
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    millares = ["", "M", "MM", "MMM"]

    resultado = millares[numero // 1000] + centenas[(numero % 1000) // 100] + decenas[(numero % 100) // 10] + unidades[numero % 10]

    return resultado

print (convertir_romano("56t"))
print (convertir_romano("56"))
print (convertir_romano("-3"))
print (convertir_romano("4000"))
print (convertir_romano("3333"))