import string

def rangoli(size):
    n = size
    alphabets = string.ascii_lowercase
    width = 4*n - 3
    ans = []
    for i in range(n):
        left = '-'.join(alphabets[n - 1:i:-1] + alphabets[i:n])
        ans.append((left).center(width, '-'))
    print('\n'.join(ans[::-1] + ans[1:]))

size = int(input("Enter number: "))
rangoli(size)
