a = [int(i) for i in input().split()]
b = [str(i) for i in a if not(int(i))]
print(' '.join(str(i) for i in a if int(i)), ' '.join(b))
