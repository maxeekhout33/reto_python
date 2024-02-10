# Bienvenido a Reto Python por Código Facilito

:small_blue_diamond: Día 1: Tipo de Datos <br>
&emsp;(str, int, float, bool) <br>
&emsp;Operadores relacionales (==, !=, >, >=, <, <=) <br>
&emsp;Operadores lógicos (and, or, not) <br>
<br>
:small_blue_diamond: Día 2: Estructuras de control <br>
&emsp;if - else (elif) <br>
&emsp;match (switch en otros lenguajes de programación) <br>
&emsp;foreach (cuando sepamos cuantas iteraciones se necesitan) <br>
&emsp;while (cuando no sepamos cuantas iteraciones se necesitan) <br>
<br>
:small_blue_diamond: Día 3: Listas <br>
&emsp;Métodos: <br>
&emsp; - list.append(elemento) # Agrego el nuevo elemento al final de la lista <br>
&emsp; - list.insert(index, elemento) # Inserto el nuevo elemento en el indice especifico y se desplazan los demas elementos <br>
&emsp; - list.extend(new_list) # Agrego todos los elementos de una nueva lista al final de mi lista original <br>
&emsp; - list.remove(elemeto) # Elimina de la lista el elemento <br>
&emsp; - list.count(elemento) # Cuenta cuantas veces existe el elemento en la lista <br>
&emsp; - list.index(elemento) # Devuelve el indice donde se encuentra el elemento en la lista <br>
&emsp; - list.clear() # Limpia la lista y la devuelve vacia <br>
&emsp; - elemento in list # Usando la palabra reservada in podemos saber si el elemento existe o no en la lista <br>
&emsp; - etc <br>
<br>
&emsp; La funcion enumerate devuelve el indice y su valor y funciona tanto para listas como strings: <br>

```
for index, course in enumerate(courses):
    print('El valor para el indice', index, 'es', course)

for index, character in enumerate('Hola mundo'):
    print(index, character)
```

<br>
:small_blue_diamond: Día 4: Tuplas y diccionarios <br>
&emsp; Las tuplas son inmutables (str, int, bool, etc)
&emsp; Los diccionarios son mutables {'key':'value'} la llave = objetos inmutables (str, int, float, bool, tuplas)
