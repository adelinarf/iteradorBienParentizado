#El iterador recursive se encarga de agregar nuevas expresiones bien parentizadas a una lista de  
#expresiones bien parentizadas, se visita de manera recursiva para recorrer toda la lista
#Una vez culmine toda la lista, se devuelve la lista aux que contiene todas las expresiones bien
#parentizadas para el numero de iteraciones en el que se ha llamado a esta funcion 
def recursive(lista, n, aux):
    if n>=0 and list(lista)!=[]:
        aux.append("("+list(lista)[n]+")")
        aux.append("()"+list(lista)[n])
        aux.append(list(lista)[n]+"()")
        for i in recursive(lista,n-1,aux):
            yield i
    else:
        yield list(set(aux))
#El iterador bienParentizadas itera sobre si mismo n veces y contiene el caso base de las expresiones 
#parentizadas. Llama a la funcion recursive en cada llamada de esta funcion y de manera recursiva construye
#las expresiones correctamente parentizadas.
def bienParentizadas(n):
    if n>1:
        for x in bienParentizadas(n-1):
            tamano = len(list(x))
            for y in recursive(x,tamano-1,[]):
                yield y
    else:
        yield ["()"]
#La funcion bienParentizada consigue los valores de una expresion bien parentizada con n parentesis
def bienParentizada(n):
    for c in bienParentizadas(n):
    	print(list(c))
#La funcion main permite ingresar un numero desde la consola y se le calculara sus expresiones bien 
#parentizadas. Si se desea salir del programa se inserta -1.
def main():
    inicia = True
    while inicia:
        get = int(input("Inserte un numero: "))
        if get == -1:
            inicia = False
        else:
            bienParentizada(get)
main()
