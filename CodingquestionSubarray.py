def findSubArray(arr, n):
    newDict = {}
    output = []
    newSum = 0
    for i in range(n):
        newSum += arr[i]
        if newSum == 0:
            output.append((0, i))
        al = []

        if newSum in newDict:
            al = newDict.get(newSum)
            for it in range(len(al)):
                output.append((al[it] + 1, i))
        al.append(i)
        newDict[newSum] = al
    return output


if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2,2, 4, 6, -12, -7]
    n = len(arr)
    output = findSubArray(arr, n)

    if (len(output) == 0):
        print("No subarray exists")
    else:
        x = output[0][0]
        y = output[0][1]
        print(arr[x:y+1])
