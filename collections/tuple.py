tup = ()
print(tup)

print(tuple("Gokul"))

tup = (5,"Gokukl",3.5,[1,3,4])
print(tup)


a,b,c="Geeks" ,"For","Geeks"
print(a,b,c)

# * used to geab a multiple items into list.
tup = [1,2,3,4,5]
a,*b,c = tup
print(a)
print(b) # gether the elements into list.
print(c)

# reverse function()..
name ="Sarayu"
print(tuple(reversed(name)))
print(str("".join((reversed(name)))))

