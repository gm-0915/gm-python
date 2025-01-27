text = input("文字列：")
text = str(text)

n = len(text)

if n >= 3:
    print(text[:3])

elif n < 3:
    print(text)