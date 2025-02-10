import sys
class SportGame:
    def __init__(self):
        self.Answers = [["11", "6", "5"], 
                       ["90", "60", "48"], 
                       ["England", "Canada", "USA"]]
        self.sport_knowledge = [["Football", "Ice Hockey", "Basketball"], 
                       ["Number of Players", "Match Time (min)", "Originated Country"]]
        self.grid = self.create_grid()
        self.guess_grid = self.create_guess_grid()

    def create_grid(self):
        grid = {}
        count = 1
        for i in range(3):
            for j in range(3):
                grid[count] = self.Answers[i][j]
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
            print(f"{self.sport_knowledge[0][i]}\t\t", end='')
        print("\n" + '-'*90)

        count = 1
        for i in range(3):
            print(f"{self.sport_knowledge[1][i]}\t\t", end='')
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

            answer_guess = input("Guess the Answer: ")
            if answer_guess == self.grid[guess]:
                self.guess_grid[guess] = "✓"
                print("Correct guess!")
            else:
                print("Incorrect guess, try again!")
        print("Congrats, you have guessed all answers correctly!")
        sys.exit(1)

if __name__ == "__main__":
    print("Fill the grid with answers common to the column's top sports and row's left sports knowledge")
    game = SportGame()
    game.play()
