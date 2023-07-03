def happy(first):
    wordlist = first.split()
    print(wordlist)
    

    return wordlist[0][0] == wordlist[1][0]



print(happy("lee line"))

def check_sum(a,b):
    if a + b == 20:
         return True
    elif a == 20 or b == 20:
         return True
    else:
         return False
    

print(check_sum(10,4))

def mac(name):
    first = name[0]
    inbetween = name[1:3]
    four = name[3]
    rest = name[4:]


    return first.upper() + inbetween + four.upper() + rest


print(mac('macDonal'))

def reverse(text):
    word = text.split()
    reversed = word[::-1]

    return " ".join(reversed)


print(reverse("i am good"))


def it_33(num):
     for i in range(0,len(num)-1):
         if num[i] == 3 and num[i+1] == 3:
             return True
     return False



print(it_33([1,2,3,3]))

def char(text):
    
    result = " "

    for chr in text:
         result += chr*3 
    return result 
        
        
    

    
print(char("hello"))


def sum_total(a,b,c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:

        return sum([a,b,c]) - 10 
    
    else :
        return "burst"


print(sum_total(11,11,11))


        

def spy_game(*nums):
    code = [0,0,7,"x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
       


print(spy_game(1,2,0,0,7))


def count_prime(*nums):

    count = 0
    

    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
        

        
    

# print(count_prime(0,1,2,3,4,5,6,7,8,9,10))

def count_prime(nums):

    count = 0
    if nums < 2 :
        return 0
    
    prime = [2]

    x = 3
    while x <= nums:
        ##check if x is prime
        for y in prime :
            if x % y == 0:
                x += 2
                break

        else:
            prime.append (x)
            x += 2 

    print(prime)
    return len(prime)


print(count_prime(10))


for y in range(3,10,2):
    print(y)


### MAP FUNCTION: - ######

def divide(num):
    return num % 2

my_list = [2,5,9,11]

for i in map(divide,my_list):
    print(i)

 ##filter function will only apply on true value of object#####
####like in this it will give only even number result#
def check_even(num):
    return num % 2 == 0


my_list = [1,2,3,4,5,6,7,8,9]
for n in filter(check_even,my_list):
    print(n)


my_list = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda num:  num % 2  , my_list)))


