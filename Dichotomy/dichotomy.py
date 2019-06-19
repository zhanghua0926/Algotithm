def DichotomySearch(list, item):
    # 数组的两端
    left = 0
    right = len(list) - 1
    time = 0

    while left <= right:
        mid = int((left + right)/2)
        tmp = list[mid]
        time +=  1
        print('查找第' + str(time) + '次，值为：' + str(list[mid]))
        if list[mid] == item:
            print('查找次数' + str(time))
            return  mid
        elif list[mid] < item:
            left = mid + 1
        else:
            right = mid -1
    
    print('数组中没有所查找的元素')
    return None


list = [1,2,4,5,8,10,22,34,44,77,89,100,101,103,104,232,998,1009]
print('查找的元素在数组中位置' + str(DichotomySearch(list, 22)))