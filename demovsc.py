"""print("good day")

score =100
secret_number =50
guess =int(input("enter your guess:"))
if guess ==secret_number:
    print("correct!")
    score =score +20
    print("your score:",score)
elif guess ==secret_number:
    print("Too high!")
    score =score - 10
    print("your score:",score)
else:
    print("Too low!")
    score =score - 10
    print("your score:",score)


    score =score - 10
    print("your score:",score)

"""
"""a=1                             # intialisation or starting
while a<10:                     # condition
      print(a , end=" ")        
      a+=1                      # incrementation\jump
print("\nloop over")
"""



#example 3 
row=int(input("enter a number for row:"))
column=int(input("enter a number for column:"))
symbol=input("enter a number for symbol:")
for x in range(1,row+1):
    for y in range (1, column+1):
        print(symbol,end="")
    print()
