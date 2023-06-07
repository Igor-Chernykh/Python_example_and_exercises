# Old approach
x = 10
if x == 10:
    print("x is equal to 10")
else:
    print("x is not equal to 10")

# New approach
x = 10
print("x is equal to 10") if x == 10 else print("x is not equal to 10")


# Old approach: Implementing a sorting algorithm from scratch
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# New approach: Using the built-in sort function from the list class
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
arr.sort()
print(arr)


# Old approach: Using a for loop
squares = []
for x in range(1, 11):
    squares.append(x ** 2)

# New approach: Utilizing list comprehension
squares = [x ** 2 for x in range(1, 11)]


