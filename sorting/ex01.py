def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        print(f"Round {i} {arr}")
        
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)

