large = None
small = None
while True:
    try:

        num = input("Enter a number: ")
        if num == "done" : break
        n=int(num)
        if large is None or large < n:
            large = n
        elif small is None or small > n:
            small = n
    except ValueError:
        print('Invalid input')


print("Maximum is", large)
print("Minimum is", small)
