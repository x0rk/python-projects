arr = [25, 80, -9, 3, 0, 74, 32, 10, 55, -96]
print("Make sure this is your array\n",arr)
sortedArray = sorted(arr)
target = int(input("Enter the target number: "))

def binarySearch(sarr, tar):
    start = 0
    end = len(sarr) - 1
    mid = int((start + end)/2)
    while True:
        if tar == sarr[mid] or len(sarr) < 2:
            print("Target is present")
            break
        elif tar < sarr[mid]:
            binarySearch(sarr[:mid], tar)
        else:
            binarySearch(sarr[mid+1:],tar)

binarySearch(sortedArray,target)