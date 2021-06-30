lst = input()
steps = 2 
lst = lst[steps:] + lst[:steps]
print(lst)