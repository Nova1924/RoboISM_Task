data = input()
arr = data.split()
arr1 = []
a = 0
for b in range(10):
    arr1.append(b + 1)
arr.sort()
for b in range(11):
    if int(arr[b]) != arr1[b]:
        a = b
        break
if a != 0:
    print(arr[b] + " Is the Repeated character")
else:
    print("No character is being repeated")