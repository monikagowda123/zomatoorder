
def quicksort(list, left, right):
    if left < right:
        partition_pos=partition(list,left,right)
        quicksort(list, left, partition_pos-1)
        quicksort(list, partition_pos+1, right)


list=[22, 11, 88, 66, 55, 77, 33, 44]
quicksort=(list, 0, len(list) -1)
print(list)