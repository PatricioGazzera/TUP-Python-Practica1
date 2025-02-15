"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
suma_de_numeros = int("123") + int("456") + int("789") + int("132")
# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
num1 = str(123)
num2 = str(456)
num3 = str(789)
suma_de_numeros_string = 'num1' + 'num2' + 'num3'
# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
multiplicacion_de_numeros = bin(0b111010110101110111101000000) * oct(0o1425) * hex(0x6f540)
# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
resultado_resta = int("987") - int("0x6f54F", 16) - int("0o1234", 8) - 654
# COMPLETAR - FIN

assert resultado_resta == -456350