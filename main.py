#Game description b4 the game -> Person who coded the game
import subprocess
import random 
import time 

#let the bool value be False since the player hasn't win the games
game1 = False
game2 = False
game3 = False
currentlevel = 1
minesweeper_sublevel = 1 

print('''
In a world consumed by darkness and despair, tragedy befalls your beloved. 
Your boyfriend, captured by the most evil demon known to mankind, awaits your rescue. 
It is now your destiny to embark on an extradinary journey to rescue him!

Prepare yourself, for your journey begins within a mysterious jungle, concealing deadly bombs beneath its surface. 
Navigate the jungle, avoiding hidden bombs while collecting one of your own as a powerful weapon against the demon. 

But the jungle is merely the first trial on your path. 
You will then encounter disconnected pipes, and your task is to match those fragments, forming a complete pipeline. 
Only then can you unleash water's power while preparing it to flood the demon's castle. 

But the demon has one final test in store for you, a test of wisdom. 
Your task is to answer a seris of questions, each more difficult than the last. 

With each step, you shall grow in strength and prowess. 
This journey is not for the faint-hearted, but your determination will guide you through the darkest of times. 
In the end, only the strongest and smartest warrior can hope to pass this impossible mission. 

Now, warrior, I ask you once again: Are you truly prepared to embark on this perilous journey?  
''')

#to activate minesweeper
def startminesweeper():
    print('\n You see a flag in front of you and you think there are mines ahead! \n You will have to mark down the bombs to go ahead')
    global game1
    global minesweeper_sublevel
    if minesweeper_sublevel == 1:
        result1 = subprocess.run(['python','minesweeper.py'])
    elif minesweeper_sublevel == 2:
        result1 = subprocess.run(['python','minesweeper2.py'])
    if result1.returncode == 1:
        game1 = True 
        minesweeper_sublevel += 1
        print('\nYou successfully cleared the path ahead!\n')
    else:
        game1 = False
        startminesweeper()
    return True


#to activate pipes 
def startpipes():
    global game2
    result2 = subprocess.run(['python', 'pipes.py'])
    if result2.returncode == 1:
        game2 = True 
        print('Yeah! Please get to the door to enter the next level.')
    else:
        game2 = False
    return True

#to activate grid games
def startgrid():
    global game3
    random_number = 0
    random_number = random.randint(1, 3)
    if random_number == 1: 
        result3 = subprocess.run(['python','grid_commonsense.py'])
        if result3.returncode == 1:
            game3 = True 
    elif random_number == 2: 
        result3 = subprocess.run(['python','grid_movies.py'])
        if result3.returncode == 1:
            game3 = True 
    elif random_number == 3: 
        result3 = subprocess.run(['python','grid_sports.py'])
        if result3.returncode == 1:
            game3 = True
    return True

#map and playermovement
def printmap(level,currentmap):
    for rows in currentmap:
        for col in rows:
            if col in level:
                print(f'{level[col]:>1}',end='')
            else:
                if col == '\n':
                    break
                else:
                    print(f'{col:>2}',end='')
        print()

def getPlayerpos(currentmap):
    row = 0
    for rows in currentmap:
        col = 0
        for cols in rows:
            if cols == 'P':
                return row, col
                break
            else:
                col += 1
        row += 1
    return row, col

def getInteractablepos(currentmap):
    games = []
    door = []
    row = 0
    for rows in currentmap:
        col = 0
        for cols in rows:
            if cols == 'B':
                games.append([row,col])
                col += 1
            elif cols == 'H':
                door.append([row,col])
            else:
                col += 1
        row += 1
    return door, games

def startgame(level):
    global currentlevel
    if currentlevel == 1:
        startminesweeper()
    elif currentlevel == 2:
        startpipes() 
    elif currentlevel == 3:
        startgrid()

    return True

def enterdoor(level):
    global currentlevel
    currentlevel += 1
    return True

def playermove(level, currentmap):
    row, col = getPlayerpos(currentmap)
    door, games = getInteractablepos(currentmap)
    wasd = ['w','a', 's', 'd', 'W', 'A', 'S', 'D']
    move = input('Input WASD (W:up A:left S:down D:right) to move: ')
    if move not in wasd:
        print('\n- - - - - - Invalid input - - - - - -\n')
        return True
    if move == 'w' or move == 'W':
        if currentmap[row-1][col] != 'X':
            currentmap[row][col] = ' '
            currentmap[row-1][col] = 'P'
            row -= 1
        else:
            print('\n- - - - - - You Bump Into A Wall - - - - - -\n')
    if move == 'a' or move == 'A':
        if currentmap[row][col-1] != 'X':
            currentmap[row][col] = ' '
            currentmap[row][col-1] = 'P'
            col -= 1
        else:
            print('\n- - - - - - You Bump Into A Wall - - - - - -\n')
    if move == 's' or move == 'S':
        if currentmap[row+1][col] != 'X':
            currentmap[row][col] = ' '
            currentmap[row+1][col] = 'P'
            row += 1
        else:
            print('\n- - - - - - You Bump Into A Wall - - - - - -\n')
    if move == 'd' or move == 'D':
        if currentmap[row][col+1] != 'X':
            currentmap[row][col] = ' '
            currentmap[row][col+1] = 'P'
            col += 1
        else:
            print('\n- - - - - - You Bump Into A Wall - - - - - -\n')
    if [row,col] in door:
        enterdoor(level)
        return False
    if [row,col] in games:
        startgame(level)
    return True

def level1():
    print('''
Hey there, warrior! 
Your journey begins in a jungle, where numerous bombs are hidden beneath to catch you off the guard. 
Your task is to navigate through the jungle and uncover all the safe squares and 
uncover all the safe squares without detonating any of the bombs. 

Each safe square holds a clue that reveals number of bombs nearby, 
and a wrong move can lead to death. 
However, the jungle has granted you a favor - the first click is always safe. 
To avoid clicking on mines, you may place a flag and mark it as a mine. 

In order to win the game, you must click on every square that does not have a mine under it. 
However, the Demon has prepared two levels for you, and you must win both in order to escape from the jungle

So, are you ready to start the game? The fate of your beloved rests in your hands. 
''')
    level = {'X':'🌴', 'B':'🚩', 'P':'👩', 'H':'🚪'}
    currentmap = []
    with open('map1Jungle.txt') as file:
        for line in file:
            letterlist = []
            for letter in line:
                letterlist.append(letter)
            currentmap.append(letterlist)
    check = True
    while check:
        printmap(level, currentmap)
        check = playermove(level, currentmap)

def level2():
    print('''

--------------------------------------------------------------------------------------
Ah, you have managed to survive this far, human. 👾
But do not be fooled by your small victories, the challenges are far from over. 👿
Brace yourself, for you are about to enter the treacherous realm of scorching lava! 🔥
Prepare to be both terrified and mesmerized by its fiery depths! 🌋
--------------------------------------------------------------------------------------
''')
    level = {'X':'🔥', 'B':'💧', 'P':'👩', 'H':'🚪'}
    currentmap = []
    with open('map2Lava.txt') as file:
        for line in file:
            letterlist = []
            for letter in line:
                letterlist.append(letter)
            currentmap.append(letterlist)
    check = True
    while check:
        printmap(level, currentmap)
        check = playermove(level, currentmap) 

def level3():
    level = {'X':'🔩', 'B':'📚', 'P':'👩', 'H':'🚪'}
    currentmap = []
    with open('map3Final.txt') as file:
        for line in file:
            letterlist = []
            for letter in line:
                letterlist.append(letter)
            currentmap.append(letterlist)
    check = True
    while check:
        printmap(level, currentmap)
        check = playermove(level, currentmap) 

#to be shown after the player passes all levels
def victory():
    print('''
 ___      ___ ___  ________ _________  ________   ________      ___    ___ ___   
|\  \    /  /|\  \|\   ____\\___   ___\\   __  \ |\   __  \    |\  \  /  /|\  \    
\ \  \  /  / | \  \ \  \___\|___ \  \_\ \  \|\  \\ \  \|\  \   \ \  \/  / | \  \   
 \ \  \/  / / \ \  \ \  \       \ \  \ \ \  \\\  \\ \   _  _\   \ \    / / \ \  \  
  \ \    / /   \ \  \ \  \____   \ \  \ \ \  \\\  \\ \  \\  \|   \/  /  /   \ \__\  
   \ \__/ /     \ \__\ \_______\  \ \__\ \ \_______\\ \__\\ _\ __/  / /      \|__|    
    \|__|/       \|__|\|_______|   \|__|  \|_______| \|__|\|__|\___/ /         ___  
                                                              \|___|/         |\__\ 
                                                                              \|__|
    ''')

    print('''
                                                                                                   


                                           =- ++%@@@%%%#-
               ..=+*%@@@%@*              -.+@@@@@+*@@@@@*+*
             .+ :+@@@@%@@+           =.*@@@%@%%@@@@%@%%%%%%%
            .-  =-  =++@              %%%@%%%%%%%%%*--%%@%@%%*
          =.  .:+@                   +:@%%%%%%%%@%%----+%@%%@%#
          ..+-. .=                  ==@@@@@@@@@@+--- -===@@@@@%
         +-*****-+                  *=@@@@%+*=--=+=--====*@@@@%
          ===----+                 + @=@@@@%====-=++--====*@@@@@=
        +=======++                 :+@=@@@@@+=========+*=+*@@@@@@
        +=+++====+*+                %@=@@@@@%+=+ --. :+=+*@@@@@@@
       =-=+**++==+**                @@@@@@@@@*++==*+===+%@@@@@@@@
        +*+***++++@++                @%@@@@@@@%++===+%%%@@@@@@@@
        *++***+++====.    -----++.   =+@@@@@@@%%%%@%%%%*@@@@@@@+
       .*+++**++========---------=%%   ---=@@@@@@%%%%%%**@@@@@*
          =:=**++**++===--------===% ==@+=---==@@%@%@%%%%*=@=-
           @.+***@*+====---------=**@@+===%@@+------==+*%%-%*+@@+
            :=--***++======------=*@+====%%@====+*+*+*=*@+========@+
                 =.-***+++++=======+++===@%%=-=+===+++*===@@======--=@
                    +: .=+***********+==*@@*@@===-----======%%+========+
                          =:=:=%@@@@@%*==@:::+@@+**+----==++*@@%========+*
                                  %%%%@@%*=%%@*@@*===+*+==-= @@==--**++++===+
                                  ****@@@@@@****@*%===+*==-==++@***%*======++==
                                  %%@@@@@%@@*****%@%@@======@%%******%======*+==
                                  @@@@@@@%@@***********@@@@@*******%%%%===========
                                  @@@@@@@@@%%%%%%%*****************%%%@#==========   
        
        ''')
    print('''
    
                                       *@@@@@@*                                         ...:::...
         -%@@@@@,                   =@@@@@@@@@@@@*.                                 ..-#@@@@@@@#-..
      +@@@@@%@@@@@@@@              @@@@@@@@@@@@@@@@@-                             .-@@@*:.    .#@@:   
     @@@@@@@*::=@@@@@@+           @@@@@@*-%@@@@@@@@@@+                          .-@@@*:.       .#@@:  
    -@@@@@@@+:::::=%@@@           @@@%=::::::-%@@@@@@-     .:+###*-.          .-@@=...         .%@@:   
    @@@@@==:::::::::;%@@          -::::::::::::--::;,     .*@@+-:::=#%*..    .#@=..            .#@@=                                  
    @==:::::::::::::;@@           ::::::::::::::;;,      .%@%.      ..=%*.  :%#:.              .@@@=                                            
    -@@*::::::::::::::@@            ==::::::::::::;.     =@@.          .*%:.%*.               .*@@@.                                        
    +@@@@@*::::::::=@@@%            :+=:::::::=;,        +@@.           .=%#%.               .+@@@=.                                           
    @@@@@@@@@@%%@%@@@@@@+               =.+==+:;         :@@.            .+@=               .+@@@*.                                            
    *@@@@@@@@@*==*%@@@@@-          :-**=*=-+*---+*=-:    .*@*.            .%:              ..%@@@+.                                    
    :@@@@%*++******++++*:        %%++=+=-----==--------+; .%@+                            .=@@@@:                                        
    **--%+++++++++++++--*+;     %++==/--------------\---+; .*@*                          .:%@@@*..                                          
   %+---/**++++++++++\---*;     ++*-=:--------------:=---=;  .-@%:                      .#@@@%:.                                     
   +=--+:*+++++++++++*:--=+;    ++--+:--------------:----+;    .+@#:.                  .*@@@%-.                                       
   +--+*:+++++++++++++:--==;    +--+=:--------------:-----;      .+%#-..              .=%@@%=.                                           
   +-+-*:*++++++++++++:--=+;    +=-+-:--------------:-----;        .-*#+:.           .#@@@+.                                            
   ++==*:++++++++++++*:*++*;    ++++=-------------@*:=+*--;          .:+*=:.       .:@@@*.                                    
   +----*++++++++++++++::=-;    *:*------=+**++++*=-:::+:*;            .=:.       :@@@-.                          
   ::::::::::::::::::::*=.        =*-::::::::::::::::::--+:                      .*@@:                         
                                                                                .%@=.                         
                                                                               .*#.                          
                                                                              ..          
        ''')

def main ():
    print('''
                             .                                                                   
                             @@-                                                                     
                            :@@                                      @@                              
                            @@%@                                    @*@:                             
                           -%*+@*                                  :% @:                             
                           +@@+@@.       .=-++@@@@%%+::-          -%:=@                              
                           :@%=*@-   =@@@@@@@%@---=*@*@@@@@-     %%--%*                              
                            @@+ :@@@@@.++.  -          :=:=@@-:*@+: +@                               
                             @@- @@@@=                     :@@%@@.:@@                                
              -     *+@      :%@@@+-                         ==@@*@*                                 
             +*=    :*@      :@@+                             - +@@@                                 
             -@:@*  @:@@    *@@@%+.                          :==.=@@@                                
              -%=.+.=*@     .@@* :%=+@+:                    +@%@.  =@@.              .@               
               @@-*- *     %@@ .:@****:*%=             .+@+***+%.   -@@             .@.               
                @%%%@+@   :@@=  @@+********@*-        %@=:*****:@   -@%-     *%@@ =+  :- _             
                    +%+   -@@+   @@:********:@%   +@@+**********@-   +@*   .%% :* -+   +             
                     %@=  -@@=     =@-*****:-=@-     @@%-*******=*   +@*    @-.*   .@**             
                     :@@= +@+-    :-@@@%@@%-          %@%+:******@  +=     %      ..@             
                      *@%+ @%+:     .=-                 :@*@==       @@:     % =                      
                       @*** @%-                                    .+@      =*--                     
                       =@@- @@=                                    -%:       -%:*                     
                        -%@  @@.                                   +:        *--@                     
                         +*%  @+.                                 %-        =%.@                     
                         :*=%. %+:.                            :@@%-        =*+@                     
                          @.@=  @@-:+                        :@@- :        +=.                     
                           @:@:   **%@@:.                  .@@@@* :%@@  -+- @+                       
                           :@:=+    -*@*=-:            +.=%@.    **.:-+**%*/                        
                            -+-         -**+**++:..-@@@@*:                                           
                                              :---+=                                     
    ''')
    global game1
    global game2
    global game3
    level1()
    level2()
    level3()
    if game1 == True and game2 == True and game3 == True:
        victory()

main()



