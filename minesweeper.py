import time
import random
import sys
# generates the levels as empty 2d lists with 0s 
level = [[0]*8 for i in range(8)] # 12 bombs
displaylevel = [['🌴']*8 for i in range(8)]

def addbombs(level, startmove):
    bombs = []
    #randomly generates bombs
    for i in range(12):
        x = random.randint(0, len(level) - 1)
        y = random.randint(0, len(level) - 1)
        bombs.append([x,y])

    #remove bomb if the starting move is a bomb, and removes bombs surrounding
    #so that breakadjacent is guaranteed
    bombs = [list(x) for x in set(tuple(i) for i in bombs)]
    if startmove in bombs:
        bombs.remove(startmove)
    surroundings = [[startmove[0], startmove[1]+1], [startmove[0], startmove[1]-1],
    [startmove[0]-1, startmove[1]], [startmove[0]+1, startmove[1]],
    [startmove[0]-1, startmove[1]+1], [startmove[0]-1, startmove[1]-1],
    [startmove[0]+1, startmove[1]+1], [startmove[0]+1, startmove[1]-1]]
    for loc in surroundings:
        if loc in bombs:
            bombs.remove(loc)
    #converts bombs into a list
    #puts bombs into the numbered level
    for i in bombs: 
        level[i[0]][i[1]] = '💣'
    return level, bombs

def addnumbers(level, bombs):
    right = False
    left = False
    top = False
    bottom = False
    #adds numbers surrounding the bombs, checks to see if it's within the level
    for i in bombs:
        if i[1] < len(level) - 1:
            right = True
            if level[i[0]][i[1]+1] != '💣':
                level[i[0]][i[1]+1] += 1
        if i[1] > 0:
            left = True
            if level[i[0]][i[1]-1] != '💣':
                level[i[0]][i[1]-1] += 1
        if i[0] > 0:
            top = True
            if level[i[0]-1][i[1]] != '💣':
                level[i[0]-1][i[1]] += 1
        if i[0] < len(level)-1:
            bottom = True
            if level[i[0]+1][i[1]] != '💣':
                level[i[0]+1][i[1]] += 1
        if top and left:
            if level[i[0]-1][i[1]-1] != '💣':
                level[i[0]-1][i[1]-1] += 1
        if top and right:
            if level[i[0]-1][i[1]+1] != '💣':
                level[i[0]-1][i[1]+1] += 1
        if bottom and left:
            if level[i[0]+1][i[1]-1] != '💣':
                level[i[0]+1][i[1]-1] += 1
        if bottom and right:
            if level[i[0]+1][i[1]+1] != '💣':
                level[i[0]+1][i[1]+1] += 1
        bottom = False
        top = False
        left = False
        right = False
    return level


def hiddenboarddisplay(level):
    #function that prints the solved state
    #only used for testing
    for rowlist in enumerate(level):
        print(rowlist[0],end=' ')
        for col in (rowlist[1]):
            if col == '💣':
                print(f'{col:>2}',end='')
            else:
                print(f'{col:>3}',end='')
        print()
    print()
    print('    ',end='')
    for x in range(len(level)):print(x,end='  ')
    print()

def levelselect():
    #used for testing
    choose = input('Choose Level(1/2/t): ')
    if choose == '1':
        level = level1
        displaylevel = displaylevel1
        n = 12
    if choose == '2':
        level = level2
        displaylevel = displaylevel2
        n = 20
    if choose == 't':
        level = testlevel
        displaylevel = testleveld
        n = 3
    return level, choose, displaylevel, n


def instructions(mode):
    #prints instruction if an invalid input is given, based on which situation
    if mode == 'flag':
        print('''Instructions:
        Enter row number and column number separated by a space to place a flag 🚩. Example: 1 1
        Flags can only be placed on trees 🌴. 
        Unflag a square by entering same row number and column number.
        ''')
    if mode == 'break':
        print('''Instructions:
        Enter row number and column number seperated by a space to clear a tree. Example: 1 1
        If there is a mine under the tree, you will lose :(
        You cannot clear a flagged tree
        If the number under a tree is 0, it will show all adjacent 0s that are connected to eachother, and show the other numbers around those 0s
        ''')
    if mode == 'start':
        print('''Instructions:
        Enter row number and column number seperated by a space to clear the first tree. Example: 1 1
        The first tree won't contain any mines, and the trees surrounding it won't have mines.
        ''')

def breakadjacent(row,col,displaylevel,level):
    #uses recursion to clear surrounding trees with 0 underneath
    if displaylevel[row][col] == 0:
        #exits if the tree has already been cleared
        #breaksquare goes through this function first before clearing the tree if it is 0
        return
    elif level[row][col] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        #clears the tree if it is not 0 and then exits
        displaylevel[row][col] = level[row][col]
        return
    else:
        #checks to see if surroundings are in valid positions before recurring , uses similar code to addnumbers()
        displaylevel[row][col] = 0
        if row < len(level) - 1:
            breakadjacent(row+1,col,displaylevel,level)
        if row > 0:
            breakadjacent(row-1,col,displaylevel,level)
        if col < len(level) - 1:
            breakadjacent(row,col+1,displaylevel,level)
        if col > 0:
            breakadjacent(row,col-1,displaylevel,level)
        if row < len(level) - 1 and col < len(level) - 1:
            breakadjacent(row+1,col+1,displaylevel,level)
        if row < len(level) - 1 and col > 0:
            breakadjacent(row+1,col-1,displaylevel,level)
        if row > 0 and col < len(level) - 1:
            breakadjacent(row-1,col+1,displaylevel,level)
        if row > 0 and col > 0:
            breakadjacent(row-1,col-1,displaylevel,level)
    return displaylevel


#uses inputs to clear a tree. If a 0 would be cleared then it runs the breakadjacent recursive function to clear the adjacent 0s and numbers surrounding those 0s
#otherwise clears the tree and adds the number from level to displaylevel
def breaksquare(location, displaylevel, level):
    #checks to see validity of input
    if len(location) == 2 and str(location[0]).isnumeric() and str(location[1]).isnumeric() and int(location[0]) in list(range(len(level))) and int(location[1]) in list(range(len(level))) :
        row = int(location[0])
        col = int(location[1])
        if displaylevel[row][col] == '🌴':
            if level[row][col] != 0:
                #replaces displaylevel to be the number, doesn't replace 0s and runs the breakadjacent recursive function
                displaylevel[row][col] = level[row][col]
                return displaylevel
            else:
                displaylevel = breakadjacent(row, col, displaylevel, level)
                return displaylevel
        elif displaylevel[row][col] in [0, 1, 2, 3, 4, 5, 6, 7, 8, '🚩']:
            #checks to see if the tile cleared is valid
            print('\n- - - - - - Invalid input - - - - - -\n')
            instructions('break')
            return displaylevel
    else:
        print('\n- - - - - - Invalid input - - - - - -\n')
        instructions('break')
        location = input('Enter col number and row number: ').split()
        # reformats the location to fit the level format, as the display is printed differently for readability
        if str(location[1]).isnumeric and str(location[0]).isnumeric():
            location[1] = len(level) - int(location[1]) -1
        location = location[::-1]
    return displaylevel


flags = []
#adds flags from player input, removes if flag is already placed
def addFlag(displaylevel):
    location = input('Enter col no. and row no.: ').split()
    location = location[::-1]
     # reformats the location to fit the level format, as the display is printed differently for readability

    #if len(input) == 2:
        #if [row, col] in flags:
            #flags.remove([row, col])

    #checks validity of input
    if len(location) == 2 and location[0].isnumeric() and location[1].isnumeric() and int(location[0]) < len(level) and int(location[1]) < len(level):
        location[0] = len(displaylevel) - int(location[0]) - 1
        row = int(location[0])
        col = int(location[1])
        #checks if there's already a flag in the tile, removes if so
        if [row, col] in flags:
            flags.remove([row, col])
            displaylevel[row][col] = '🌴'
            print(f'\n- - - -Unflagged successfully at {col,len(level)-row-1}- - - -\n')
            return displaylevel
        #adds flags to displaylevel
        elif displaylevel[row][col] == '🌴':
            displaylevel[row][col] = '🚩'
            flags.append([row, col])
            print(f'\n- - - -Flag placed successfully at {col,len(level)-row-1}- - - -\n')
            return displaylevel
        else:
            print('\n- - - - - - Invalid input - - - - - -\n')
            instructions('flag')
            return displaylevel
    else: 
        print('\n- - - - - - Invalid input - - - - - -\n')
        instructions('flag')
        return displaylevel
    return displaylevel


def boom():
    frame1 = """
                                                          *-.........................%              
                                                          @:.........................@              
                                                         +%.........................:@              
                                                         %=.........................=@              
                                                        =%..........................*%              
                                                        .@:.........................##              
                                                       .@=..........................#*              
                                                       *@:..........................##              
                                                     .%#............................*%              
                                                  %%................................=@                       
                                            .%@=.....................................%+             
                                         *@@=........................................+%             
                                 :=*%@@*=.......................................=.....%+                      
                           .%@*.......................................**....:#@:......+@           
                     =%@+................................................-*##+.........:@:          
               =@@@%=...................................................................@=        
       .%@@%@%:.........................................................................%+         
       @+....=-.........................................................................@+         
       @=#=%+.....-%*...................................................................@-         
        %#:....*%-.....................................................................+@         
          +%@@#.......-...............................................................*%           
           @#.=...%#................................................................*@*                 
           #@#@##....#*..................................................:-+#@@%=               
            -@..#..%+......+=.........................=#%@@#=-:::-:----:.                       
            :@==:+@::+..+#.......................=#@%=.                                                                                          
                 :@%%@@:.*..=#%%@%%%##%%@@%=                                                         
                """
    frame2 = """                                                 *                                                                           
                                                                **                                                          
                                                               @@  
                                                            @@@@#**   =+    
                                                        @@@@@@@@%%#%@+=       
                                                    @@@@@%%%%%@@@%##%@@@          
                                                  @@%%%%%%%%%%%%%%%#%@@@@        
                                                 @@@@%%%%%%%%%%%%%%%#=#%@@       
                                                @@@@%%%%%%%%%%%%%%%%%#-=%@@     
                                               @@@@@%%%%%%%%%%%%%%%%%%*:+%@      
                                               @@@@@%%%%%%%%%%%%%%%%%%*-*%@       
                                               @@@@@%%%%%%%%%%%%%%%%#+%%@@@      
                                               @@@@@@@%%%%%%%%%%%%%%%%%@@@       
                                                 @@@@@@@%%%%%%%%%%%%%%@@        
                                                   @@@@@@@@@@@@@@@%%%@@          
                                                      @@@@@@@@@@%@@@@            
                                                          @@@@@@@"""
    frame3 = """                                                    :=....                                                        
                                                                            ..#%*...                                                        
                                                                            ...%#-..               ..:%%*:.                                 
                                                                            .:%=..              ..+%%*:..                                 
                                                                    ......     .-+..            ...#%+...                                   
                                                                    .=%*:..     ....            .-%=...                                     
                                                                    .=#*...                   ::                                                        
                                                                        .==. .    ++    +++          
                                                                                === ==++           
                                                                                =======          ..=%*.  
                                                                        ++++++==--------===         ...-=*##-.
                                                                            +==---:::::---==++++  
                                                                                --:::::::--===+          
                                                                            ##+=+=-----==          
                                                                    @@@@@@@@%#####=--=====++    ..=+..    
                                                                    @@@@@@@@@####  ===      +++  .+%=..    
                                                        @@@@@@@@@@@@@@@%%%%###%@@@*+              ..=%*.  
                                                @@@@@@@@@@@@%%%%%%@@%@@@@%%%####%%@@@                
                                            @@@@@@%%%%%%%%%%%%%%%%%@@@@%%%##%%%%@@@                              
                                        @@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@                
                                        @@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@                 
                                        @@@%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%#**%%%%%%%@@                
                                    @@%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*:+%%%%%@@               
                                    @@%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=.=#%%%@@             
                                    @@%@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+.:+%%%@@@             
                                    @@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=..=%%%@@             
                                @%@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:..+%%@@@@            
                                @@%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+..-%%%@@            
                                @@%@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*..:#%%@@            
                                @@%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#..-#%%@@           
                                @@%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*..-%%%@@                     
                                    @@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+::%%%%%@@                             
                                    @@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@               
                                    @@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@                
                                        @@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@@@                 
                                        @@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%@@@@                   
                                            @@@@%@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@                     
                                            @@@@@%%%@@@@@@@@@@@@@%%%%%@@@@@                        
                                                @@@@@@@%%%%%%%%%%@@@@@@@                           
                                                        @@@@@@@@@@@@@@"""
    
    frame4 = """                                   . :@@@@@@@@@:.     .                                    
                              .-==-+@@%******#@@@==%@@@@@@+.                               
                         ...#@@@%%%@#***********@@@@##**#%@@@=  . :+#@@@%+:                
                          .@@#******************************@@+-@@@%#***#%@@@:             
                      .. .@%********************************#@@%*+++#*%%#***%@@.           
                   .:::. *@*********************************#@#++*#**++#@@#**#@%           
                =@@%###%@@#*******#%%***********************%***@#*******#@***@@-          
               @@***************@@#*******#****#****************#*********#****@@@:        
              :@%*************#@%****#****#*#**#*#**#*#**#*#****#****************@@*       
            .*@@@**********#@@@@**************************************************@@+:     
           .#@#************@%*#@#*+*******************************************+***#@@@@@+  
         ..=@#************#@****@###*#*####*##*#*####*####*##*#*#**#*#****************#@@@.
      ..   .@@********#*##*@%##*%*##*%#%##%*###%#%##%#%##%*####*%###*##@@*#*************%@+
            :@#*************%@#******#****#*#**#*#**#*#**#*#************#@#*************#@#
   .     -- .@#**********************#*#**#*#**#*#**#*#**#*#**#*******##*@@*************#@+
             *@#****#*#+##*###############%##+#%#########%#########+*##@#@%*##*#@@#****#@*.
      ::    --=@%#**#*####*##########%####%####%#%##%#%##%############%@@%#*##*#**@@**@@%. 
         .:   :@#****@%****#**#*#*##*#*####*####*####*####*####*%**##@@#***********@@@+.   
   .     :-   -@#***@@**********#*##*#*##*#*##*%*####*####*#**#*#*%@##********%#**#@.      
.     -:   .--:@@###%@##########%#@##%#%##%#%##%#%%#%#%##%#%##%#%###########*##@#@@+.    ..
      .     .:..=@###%@####%####%#*@#%#%%@%%%%%%%%%%%#%#+%#%##%#%####%####*=++*#=.         
   -:   .--.  .--@%***##%%%#*##*#*#%@@@@%#%####%####%####%##########*#**#*#**#@+-:    -:   
      ..    .:...=@@#*#*##*#*###%####%####%####%#%##%#%##%##########*#*##*#*%@+    .       
.     --   .--:  .=%@@@@@@%%#%%#%@%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%#%%#%##%#@@@=:   .-:    ..
   ..   .--.   ---   ---:=@@@@@@@@@@@@@@@%%#%%@%%%%%%%@@@@%%%%@@@@@@@@@@@@%.   :-.    ..   
   ..    :-.   --- ..--:-..-=+=:.@@##%##%@#*%*-=%%@@@#*%-%%%%@%*###+*#%@.--.   :-.    ..   
:     --   .---  .---.  :---. :--=@@%%#%%%@=@@=:#-*#--=@-#@%#%@@%####@%-.  .--:   .-:    ..
      ..    .:..:..:::::-----:-----+%@@@#=-=@@=:@=*#---@-*@%%%%%@@@%#:::... .:             
  .-:   .--.  .---   :--:  :---. .----..---=@@=:@=*#---@-=@%##%#%@---.  :--:   --:    -:   
      ..    .-.....--...----:.-------------=@@-:@-*#::-@--@@@@@@@=...:--... ::  :%#.  :%@@%
.     -:    :-:  .---.  :---  :---. .----..##@--@-*%---@--@- .:---.  ---:*@.@@#+=*++@+=--@:
   ..    :-.   ---   :--:  :---. :----..---@+@-:@:+%:--@*@@@%%@%  -@@@%=-+@@*----@@@@---+# 
   .     .:    :-: . :--:..:---:.:----.:+@@@#*#@@-+%--+@#------+@.#@-----*@@-----@@@%===@. 
.     -:   .--:   ----+%@@@@%%@@@+. .-+@%=------=@+@-@%---------%%@*-----%@=====+@@@+==##  
             .  . -@%*=---------=@#:-@@=---------*@@@+----------+@@=-====@@===-=#@@@=-=@.  
   ..    --    ---+@-------------=@%@*-----------+@@+---=+#%--=--#+:----=@======#@@*+*#*   
            ..    @#-------------=@@=------==-===+@*====#@@@@*+-=%--+--=+%==+**=%@@***@.   
      ..    .-.  :@=----=@@@@----%@*=+=-=@@@@*--=+@=++=%@@@@@===@%+==+==#++%*+==@@@*+**    
         ..    .-*@=----#@@*====+@*==-=+@@@@@*==+*====*@@@@@*==+@#+==#==+*#@+===@@#**@:    
               ..#@-======-====%@@==-=*@@@@@@+===%++==@@@@@@+++#@++++%+++*%%+++*@@@@@-     
      ..    .-.  @#=======++=%@@@+==++@@@@@@@+==#++++%@@:=@***#@+=++@%*##*@++++#@#***@.    
                :@**==-==++++=+@@==**#@@@@@@*+++@==+*@@::@#***@@*+++@####%@+++=#####+@:    
         ..    .%@+====@@@@#===#***+=@@@@@@+++=@@*###*@@@****@@#+==#@%##*@@+==+%####%%     
                @%===+*@@@@*===*##*==@@@@@##*+@@@*###*++==+%@@@*++=@@###@@@%@@@@@%@@+      
               .@*=++++@@%*==+*%**++++##+*##*@@@@**####*==@@@@###%@@@@@@@@@@@@@@@*.        
               *@++******+=++*#@*++++++*###%@@@@@@*#####@@@%@@@@@@@@@@@@@*@@@@=.           
              .@#+++*##+++=+*%@@@#*+=++*#%@@@#@-+@@@@@@@@@.@@@@@%@#=-:.                    
              -@*++*###**++%@@@@@@#*++*@@@@@@@.  +@@@@@%.:-=:. .-.                         
              %@==*#####%@@@@@@@@@%@@@@@@@@@:      ...                                     
             :@#*+=+#@@@@@@@@@@@-  : +@@@=:     :     ..     .                             
             *@@@@@@@@@@@@@@@-                                                             
                                                           """
    
    print(frame1)
    time.sleep(1) 
    print(frame2)
    time.sleep(1)
    print(frame3)
    time.sleep(1)
    print(frame4)











#checks the board to see if the game should be over. returns False if the game is over and returns True if the game should still run
def boardcheck(bombs, displaylevel, level):
    # if level[row][col] == '💣':
    #     print('You stepped on A MINE! GAME OVER!')
    #     return False
    # elif displaylevel[row][col] != '🌴' and displaylevel[row][col] != '🚩':
    #     count += 1
    
    #converts displaylevel into a large list
    totallevel = []
    for rowlist in displaylevel:
        for col in rowlist:
            totallevel.append(col)
    #iterates through the list to see if a mine was stepped on
    if '💣' in totallevel:
        boom()
        print('You stepped on A MINE! GAME OVER!')
        sys.exit(2)
        return False
    #counts the amount of remaining trees/flags to see if all the bombs have been cleared
    count = 0
    for i in totallevel:
        if i == '🌴' or i == '🚩':
           count += 1
    if count == len(bombs):
        print("CONGRATS!!!! YOU WON")
        return False
    return True
    
def boarddisplay(displaylevel):
    #prints the board and numbers using formatting
    print()
    print('v Row',end='  ')
    for x in range(len(level)):print(x,end='   ')
    print()
    print()
    revdisplay = displaylevel[::-1]
    for rowlist in list(enumerate(revdisplay))[::-1]:
        print(rowlist[0],end='   ')
        for col in (rowlist[1]):
            if col == '🌴' or col == '🚩' or col == '💣':
                print(f'{col:>3}',end='')
            else:
                print(f'{col:>4}',end='')
        print(f'{rowlist[0]:>5}')
    print()
    print('Col > ',end=' ')
    for x in range(len(level)):print(x,end='   ')
    print()
    return displaylevel

displaylevel = boarddisplay(displaylevel)

def startmoving(level):
    #starting input has to be kept seperate so that the player doesn't hit a bomb in the first move
    startmove = input('Enter col no. and row no. to  start:').split()
    if len(startmove) == 2:
        for i in startmove:
            if not str(i).isnumeric() and i not in range(len(level)):
                print('\n- - - - - - Invalid input - - - - - -\n')
                instructions('start')
                return startmoving(level)
        #changing format 
        startmove = [int(x) for x in startmove]
        startmove[1] = len(level) - startmove[1] - 1
        startmove = startmove[::-1]
        return startmove
    else:
        print('\n- - - - - - Invalid input - - - - - -\n')
        instructions('start')
        return startmoving(level)
    
#pre-game setting up 
startmove = startmoving(level)
level, bombs = addbombs(level, startmove)
level = addnumbers(level, bombs)
breaksquare(startmove, displaylevel, level)
#hiddenboarddisplay(level)
displaylevel = boarddisplay(displaylevel)

check = True
#runs through the while loop until boardcheck returns false
while check:
    option = input('Break square or add Flag (b/f): ')
    if option == 'b':
        location = input('Enter col number and row number: ').split()
        if len(location) == 2 and str(location[1]).isnumeric and str(location[0]).isnumeric():
            #changing input format
            location[1] = len(level) - int(location[1]) -1
            location = location[::-1]
            displaylevel = breaksquare(location, displaylevel, level)
            displaylevel = boarddisplay(displaylevel)
            check = boardcheck(bombs, displaylevel, level)
        else:
            print('\n- - - - - - Invalid input - - - - - -\n')
            instructions('break')
    elif option == 'f':
        displaylevel = addFlag(displaylevel)
        displaylevel = boarddisplay(displaylevel)
    elif option == 'q':
        break
    else:
        print('\n- - - - - - Invalid input - - - - - -\n')

sys.exit(1)
