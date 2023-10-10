def insertMinHeap(heap, index):
    inserted_element = heap[index]
    parent_index = (index - 1) // 2
    while index > 0 and inserted_element < heap[parent_index]:
        heap[index] = heap[parent_index]
        index = parent_index
        parent_index = (index - 1) // 2
    heap[index] = inserted_element


def deleteMin(heap, last):
    inserted_element = heap[last]
    heap[last] = heap[0]
    print(f"deleteMin = {heap[0]} FindPlaceFor {inserted_element}")
    hole = 0
    left_child = hole * 2 + 1
    found = False
    while left_child < last and not found:
        right_child = left_child if left_child + 1 >= last else left_child + 1
        min_child = left_child if heap[left_child] < heap[right_child] else right_child
        if heap[min_child] < inserted_element:
            heap[hole] = heap[min_child]
            hole = min_child
            left_child = hole * 2 + 1
        else:
            found = True
    heap[hole] = inserted_element
    print(*heap)


heap_list = []
user_input = input("Enter list of number: ").split(",")
for i in range(len(user_input)):
    heap_list.append(int(user_input[i]))
    insertMinHeap(heap_list, i)

print("Heap: ", end="")
print(*heap_list)
print("==== heap sort ====")
for last_index in range(len(heap_list) - 1, 0, -1):
    deleteMin(heap_list, last_index)
print("==== Sorting a ====")
heap_list.reverse()
print(*heap_list)