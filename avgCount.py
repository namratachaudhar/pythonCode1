def findCount(arr):
    l = len(arr)
    sum1 = 0
    for x in arr:
        sum1 += x
    avg = sum1//l
    print(arr.count(avg))

if __name__ == '__main__':
    arr = [ 1,3,2,4,5]  
    findCount(arr)
