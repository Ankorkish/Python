text=open("test.txt")
l = [line.strip().split() for line in text]
print(l)  
text.close()
