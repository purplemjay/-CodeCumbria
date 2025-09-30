def square_lists(numbers):   # ( ) → defines parameter
    result = []              # [ ] → empty list
    for n in numbers:
        result.append(n * n) # ( ) → call append
    return result

print(square_lists([1, 2, 3])) # ( ) to call function, [ ] to pass a list
