for i in range(101):
    b = i % 7
    if b == 0:
        continue
    elif '7' in str(i):
        continue
    else:
        print(i)
