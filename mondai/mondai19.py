text = input("文字列：")

n = len(text)

if n >= 4:
    print(text[1:4])
    
elif n < 4:
    print("範囲外です")