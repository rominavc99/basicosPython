#Esto es un comentario 
print("Hello World")
print("Goodbye World")

#operadores arimeticos
5+1
print(4+6)
print(3*4)
print(1-3)
print(3/1)
#precedencia de operadores
print(5+8*3+2)
print(5+8*(3+2))

#valores y tipos
print(type(2))
print(type(2.5))
print(type("hola"))

#variables
mensaje = "esto es un mensaje"
print(mensaje)
mensaje = "mensaje modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

#las variables no pueden iniciar con numeros ni incluir caracteres especiales que esten reservados para otras cosas
#se pueden utilizar mayusculas y minusculas

mis3animales = "gato, perro, lobo"
print(mis3animales)

tresAnimales = "gato, perro, lobo"
print(tresAnimales)

#concatenacion de strings
textouno = "hola"
textodos = "como estas"

print(textouno + textodos)

edad = "20"
print("la edad del usuario es: " + edad)

#para cambiar tipos de datos str() int() float()
edad = 20
print("la edad del usuario: " + str(edad))
print(type(edad))

print("el tipo de dato es: " + str(type(edad)))

#librerias
import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(grados)
print("el seno de 45 grados es: " + str(seno))



#funciones
def saludar(nombre):
    print("hola " + nombre)
    print("como estas")
def despedir():
    print("adios")

def concatenar(parte1, parte2, parte3):
    return parte1 + parte2+ parte3


print("esto no es parte de la funcion")

saludar("chayanne")
despedir()

frase = concatenar("Hola", "como estas", "adios")
print(frase)
