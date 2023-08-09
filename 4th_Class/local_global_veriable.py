#-----------------------------Local variable-----------------------


#declaring funtion
def add():
    #defining local  variable
    a=20
    c=a+5
    print("The sum is:",c)


add()

# print(a)   #a local variable tai kaj korbe na ,,,Tai commenmt kore rakhlam
# print(c)    #a local variable tai kaj korbe na




#------------------------------Global variable--------------------



x=20 #X  ta funtion er baire call korar por o deafault hishebe global variable dhore nibe


def sub():
    #defining local  variable
    #global x
    global y  #function er vitor e tai global likhe call korte hbe
    
    y=x-5
    print("The sub is:",y)

sub()

print(x)  #jehetu x and y global variable tai print hoyeche
print(y)

