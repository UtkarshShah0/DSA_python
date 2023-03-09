#list vs strings
a="spam"
b=list(a)
print(b)

a="spam spam spam"
b=a.split()
print(b)

a="spam1-spam2-spam3"
b=a.split("-")
print(b)

a="spam spam spam"
b=a.split()
c=("-".join(b))
print(c)
