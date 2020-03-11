for i in range(101):
	#对7取余，余数为0则表示是7的倍数
    b = i % 7
    if b == 0:
        continue
	#验证是否带有7
    elif '7' in str(i):
        continue
    else:
        print(i)
