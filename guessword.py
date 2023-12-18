letters = [['h','o','l','i','d','a','y'],

           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],

           ['b','o','o','t','c','a','m','p'],

           ['f','l','o','w','c','h','a','r','t'],

           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

 

words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],

         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",

          "pong","pram","prom","ramp"],

         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",

          "comb","boom","pact","atom"],

         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",

          "fowl","wolf","crow","half"],

         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",

          "cope","crap","crew","crop","pace"]];

score=0  #indicates score of the user
level=0  #level of the game
lives=5  #minimum lives of the user

while level<5:
    print("Let's Play!!!")
    print(f"level{level+1}")
    print("Create minimum three words from the below letters")

    x={letter for letter in  letters[level]}
    print(x)

    #declare some variables to get input from the user and store in it

    Guess_Count=0
    Guess_Limit=3
    word=""
    oldword=""    

    while Guess_Count<Guess_Limit:
        match=False
        word=input("Guess the word:)").lower()
        if not (word==oldword):
            for i in words[level]:
                if(word==i):
                    Guess_Count+=1
                    score+=1
                    oldword=word
                    match=True

        if not match:
            print("Wrong Guess Brooh") 
            lives-=1  

        if lives==0:
            print("Better Luck Next Time:(")
            break
        
    if (lives==0):
        print("Lives over Game ended!!!") 
        break
    if level == 4:
        print('Thank you for playing the game!!!')
        print(f'Your score is ({score})')
        level += 1

    else:
        UserChoice = input('Do you want to go for the next round? (y/n) ').lower()
        if(UserChoice=="y"):
            level += 1
        else:
            print('Thanks for playing the game!!!')
            print(f'Your score is ({score})')
            break
     
            



    
    

