PlayAgain = "yes" #This sets the PlayAgain variable to yes so that the game can start
while PlayAgain != "NO".lower(): #If this variable is no, the game will stop
    import random #Fetches the randint function

    def WhoGoesFirst(): #This method asks the user if they want to go first or not
        wgf = input("Would you like to go first?[yes/no]: ")
        return wgf
    
    def Board(): #This method prints out the current game board
        print(SlotList[0],"|",SlotList[1],"|",SlotList[2])
        print("-"*10)
        print(SlotList[3],"|",SlotList[4],"|",SlotList[5])
        print("-"*10)
        print(SlotList[6],"|",SlotList[7],"|",SlotList[8])
        return ""

    def PlayerMove(SlotList,player,cpu): #This will ask for and apply the player's move onto the game board
        choice = int(input("Choose a slot, 1-9: "))
        for i in SlotList:
            if i == choice:
                SlotList[i-1] = player
        return choice
   
    def CpuMove(player,cpu): #This method determines which move the cpu will make. At first, it will be random, but later in the game, it starts to become logical.If
        choicelist = []      #the player is able to win the game in the next move, it will block the player. If the cpu is able to win the game with their next move,       
        for i in SlotList:   #then it will try to take that move.
            if i != player and i != cpu: #This makes sure the cpu doesn't choose an already filled slot
                choicelist = choicelist + [i]
        CpuChoice = (choicelist[random.randint(0,len(choicelist)-1)])
        CpuChoice = CpuLogic(CpuChoice, SlotList,player,cpu) #This line calls the CpuLogic method which will analyze the board and select the best move for the cpu
        for i in range(len(SlotList)):                       #to make
            if SlotList[i] == CpuChoice:
                SlotList[i] = cpu
        print(Board())
        return CpuChoice
    
    def PlayerWins(SpotList, choice): #This method checks whether or not the player has 3 in a row or not. If they do, the player wins the game.
        if ((SpotList[6] == choice and SpotList[7] == choice and SpotList[8] == choice) or (SpotList[3] == choice and SpotList[4] == choice and SpotList[5] == choice) or (SpotList[0] == choice and SpotList[1] == choice and SpotList[2] == choice) or (SpotList[6] == choice and SpotList[3] == choice and SpotList[0] == choice) or (SpotList[7] == choice and SpotList[4] == choice and SpotList[1] == choice) or (SpotList[8] == choice and SpotList[5] == choice and SpotList[2] == choice) or (SpotList[6] == choice and SpotList[4] == choice and SpotList[2] == choice) or (SpotList[8] == choice and SpotList[4] == choice and SpotList[0] == choice)):
            WinMessage = ("You Win!")
        else:
            WinMessage = ("")
        return WinMessage
    
    def CpuWins(SpotList, CpuChoice): #This checks whether or not the cpu has 3 in a row. If it does, the cpu wins the game
        if ((SpotList[6] == CpuChoice and SpotList[7] == CpuChoice and SpotList[8] == CpuChoice) or (SpotList[3] == CpuChoice and SpotList[4] == CpuChoice and SpotList[5] == CpuChoice) or (SpotList[0] == CpuChoice and SpotList[1] == CpuChoice and SpotList[2] == CpuChoice) or (SpotList[6] == CpuChoice and SpotList[3] == CpuChoice and SpotList[0] == CpuChoice) or (SpotList[7] == CpuChoice and SpotList[4] == CpuChoice and SpotList[1] == CpuChoice) or (SpotList[8] == CpuChoice and SpotList[5] == CpuChoice and SpotList[2] == CpuChoice) or (SpotList[6] == CpuChoice and SpotList[4] == CpuChoice and SpotList[2] == CpuChoice) or (SpotList[8] == CpuChoice and SpotList[4] == CpuChoice and SpotList[0] == CpuChoice)):
            LoseMessage = ("You Lose!")
        else:
            LoseMessage = ("")
        return LoseMessage
        
    def PlayAgain(): #Whenever the game finishes, this method is called upon. It asks the player if they want to play again. If they say yes, the game board is 
                     #reset. If they choose no, the code stops.
        PlayAgain = input("Would you like to play again? [yes/no] Make sure not to use caps lock: ")
        if PlayAgain != "no":
            for i in range(1,10):
                SlotList[i-1] = i
            print(Board())
        if PlayAgain == "no":
            exit()
            
    def CpuLogic(CpuChoice,SpotList,choice,cpu): #This entire method analyzes the board. It is seperated into 2 parts: offence and defence. In offence, if the cpu has
        # 2 in a row, then it will try to take the winning move. In defense, if the player has 2 in a row, the cpu will block him/her from taking the winning move.
        # The reason it is so long is because it has to analyze every winning combination(which there is 8 of), and then each winning combo has 3 combination, adding up
        # to 24 combinations. Finally, there is both offense and defense, adding up to a total of 48 possible moves that the cpu could take. THis method makes sure that
        # the cpu takes the best move strategically.
        #Offense
        if   (SpotList[6] == cpu and SpotList[7] == cpu) and SpotList[8] != choice:   
            CpuChoice = 9
        elif (SpotList[7] == cpu and SpotList[8] == cpu) and SpotList[6] != choice:
            CpuChoice = 7
        elif (SpotList[6] == cpu and SpotList[8] == cpu) and SpotList[7] != choice:
            CpuChoice = 8
        elif (SpotList[0] == cpu and SpotList[1] == cpu) and SpotList[2] != choice:  
            CpuChoice = 3
        elif (SpotList[0] == cpu and SpotList[2] == cpu) and SpotList[1] != choice:
            CpuChoice = 2
        elif (SpotList[1] == cpu and SpotList[2] == cpu) and SpotList[0] != choice:
            CpuChoice = 1                                                             
        elif (SpotList[0] == cpu and SpotList[3] == cpu) and SpotList[6] != choice:  
            CpuChoice = 7
        elif (SpotList[0] == cpu and SpotList[6] == cpu) and SpotList[3] != choice:
            CpuChoice = 4
        elif (SpotList[6] == cpu and SpotList[3] == cpu) and SpotList[0] != choice:
            CpuChoice = 1                                                              
        elif (SpotList[8] == cpu and SpotList[5] == cpu) and SpotList[2] != choice: 
            CpuChoice = 3
        elif (SpotList[8] == cpu and SpotList[2] == cpu) and SpotList[5] != choice:
            CpuChoice = 6
        elif (SpotList[5] == cpu and SpotList[2] == cpu) and SpotList[8] != choice:
            CpuChoice = 9                                                              
        elif (SpotList[0] == cpu and SpotList[4] == cpu) and SpotList[8] != choice:  
            CpuChoice = 9
        elif (SpotList[0] == cpu and SpotList[8] == cpu) and SpotList[4] != choice:
            CpuChoice = 5
        elif (SpotList[8] == cpu and SpotList[4] == cpu) and SpotList[0] != choice:
            CpuChoice = 1                                                               
        elif (SpotList[6] == cpu and SpotList[4] == cpu) and SpotList[2] != choice:   
            CpuChoice = 3
        elif (SpotList[6] == cpu and SpotList[2] == cpu) and SpotList[4] != choice:
            CpuChoice = 5
        elif (SpotList[2] == cpu and SpotList[4] == cpu) and SpotList[6] != choice:
            CpuChoice = 7                                                           
        elif (SpotList[1] == cpu and SpotList[4] == cpu) and SpotList[7] != choice:  
            CpuChoice = 8
        elif (SpotList[1] == cpu and SpotList[7] == cpu) and SpotList[4] != choice:
            CpuChoice = 5
        elif (SpotList[4] == cpu and SpotList[7] == cpu) and SpotList[1] != choice:
            CpuChoice = 2                                                            
        elif (SpotList[3] == cpu and SpotList[4] == cpu) and SpotList[5] != choice:  
            CpuChoice = 6
        elif (SpotList[3] == cpu and SpotList[5] == cpu) and SpotList[4] != choice:
            CpuChoice = 5
        elif (SpotList[4] == cpu and SpotList[5] == cpu) and SpotList[3] != choice:
            CpuChoice = 4
            
        #Defense
        elif (SpotList[6] == choice and SpotList[7] == choice) and SpotList[8] != cpu:   
            CpuChoice = 9
        elif (SpotList[7] == choice and SpotList[8] == choice) and SpotList[6] != cpu:
            CpuChoice = 7
        elif (SpotList[6] == choice and SpotList[8] == choice) and SpotList[7] != cpu:
            CpuChoice = 8                                                              
        elif (SpotList[0] == choice and SpotList[1] == choice) and SpotList[2] != cpu:  
            CpuChoice = 3
        elif (SpotList[0] == choice and SpotList[2] == choice) and SpotList[1] != cpu:
            CpuChoice = 2
        elif (SpotList[1] == choice and SpotList[2] == choice) and SpotList[0] != cpu:
            CpuChoice = 1                                                             
        elif (SpotList[0] == choice and SpotList[3] == choice) and SpotList[6] != cpu:  
            CpuChoice = 7
        elif (SpotList[0] == choice and SpotList[6] == choice) and SpotList[3] != cpu:
            CpuChoice = 4
        elif (SpotList[6] == choice and SpotList[3] == choice) and SpotList[0] != cpu:
            CpuChoice = 1                                                              
        elif (SpotList[8] == choice and SpotList[5] == choice) and SpotList[2] != cpu:  
            CpuChoice = 3
        elif (SpotList[8] == choice and SpotList[2] == choice) and SpotList[5] != cpu:
            CpuChoice = 6
        elif (SpotList[5] == choice and SpotList[2] == choice) and SpotList[8] != cpu:
            CpuChoice = 9                                                              
        elif (SpotList[0] == choice and SpotList[4] == choice) and SpotList[8] != cpu:  
            CpuChoice = 9
        elif (SpotList[0] == choice and SpotList[8] == choice) and SpotList[4] != cpu:
            CpuChoice = 5
        elif (SpotList[8] == choice and SpotList[4] == choice) and SpotList[0] != cpu:
            CpuChoice = 1                                                               
        elif (SpotList[6] == choice and SpotList[4] == choice) and SpotList[2] != cpu: 
            CpuChoice = 3
        elif (SpotList[6] == choice and SpotList[2] == choice) and SpotList[4] != cpu:
            CpuChoice = 5
        elif (SpotList[2] == choice and SpotList[4] == choice) and SpotList[6] != cpu:
            CpuChoice = 7                                                           
        elif (SpotList[1] == choice and SpotList[4] == choice) and SpotList[7] != cpu:  
            CpuChoice = 8
        elif (SpotList[1] == choice and SpotList[7] == choice) and SpotList[4] != cpu:
            CpuChoice = 5
        elif (SpotList[4] == choice and SpotList[7] == choice) and SpotList[1] != cpu:
            CpuChoice = 2                                                            
        elif (SpotList[3] == choice and SpotList[4] == choice) and SpotList[5] != cpu:  
            CpuChoice = 6
        elif (SpotList[3] == choice and SpotList[5] == choice) and SpotList[4] != cpu:
            CpuChoice = 5
        elif (SpotList[4] == choice and SpotList[5] == choice) and SpotList[3] != cpu:
            CpuChoice = 4                                                                
        return CpuChoice
        
    def TieCheck(SlotList):# This method checks to see if the board is full, and whether or not there are any winners. If there are no winners, and the board is full, 
                           # then the game is a tie. The tie variable is then set to true if this is the case.
        if 1 not in SlotList and 2 not in SlotList and 3 not in SlotList and 4 not in SlotList and 5 not in SlotList and 6 not in SlotList and 7 not in SlotList and 8 not in SlotList and 9 not in SlotList:
            Tie = True
            return Tie
    
    choice = 1 #This chunck of code is the setup for the game. It sets the number, draws the board, and asks the user whether they want to go first, and whether they
               # want to be X or O.
    SlotList = [1,2,3,4,5,6,7,8,9]
    print("Welcome to Tic-Tac-Toe!")
    
    print(Board())
    count = 0  # temporary variable thet helps check if the input was valid.      
    wgf = WhoGoesFirst()
    player = input("Do you want to be X or O?: ").upper()
    if player == "X" or "O":
        if player == "X":
            cpu = "O"
            count=0
        elif player == "O":
            cpu = "X"
            count=0
        else:
            print ("invalid")
            count= 1 # Tenporary variable 

    if count==1: 
        
        print("INVALID! Restart your game. Enter YES and contune")
   
    while count == 0:
    
        while (PlayerWins(SlotList,player)) != ("You Win!") or (CpuWins(SlotList,cpu)) != ("You Lose!") and PlayAgain != "NO".lower():
            if wgf == "yes":                                      # This is where the main part of the game takes place. It starts off by applying the move of the first player,
                choice = PlayerMove(SlotList,player,cpu)          # either cpu or player. It then checks whether or not that move was a winning move. If not, it then checks if 
                if (PlayerWins(SlotList,player)) == ("You Win!"): # the board is full. If it is, it announces that it is a tie game. If it is not a tie, then the move of the 
                    print("You Win!")                             # second player is applied. It then checks whether or not that move was a winning move. If this move was not
                    PlayAgain()                                   # a winning move, then the whole process is repeated until either a winner or a tie game is announced.            
                elif TieCheck(SlotList) == True:
                    print(Board())
                    print("The game is a tie!")
                    PlayAgain()
                else:
                    CpuMove(player,cpu)
                    if (CpuWins(SlotList,cpu)) == ("You Lose!"):
                        print("You Lose!")
                        PlayAgain()
            else:
                CpuMove(SlotList,tplayer,cpu)
                if (CpuWins(SlotList,cpu)) == ("You Lose!"):
                    print("You Lose!")
                    PlayAgain()
                elif TieCheck(SlotList) == True:
                    print("The game is a tie!")
                    PlayAgain()
                else:
                     choice = PlayerMove(player,cpu)
                if (PlayerWins(SlotList,player)) == ("You Win!"):
                    print("You Win!")
                    print(Board())
                    PlayAgain()