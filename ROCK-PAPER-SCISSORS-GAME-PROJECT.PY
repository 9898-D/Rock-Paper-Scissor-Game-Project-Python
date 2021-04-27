#  ----------------------------------- ROCK PAPER SCISSOR GAME -------------------------------------------  


#  CREATE A 2 VARIABLR TO TRACKING WINING GAME for Both

player_count=0          #for count PLAYER WIN
computer_count=0        #for count COMPUTER WIN


#  Write a function To Player choose a ROCK PAPAER SCISSOR

def player_choose():
    
    """
    [get input from user (R P S) ]

    Returns:
        [STRING]: [we get input user and check it RIGHT or WRONG in while loop]
    """
    
    choice="WRONG"
    
    while choice not in ['R','P','S']:  # FOR REPEATLY ASK INPUT IF USER CAN GIVE WROMNG INPUT
        
        choice=input("\nUser Choice: Choose (R,P,S) ").upper() 
        
        if choice not in ['R','P','S']:
            print(" \nINVALID INPUT! ")
        
        if choice=='R':
            choice='R'
        
        elif choice=="P":
            choice='P'
        
        elif choice=='S':
            choice='S'
        
        else:
            pass
        
    return choice
    
#print(player_choose())


#  Write a function to PLAY COMPUTER PLAYER AS RANDOM THROUGH

import random  # TO RANDOM CHOOSE NUMBER IN 1 2 3 and GIVE OUTPUT
def comp_choose():
    
    """
    [get input from computer as use with random]

    Returns:
        [STRING]: [comp select randomly (1,2,3) and compare and return it STRING ]
    """
    comp=random.randint(1,3)
    
    if comp==1:
        comp='R'
    
    elif comp==2:
        comp='P'
    
    elif comp==3:
        comp='S'
    
    return comp

#print(comp_choose())
  
  
  #  WRITE A FUNC TO PLAY AGAIN GAME
  
def ply_again():
    
    """
    [if player should be play again or not ]

    Returns:
        [STRING]: [player choice (Y OR N) and if select Y game is restart and if N game is EXIT]
    """
      
    choice="WRONG"
      
    while choice not in ['Y','N']:
          
        choice=input("\nWould You Like To Play Game Again (Y , N): ").upper()
          
        if choice not in ['Y','N']:
            print("\nINVALID INPUT! Y OR N")
    
    return choice=='Y'
        
#ply_again()


# ---------------------------------------- LOGIC PART -----------------------------------------

game_on=True
while game_on:
    
    print("\nWELCOME TO ROCK PAPER AND SCISSOR GAME! ")
    
    ply_choose=player_choose() # Assign a player choose input in variable
    
    cmp_choose=comp_choose()   # Assign a comp choose input in variable
    
    #  COMPARE A BOTH VALUE AND POSSIBILITY CONDITIONS
    
    if  ply_choose=='R' and cmp_choose=='R':
        print(" \nPlayer Choose ROCK AND Computer Choose Rock ")
        print(" \n\tGAME TIE ")
    
    elif ply_choose=='R' and cmp_choose=='P':
         print(" \nPlayer Choose ROCK AND Computer Choose PAPER ")
         print(" \n\tCOMPUTER WIN ")
         computer_count=computer_count+1
    
    elif ply_choose=='R' and cmp_choose=='S':
         print(" \nPlayer Choose ROCK AND Computer Choose SCISSOR ")
         print(" \n\tYOU WIN ")
         player_count=player_count+1
    
    elif ply_choose=='P' and cmp_choose=='P':
         print(" \nPlayer Choose PAPER AND Computer Choose PAPER ")
         print(" \n\tGAME TIE ")
    
    elif ply_choose=='P' and cmp_choose=='R':
         print(" \nPlayer Choose PAPER AND Computer Choose ROCK ")
         print(" \n\tYOU WIN ")
         player_count=player_count+1
    
    elif ply_choose=='P' and cmp_choose=='S':
         print(" \nPlayer Choose PAPER AND Computer Choose SCISSOR ")
         print(" \n\tCOMPUTER WIN ")
         computer_count=computer_count+1
    
    elif ply_choose=='S' and cmp_choose=='S':
         print(" \nPlayer Choose SCISSOR AND Computer Choose SCISSOR ")
         print(" \n\tGAME TIE ")
    
    elif ply_choose=='S' and cmp_choose=='R':
         print(" \nPlayer Choose SCISSOR AND Computer Choose ROCK ")
         print(" \n\tCOMPUTER WIN ")
         computer_count=computer_count+1
    
    elif ply_choose=='S' and cmp_choose=='P':
         print(" \nPlayer Choose SCISSOR AND Computer Choose PAPER ")
         print(" \n\tYOU WIN ")
         player_count=player_count+1
    
    else:
        pass
    
    print(f" \nPLAYER WINS: {player_count} ")
    print(f" \nCOMPUTER WINS: {computer_count} ")
    
    game_on=ply_again()
        
    
    
    
        