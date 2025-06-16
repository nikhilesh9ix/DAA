def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)

n = int(input())
arr = list(map(int, input().split()))
print(*merge_sort(arr))

##########################################################################################

def merge_sort(a):
    return a if len(a) < 2 else sorted(merge_sort(a[:len(a)//2]) + merge_sort(a[len(a)//2:]))

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    a = list(map(int, input("Enter the elements separated by space: ").split()))
    sorted_list = merge_sort(a)
    print("Sorted list:", *sorted_list)