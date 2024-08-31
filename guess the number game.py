import random
n=random.randint(1,100)
a=-1
guesses=0

while(a!=n):
    a=int(input("gusess the number"))
    
    if(a>n):
        print("lower number please")
        guesses+=1
    elif(a<n):
        print("higher number please") 
        guesses+=1
        
print(f"u have guessses the number {n} in {guesses}attempt")