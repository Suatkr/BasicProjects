def bubble_sort(array):
    for i in range(1,len(array)):
        for a in range(len(array)-i):
            if array[a]>array[a+1]:
                b=array[a]
                array[a]=array[a+1]
                array[a+1]=b

    return array

sayilar=[5,6,9,41,88,25,3,65,26,17,8]
print("{}".format(bubble_sort(sayilar)))