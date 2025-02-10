import sys 
class CommonSenseGame:
    def __init__(self):
        self.Answer = [["Beijing", "Washington DC", "Tokyo"], 
                       ["Right", "Right", "Left"], 
                       ["2", "1", "4"]]
        self.Country_Common_Sense = [["China", "USA", "Japan"], 
                       ["Capital City", "Road Direction", "GDP Ranking"]]
        self.grid = self.create_grid()
        self.guess_grid = self.create_guess_grid()

    def create_grid(self):
        grid = {}
        count = 1
        for i in range(3):
            for j in range(3):
                grid[count] = self.Answer[i][j]
                count += 1
        return grid

    def create_guess_grid(self):
        guess_grid = {}
        for i in range(1, 10):
            guess_grid[i] = " "
        return guess_grid

    def print_grid(self):
        print("\n" + '-'*90)
        print("\t\t", end='')
        for i in range(3):
            print(f"{self.Country_Common_Sense[0][i]}\t\t", end='')
        print("\n" + '-'*90)

        count = 1
        for i in range(3):
            print(f"{self.Country_Common_Sense[1][i]}\t\t", end='')
            for j in range(3):
                print(f"{count}. {self.guess_grid[count] if self.guess_grid[count] != ' ' else ''}\t\t", end='')
                count += 1
            print("\n" + '-'*90)

    def play(self):
        while " " in self.guess_grid.values():
            self.print_grid()
            while True:
                try:
                    guess = int(input("Enter the grid number from 1 to 9: "))
                    if guess not in range(1, 10):
                        raise ValueError("Number must be in range 1-9")
                    break
                except ValueError as e:
                    print(e)
                    continue

            Answer_guess = input("Guess the Answer: ")
            if Answer_guess == self.grid[guess]:
                self.guess_grid[guess] = "✓"
                print("Correct guess!")
            else:
                print("Incorrect guess, try again!")
        print("Congrats, you have guessed all answers correctly!")
        sys.exit(1)


if __name__ == "__main__":
    print("Fill the grid with answers common to the column's top Countries and row's left Common Sense")
    game = CommonSenseGame()
    game.play()
