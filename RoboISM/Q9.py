data = input()
arr = []
for a in range(len(data)):
    arr.append(data[a])
for a in range(len(arr)):
    arr[a] = ord(arr[a])
arr.sort()
for a in range(len(arr)):
    print(chr(arr[a]), end ="")