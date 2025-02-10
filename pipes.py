import time
import sys

print('''                                     \U0001F600 WELCOME TO THE PIPE PUZZLE GAME! \U0001F600''')
print ('''\033[1m ----------------------------------------------------------------------------------------------------------------- 
|Swoosh! To kill the demon, you should use water to flood it!                                                     |
|You shall arrange the pipes in the correct order to create a continuous flow of water\U0001F4A7from                      |
|the starting point to the end point. You will be presented with a grid consisting of 9 pipes \U0001F600                  |
|and you need to rotate them to connect them properly.                                                            |
 ----------------------------------------------------------------------------------------------------------------- \033[0m
''')
print('''                                               \U0001F600HOW TO PLAY? \U0001F600''')
print('''\033[1m ------------------------------------------------------------------------------------------------------------------ 
|To rotate a pipe segment, you need to specify the row and column of the pipe you want to rotate (1-3).            |
|You also need to specify the direction of rotation, either clockwise ('d') or anti-clockwise ('a').               |
|Use the 'd' key to rotate the pipe segment clockwise and the 'a' key to rotate it anti-clockwise.                 |
|                                                                                                                  |
|Your goal is to connect the pipes in such a way that water flows from the starting point to the end point.        |
|Rotate the pipes strategically to create a continuous path for the water.The game will end when you successfully. |
|                                                                                                                  |
|Arrange the pipes correctly and lets flood the demon!\U0001F47EGood luck!\U0001F3C6                                               |
 ------------------------------------------------------------------------------------------------------------------ \033[0m
 ''')
 
ready = False

#straight pipe 
pipe1 = [
    ['\u250C','\u2500\u2500\u2556 ', '   ', '\u2553\u2500','\u2510'],
    ['\u2502','  \u2551 ', '  ', ' \u2551 ','\u2502'],
    ['\u2502','  \u2551 ', '  ', ' \u2551 ','\u2502'],
    ['\u2502','  \u2551 ', '  ', ' \u2551 ','\u2502'],
    ['\u2514','\u2500\u2500\u255C ', '   ', '\u2559\u2500','\u2518']
]

# horizontal pipe
pipe2 =  [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2558','\u2550\u2550\u2550', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u255B'],
    [' ','   ', '    ', '  ',' '],
    ['\u2552','\u2550\u2550\u2550', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u2555'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518']
    ]

# L shape pipe 
pipe3 = [
    ['\u250C','\u2500\u2556  ', '  \u2553', '\u2500\u2500','\u2510'],
    ['\u2502',' \u2551', '    \u255a', '\u2550','\u2550\u255B'],
    ['\u2502',' \u2551', '     ', '  ',' '],
    ['\u2502',' \u255a', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u2550\u2555'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518']
]

# 7 
pipe4 = [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2558','\u2550\u2550', '\u2550\u2550\u2550', '\u2550\u2550\u2557',' \u2502'],
    [' ','  ', '   ', '  \u2551',' \u2502'],
    ['\u2552','\u2550\u2550', '\u2557  ', '  \u2551',' \u2502'],
    ['\u2514','\u2500\u2500\u255C ', '   ', '\u2559\u2500','\u2518']
]

#  ╝ 
pipe5 = [
    ['\u250C','\u2500\u2500\u2556', '   ', ' \u2553\u2500','\u2510'],
    ['\u2558','\u2550\u2550', '\u255d   ', ' \u2551 ','\u2502'],
    [' ' , '  ' ,  '    ' ,  ' \u2551 ','\u2502'],
    ['\u2552','\u2550\u2550', '\u2550\u2550\u2550', '\u2550\u2550\u255d ','\u2502'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518'],
]

# ╔ shape pipe 
pipe6= [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2502',' \u2554\u2550\u2550', '\u2550\u2550', '\u2550\u2550\u2550','\u255B'],
    ['\u2502',' \u2551 ', '   ', '   ',' '],
    ['\u2502',' \u2551 ', '   \u2554', '\u2550\u2550','\u2555'],
    ['\u2514','\u2500\u255C  ', '  \u2559', '\u2500\u2500','\u2518'],
]

#straight pipe ║ 
anspipe1 = [
    ['\u250C','\u2500\u2500\u2556', '\U0001F4A7\U0001F4A7', '\u2553\u2500','\u2510'],
    ['\u2502','  \u2551', '\U0001F4A7', '\U0001F4A7\u2551 ','\u2502'],
    ['\u2502','  \u2551', '\U0001F4A7', '\U0001F4A7\u2551 ','\u2502'],
    ['\u2502','  \u2551', '\U0001F4A7', '\U0001F4A7\u2551 ','\u2502'],
    ['\u2514','\u2500\u2500\u255C', '\U0001F4A7\U0001F4A7', '\u2559\u2500','\u2518']
]

# horizontal pipe ═ 
anspipe2 =  [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2558','\u2550\u2550\u2550', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u255B'],
    [' \U0001F4A7','\U0001F4A7', '\U0001F4A7', '\U0001F4A7','\U0001F4A7'],
    ['\u2552','\u2550\u2550\u2550', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u2555'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518']
]

# L shape block 
anspipe3 = [
    ['\u250C','\u2500\u2556\U0001F4A7', '\U0001F4A7\u2553', '\u2500\u2500','\u2510'],
    ['\u2502',' \u2551', '\U0001F4A7\U0001F4A7\u255a', '\u2550','\u2550\u255B'],
    ['\u2502',' \u2551', '\U0001F4A7', '\U0001F4A7','\U0001F4A7\U0001F4A7'],
    ['\u2502',' \u255a', '\u2550\u2550\u2550\u2550', '\u2550\u2550','\u2550\u2555'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518']
]

#--> the 7 pipe 
anspipe4 = [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2558','\u2550\u2550', '\u2550\u2550\u2550', '\u2550\u2550\u2557',' \u2502'],
    ['\U0001F4A7','\U0001F4A7', '\U0001F4A7', '\U0001F4A7\u2551',' \u2502'],
    ['\u2552','\u2550\u2550', '\u2557', '\U0001F4A7\U0001F4A7\u2551',' \u2502'],
    ['\u2514','\u2500\u2500\u255C\U0001F4A7', '\U0001F4A7', '\u2559\u2500','\u2518']
]

#  ╝
anspipe5 = [
    ['\u250C','\u2500\u2500\u2556', '\U0001F4A7', '\U0001F4A7\u2553\u2500','\u2510'],
    ['\u2558','\u2550\u2550', '\u255d\U0001F4A7', '\U0001F4A7\u2551 ','\u2502'],
    ['\U0001F4A7' , '\U0001F4A7' ,  '\U0001F4A7' ,  '\U0001F4A7\u2551 ','\u2502'],
    ['\u2552','\u2550\u2550', '\u2550\u2550\u2550', '\u2550\u2550\u255d ','\u2502'],
    ['\u2514','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2518'],
]

# ╔ 
anspipe6= [
    ['\u250C','\u2500\u2500\u2500', '\u2500\u2500\u2500', '\u2500\u2500\u2500','\u2510'],
    ['\u2502',' \u2554\u2550\u2550', '\u2550\u2550', '\u2550\u2550\u2550','\u255B'],
    ['\u2502',' \u2551', '\U0001F4A7\U0001F4A7', '\U0001F4A7','\U0001F4A7'],
    ['\u2502',' \u2551', '\U0001F4A7\U0001F4A7\u2554', '\u2550\u2550','\u2555'],
    ['\u2514','\u2500\u255C', '\U0001F4A7\U0001F4A7\u2559', '\u2500\u2500','\u2518'],
]

thepipes = [[pipe1,pipe2,pipe1],[pipe5,pipe6,pipe2],[pipe4,pipe1,pipe3]]
modelanswer = [[pipe1,pipe1,pipe1],[pipe6,pipe5,pipe1],[pipe3,pipe2,pipe4]]

def readinstruction():
    global ready 
    ready = input('All you ready? (type --> YES <-- if you are all set!): ')
    if ready == 'YES' or ready == 'yes' or ready =='Yes':
        ready = True
        return 
    else:
        print('Seriously? 😄Please Answer Again.')
        readinstruction()
readinstruction()

def printing(thepipes):
    print("---------------------------------")
    print("\033[34m==============| ↓↓ |=============\033[0m")
    print("\033[34m==============|\U0001F4A7\U0001F4A7|=============\033[0m")

    for i in thepipes: 
        result0 = []
        result1 = []
        result2 = []
        result3 = []
        result4 = []
        for k in i:
            result0.extend(k[0])
            result1.extend(k[1])
            result2.extend(k[2])
            result3.extend(k[3])
            result4.extend(k[4])
        print(''.join(result0))
        print(''.join(result1))
        print(''.join(result2))
        print(''.join(result3))
        print(''.join(result4))
    print("\033[34m=========================| ↓↓ |==\033[0m")
    print("\033[34m=========================|\U0001F4A7\U0001F4A7|==\033[0m")

def moving(row,column,move):
    if move == 'd':
        if thepipes[row][column] == pipe3:
            thepipes[row][column] = pipe6
        elif thepipes[row][column] == pipe4:
            thepipes[row][column] = pipe5
        elif thepipes[row][column] == pipe5:
            thepipes[row][column] = pipe3
        elif thepipes[row][column] == pipe6:
            thepipes[row][column] = pipe4
        elif thepipes[row][column] == pipe1:
            thepipes[row][column] = pipe2
        elif thepipes[row][column] == pipe2:
            thepipes[row][column] = pipe1

    elif move == 'a':
        if thepipes[row][column] == pipe3:
            thepipes[row][column] = pipe5
        elif thepipes[row][column] == pipe4:
            thepipes[row][column] = pipe6
        elif thepipes[row][column] == pipe5:
            thepipes[row][column] = pipe4
        elif thepipes[row][column] == pipe6:
            thepipes[row][column] = pipe3
        elif thepipes[row][column] == pipe2:
            thepipes[row][column] = pipe1
        elif thepipes[row][column] == pipe1:
            thepipes[row][column] = pipe2

def get_row():
    row = input("pick a row (1-3):")
    if row.isdigit() and 0<int(row)<4:
        row =int(row)
    else: 
        print('\U0001F33CInvalid Input, Please Enter Again.\U0001F4AA')
        row = get_row()
    return(row)

def get_column():
    column = input("pick a column (1-3):")
    if column.isdigit() and 0<int(column)<4:
        column =int(column)
    else: 
        print('\U0001F33CInvalid Input, Please Enter Again.\U0001F4AA')
        column = get_column()
    return(column)

def get_move():
    move = input('Rotate (clockwise = d/ anti-clockwise = a): ')
    if move.isalpha() and move=='d' or move == 'a':
        move = move 
    else: 
        print('\U0001F33CInvalid input, please enter again.\U0001F4AA')
        move = get_move()
    return(move)

def delayprinting():
    time.sleep(0.75)

def victory():
    print("\033[30m",end='')
    print("\033[103m",end = '')
    print('          YOU WIN!        ')
    print('                          ')
    print("\033[0m")

while ready == True and thepipes != modelanswer: 
    print()
    printing(thepipes)
    print('\033[0m---------------------------------',end='')
    print('\033[1m',end='')
    print('\033[0m')
    row = get_row()
    column = get_column()
    move = get_move()
    moving(row-1,column-1,move)
    modelanswer[0][0]=thepipes[0][0] 
    modelanswer[0][2]=thepipes[0][2] 
    modelanswer[1][2]=thepipes[1][2] 

anspipes1 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[pipe6,pipe5,thepipes[1][2]],[pipe3,pipe2,pipe4]] 
anspipes2 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[pipe6,anspipe5,thepipes[1][2]],[pipe3,pipe2,pipe4]]
anspipes3 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[anspipe6,anspipe5,thepipes[1][2]],[pipe3,pipe2,pipe4]] 
anspipes4 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[anspipe6,anspipe5,thepipes[1][2]],[anspipe3,pipe2,pipe4]] 
anspipes5 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[anspipe6,anspipe5,thepipes[1][2]],[anspipe3,anspipe2,pipe4]] 
anspipes6 = [[thepipes[0][0],anspipe1,thepipes[0][2]],[anspipe6,anspipe5,thepipes[1][2]],[anspipe3,anspipe2,anspipe4]] 

if thepipes == modelanswer:
    printing(thepipes)
    printing(anspipes1)
    delayprinting()
    printing(anspipes2)
    delayprinting()
    printing(anspipes3)
    delayprinting()
    printing(anspipes4)
    delayprinting()
    printing(anspipes5)
    delayprinting()
    printing(anspipes6)
    victory()
    sys.exit(1)
