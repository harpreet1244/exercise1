x = float(input("x: "))
y = float(input("y: "))

z = round(x+y,1)
print(f"${z:,}")
#this function will round up the number after decimal by 1 like(2.4)
name = input("what is your name? ")

##remove the whitespaces from str
name = name.strip()

name = name.title()

##say hello user
print(f"hello, {name}")   

#or 
name = input("what is your name? ").strip().title()

##remove the whitespaces from str

##say hello user
print(f"hello, {name}") 
