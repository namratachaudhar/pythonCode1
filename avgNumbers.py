def avgNumbers(arr):
    min1 = min(arr)
    max1 = max(arr)
    
    minCount = arr.count(min1)
    maxCount = arr.count(max1)
    numb = minCount + maxCount
    sum1 = (min1 * minCount) + (max1 * maxCount)
    avg = sum1 / numb 
    print(avg)

if __name__ == '__main__':
    arr=  [1, 4, 3, 2]
    avgNumbers(arr)
