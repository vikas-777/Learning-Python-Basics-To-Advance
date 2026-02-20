# def second_largest_number(arr):
#     n = len(arr)
#     arr.sort()
#     for i in range(n-2,-1,-1):
#         if arr[i] != arr[n-1]:
#             return arr[i]
#     return -1
# if __name__=="__main__":
#     arr = [1,2,3,4,5,6,7,8,9]
#     print(second_largest_number(arr))
# def second_largest_number(arr):
#     n = len(arr)
#     arr.sort()
#     for i in range(n-2,-1,-1):
#         if arr[i] != arr[n-1]:
#             return arr[i]
#     return -1
# if __name__ == "__main__":
#     arr = [1,2,3,4,5,6,7,8]
#     print(f"{second_largest_number(arr)} Thala for a reason")
def second_largest_number(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1
    for i in range(n):
        if arr[i] >= largest:
            largest = arr[i]
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 10]
    print(second_largest_number(arr), "Thala for a reason")
