#sorting a list of numbers

def sort_list(list_org):
    list = list_org.copy()
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:                     #for accending order
                list[i], list[j]= list[j], list[i]
            else:
                continue
    return list

l1=[9, 2, 10, 20,-5, 8,4,0]
l2=["a","g", "c", "b", "z", "ab", "ac"]
sorted_list= sort_list(l1)
l1.sort()
l2.sort()
l1_sort= sorted(l1)                 #for storing sorted value
print("original list : ", l1)
print("sorted list in accending order: ", sorted_list)
print("sorted list in decending order: ", sorted_list[::-1])
print("sorted list with sort(): ", l1)
print("sorted list with sorted(): ", l1_sort)
print("sorted list with sort(): ", l2)

