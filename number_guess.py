import random as r
no=int(input("enter any no between 1 and 100="))
prediction=range(1,101)
choosen=r.choice(prediction)
i=1
while no!=choosen:
    print("wrong guess try again")
    no=int(input("enter any no="))
    i+=1
    
print(f"you guessed correctly in {i} times.")

    