def password():                                                   #sakht ramz
    import random
    code = []
    count = 0
    while count < 4:
        x = random.randrange(1,7)
        if x in code:
            continue
        else:
            count += 1
            code.append(x)
    return code

def unlist(n):                                                 #tabdil list be adad
    num = 0
    for i in n:
        num = num*10 + i
    return num


def listing(code):                                             #rikhtan dar list                                           
    code1 = []
    for i in str(code):
        code1.append(int(i))
    return code1

def goodpass(n):                                                #tashkhis ramz motabar
    good = []
    x = listing(n)
    for i in x :
        if 0 < i < 7 and i not in good:
            good.append(i)
    if x == good :
        return 1
    else:
        return 0 


def check():                                                   #chek kardan hads v ramz
    mojood = 0
    crect = 0
    for i in range(4):
        if guess1[i] == number[i]:
            crect += 1
        elif guess1[i] in number and guess1[i] != number[i]:
            mojood += 1
        
    print(f'\n{crect} numbers are correct in right position')
    print(f'{mojood} numbers are correct in wrong position\n')
print("-----------------------------------------------")                         #shroo barname
print("Game name : Mastermind")
print("-----------------------------------------------\n")
print("Name : Amirhossein maleki")
print("Student ID : 404131233\n")
print("-----------------------------------------------")


number = password()                         # password creating

count = 0
while count < 10:
    print("-----------------------------------------------")
    print (f'choose {count+1} out of 10')
    guess = input("please enter your guees : ")         # get a guess
    if guess.isdigit() and len(guess) == 4 and goodpass(guess) == 1 :          # check 4-digit-(1,6) number
       guess1 = listing(guess)
       count += 1
       if guess1 == number:
           print(f'\nyou won!\ncorrect password was {unlist(number)} and you can guess the correct password in {count}th time...')
           print("\nFinish.........")
           print("\n-----------------------------------------------")
           print("-----------------------------------------------\n")
           break
       else :
           check()
    else :
        print ("\nyour guess isn't credible . please enter another password!\n")
        continue
if count == 10:
    print("-----------------------------------------------")
    print("you lose.\nthe correct password was " , unlist(number))
    print("\nFinish.........")
    print("\n-----------------------------------------------")
    print("-----------------------------------------------\n")
    
