def sum_array(arr):
    if len(arr)>0:return sum(arr)-max(arr)-min(arr)
    else: return 0

print(sum_array([1, 2, 5, 6, 7, 10]))
        