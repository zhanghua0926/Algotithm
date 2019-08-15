def quickSort(r,low,high):
    #  取最左边的数为基准数
    if(low<high):
        # 以i,j指向数组的头尾两边，tmp保存当前基准数，即当前轮次要归位的数
        i = low
        j = high
        tmp = r[i]

        while(i<j):
            # 当数组尾部元素大于基准数时，将j向前移动
            while(i<j and r[j]>=tmp):
                j-=1
            
            # 若数组尾部元素小于tmp，则将其赋值给r[i]
            r[i] = r[j]

            # 若数组头部元素小于等于tmp，将i向后移动
            while(i<j and r[i]<=tmp):
                i+=1
            
            r[j] = r[i]

        # 基准数归位，此时索引i,j相等
        a[i] = tmp

        # 递归操作，继续对a[i]的左右两个区间进行排序
        quickSort(r,low,i-1)
        quickSort(r,i+1,high)

if __name__ == "__main__":
    a = [3,6,5,9,7,1,8,2,4]
    quickSort(a,0,len(a)-1)
    print(a)
