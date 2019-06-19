# 二分法查找
    函数Dichotomy传入两个参数：list和item。  
    取list数组的中间元素为mid,用int向下取整，即int(7/2)结果为3。  
    
    若mid是目标值，则打印查找轮次和元素位置    
    若mid小于目标值，则将左端点移至mid  
    若mid大于目标值，则将右端点移至mid  
    
    while循环直至查找结束或list中无目标元素，结束查找  
