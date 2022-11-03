import random


def generate_guess():
    digits=[str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def get_guess():
    return list(input("Enter any 3 digit number"))
def generate_clues(code,user_code):
    
    if (user_code==code):
        return("CODE CRACKED")

    clues=[]
    for ind,num in enumerate(user_code):
        if num==code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues==[]:
        return["Nope"]
    else:
        return clues

print("Welcome to the game")
secretcode=generate_guess()
print("Code has been generated,please guess a 3 digit number")
clueReport=[]

while clueReport!="CODE CRACKED":
    guess=get_guess()

    clueReport=generate_clues(guess,secretcode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)

    

        
    

    
