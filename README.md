# Iterador para expresiones bien parentizadas
### Pregunta 3.b
Se desea que construya un iterador bienParentizadas que reciba un número n y genere todas las expresiones bien parentizadas que se pueden formar con n paréntesis de cada tipo. 
Este programa cuenta con dos iteradores: bienParentizadas y recursive. El iterador recursive se encarga de iterar sobre expresiones bien parentizadas y generar nuevas expresiones con un paréntesis más que las expresiones originalmente incluidas. El iterador bienParentizadas itera n veces, siendo n el número de paréntesis que se desean obtener en cada expresión. Luego llama a la función recursive y utiliza de manera recursiva los valores de esta para construir expresiones bien parentizadas con n paréntesis.
El iterador recursive se aprovecha del hecho que si f es una expresión bien parentizada, entonces f(), ()f y (f) también lo son y de esta manera genera todas las posibilidades para cada uno de los elementos de la lista de expresiones bien parentizadas que se introducen como argumentos.

## ¿Cómo correr el programa?
El programa puede correrse en sitios web como: https://www.online-python.com/
Al correr el programa se pide un número, se debe colocar el valor y dar enter y se producirán todas las posibilidades para la cantidad n de paréntesis introducida. 

Se sale del programa al introducir el valor -1.
