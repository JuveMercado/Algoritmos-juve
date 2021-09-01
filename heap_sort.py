# Python program for implementation of heap Sort
# Programa en python para implementar el heap sort.


def heapify(arr, n, i):
	largest = i # Inicializar el indice más largo en el root
	l = 2 * i + 1	 # izquierdo = 2*i + 1
	r = 2 * i + 2	 # derecho = 2*i + 2

	# Verifica si el hijo izquierdo del root existe y es mayor que el
	if l < n and arr[largest] < arr[l]:
		largest = l

    # Verifica si el hijo derecho existe y es mayor que el root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Cambia el root de ser necesario
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] 

		heapify(arr, n, largest)



def heapSort(arr):
	n = len(arr)

	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)


# Codigo de prueba
arr = [22, 9, 17, 33, 1, 4]
heapSort(arr)
n = len(arr)
print("El array ordenado es")
for i in range(n):
	print("%d" % arr[i]),
