def worstSortEver(arr):
    n=len(arr)
    max_number = 0
    for i in range(1,n):
        if int(arr[i]) > int(max_number):
            max_number = arr[i]
    new_list = []
    for num in range(1,int(max_number)+1):
        for i in range(n):
            if num == arr[i]:
                new_list.append(num)

    print('New List', new_list)
