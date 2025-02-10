

class MovieGame:
    def __init__(self):
        self.actors = [["Leonardo DiCaprio", "Kate Winslet", "Johnny Depp"],
                       ["Emma Stone", "Brad Pitt", "Scarlett Johansson"],
                       ["Tom Hanks", "Julia Roberts", "Meryl Streep"]]
        self.movies = [["Titanic", "The Departed", "Pirates of the Caribbean"],
                       ["La La Land", "Fight Club", "The Avengers"]]
        self.grid = self.create_grid()
        self.guess_grid = self.create_guess_grid()
        self.wrong_guesses = 0
        self.hints = self.create_hints()

    def create_grid(self):
        grid = {}
        count = 1
        for i in range(3):
            for j in range(3):
                grid[count] = self.actors[i][j]
                count += 1
        return grid

    def create_guess_grid(self):
        guess_grid = {}
        for i in range(1, 10):
            guess_grid[i] = " "
        return guess_grid

    def create_hints(self):
        hints = {
            "Leonardo DiCaprio": "He won an Oscar for The Revenant.",
            "Kate Winslet": "She starred in The Reader.",
            "Johnny Depp": "He played Captain Jack Sparrow.",
            "Emma Stone": "She starred in La La Land.",
            "Brad Pitt": "He won an Oscar for Once Upon a Time in Hollywood.",
            "Scarlett Johansson": "She plays Black Widow in the Marvel Universe.",
            "Tom Hanks": "He starred in Forrest Gump.",
            "Julia Roberts": "She starred in Pretty Woman.",
            "Meryl Streep": "She has been nominated for 21 Academy Awards."
        }
        return hints

    def print_grid(self):
        print("\n" + '-' * 100)
        print("\t\t", end='')
        for i in range(3):
            print("{:<30}".format(self.movies[0][i]), end='')
        print("\n" + '-' * 100)

        count = 1
        for i in range(3):
            print("{:<30}".format(self.movies[1][i]), end='')
            for j in range(3):
                actor = self.guess_grid[count] if self.guess_grid[count] != ' ' else ''
                print("{:<2}. {:<27}".format(count, actor), end='')
                count += 1
            print("\n" + '-' * 100)

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

            actor_guess = input("Guess the actor/actress: ")
            if actor_guess == self.grid[guess]:
                self.guess_grid[guess] = "✓"
                print("Correct guess!")
                self.wrong_guesses = 0  # reset wrong guess count
            else:
                self.wrong_guesses += 1
                print("Incorrect guess, try again!")
                if self.wrong_guesses >= 3:
                    print(f"Hint: {self.hints[self.grid[guess]]}")
        print("Congrats, you have guessed all actors correctly!")
        sys.exit(1)


if __name__ == "__main__":
    print("Fill the grid with actors common to the column's top movie and row's left movie. ")
    game = MovieGame()
    game.play()
