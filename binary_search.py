# Programa en Python para la busqueda binaria. 

# Regresa el índice de x en el array si el elemento está presente, sino -1
def binarySearch (arr, l, r, x):
  
    # Verifica el caso base
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # Si el elemento se encuentra presente a la mitad.
        if arr[mid] == x:
            return mid

        # Si el elemento es menor a la mitad entonces debe
        # estar en el lado izquiero del sub array 

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Sino el elemento se encuentra en el subarray derecho
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # El elemento no se encuentra en el array
        return -1
  
# Arreglo para probar el funcionamiento.
arr = [ 5, 7, 11, 26, 51 ]
x = 11
  
# Llamada a la funcion
result = binarySearch(arr, 0, len(arr)-1, x)
  
if result != -1:
    print ("El elemento está presente en el indice: % d" % result)
else:
    print ("El elemento no se encuentra en el array")