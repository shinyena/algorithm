n = input()
a = n.split("0")
b = n.split("1")
print(min(len(a)-a.count(''), len(b)-b.count('')))