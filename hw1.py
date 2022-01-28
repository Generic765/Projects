#################################################
# hw1.py
#
# Nombre: Joaquin Dominguez
# DNI: 42686593
#################################################

#################################################
# Funciones que tenés que programar
#################################################

from typing import Container


def busqueda_lineal(vector, target):
    # INPUT: vector (lista[t]), target (t)
    # OUTPUT: indice (int)
    # Implementar el algoritmo de búsqueda lineal. Como entrada recibe un vector
    # que es de tipo lista[t], y un elemento target a buscar de tipo t. Como salida
    # deberá retornar el índice del vector donde se encuentre el elemento target
    # en caso de encontrarlo, o -1 en caso de no encontrar el elemento.

    leng = len(vector)
    i = 0
    n = -1
    for i in range (leng-1):
        if vector[i]==target:
            n = i
            return n
    return n



def bubble_sort(vector):
    # INPUT: vector (lista[t])
    # OUTPUT: vector (lista[t])
    # Implementar el algoritmo de burbuja (bubble sort en inglés). Como entrada
    # recibe un vecto que es de tipo lista[t], y como salida retorna el
    # vector ordenado.
    
    leng = len(vector)
    for h in range (leng):
        for i in range (leng-1):
            if (vector[i])>(vector[i+1]):
                aux = vector[i+1]
                vector[i+1] = vector[i]
                vector[i]= aux
    return vector


def busqueda_binaria_iter(vector, target):
    # INPUT: vector (lista[t]), target (t)
    # OUTPUT: indice (int), iter (int)
    # Implementar el algoritmo de búsqueda binaria modificado. Como entrada
    # recibe un vector ordenado que es de tipo lista[t], y un elemento target a
    # buscar de tipo t. Como salida deberá retornar el índice del vector donde se
    # encuentre el elemento target en caso de encontrarlo, o -1 en caso de no
    # encontrar el elemento. Además debe retornar el número de iteraciones que
    # hizo para encontrar el target.
    inicio = 0
    fin = len(vector)-1
    bandera = False
    contador = 0
    indice_buscado = -1
    i = 0
    if inicio == fin:
        if vector[inicio] == target:
            indice_buscado = inicio
    else:
        while (inicio <= fin) and (bandera == False):
            medio = (inicio+fin)//2
            if target == vector [medio]:
                bandera = True
                indice_buscado = medio
            elif target < vector[medio]:
                fin = medio-1
            else:
                inicio = medio + 1
            contador += 1
        # for n in range (len(vector)):
        #     if target == vector[n]:
        #         contador = i
        #     print (n)

    return indice_buscado, contador

#################################################
# Funciones de Test (no modificar)
#################################################


def test_busqueda_lineal():
    print("Testeando busqueda_lineal()... ", end="")
    assert busqueda_lineal([], 10) == -1
    assert busqueda_lineal(["e", "z", "e", "i", "z", "a"], "i") == 3
    assert busqueda_lineal(["e", "z", "e", "i", "z", "a"], "z") == 1
    assert busqueda_lineal([4, 1, 0], 3) == -1
    assert busqueda_lineal([4, 1, 0], 1) == 1
    print("Pasó!")


def test_bubble_sort():
    print("Testeando bubble_sort()... ", end="")
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort(["e", "z", "e", "i", "z", "a"]) == ["a", "e", "e", "i", "z", "z"]
    assert bubble_sort([4, 1, 0, 2]) == [0, 1, 2, 4]
    assert bubble_sort([-4, 1, 0]) == [-4, 0, 1]
    print("Pasó!")


def test_busqueda_binaria_iter():
    print("Testeando busqueda_binaria_iter()... ", end="")
    assert busqueda_binaria_iter([], 10) == (-1, 0)
    assert busqueda_binaria_iter([0, 1, 4], 1) == (1, 1)
    assert busqueda_binaria_iter([0, 1, 4], 4) == (2, 2)
    assert busqueda_binaria_iter([0, 1, 4], 3) == (-1, 2)
    assert busqueda_binaria_iter([0, 1, 4, 5, 7, 8, 9], 7) == (4, 3)
    print("Pasó!")


#################################################
# Main y testear todo
#################################################

# Comentá los tests que no querés correr
def testear_todo():
    test_busqueda_lineal()
    test_bubble_sort()
    test_busqueda_binaria_iter()


if __name__ == "__main__":
    testear_todo()

