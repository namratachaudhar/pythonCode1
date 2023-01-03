def sendMail(arr):
    dict = {}
    for x in arr:
        m = x.split('@')
        if m[1] in dict:
            dict[m[1]].append(x)
        else:
            dict[m[1]] = [x]
    myKeys = list(dict.keys())
    myKeys.sort()
    sorted_dict = {i: dict[i] for i in myKeys}
    
    for i in sorted_dict.values():
        print(sorted(i))

if __name__ == '__main__':
    arr = ['ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com','jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com']
    sendMail(arr)
