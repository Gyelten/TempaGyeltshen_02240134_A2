import random
from TempaGyeltshen_02240134_A2_PB import CardBinder
from TempaGyeltshen_02240134_A2_PB import AlbumTracker 

class Scoreboard:
    def __init__(self):
        self.guess_score = 0
        self.rps_score = 0
        self.trivia_score = 0

    def display_scores(self):
        print("\n--- Overall Scores ---")
        print(f"Guess Number Game Score: {self.guess_score}")
        print(f"Rock Paper Scissors Score: {self.rps_score}")
        print(f"Trivia Pursuit Score: {self.trivia_score}")
        print("-----------------------\n")


class GuessNumberGame:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        num = random.randint(1, 10)
        attempts = 0
        print("\nGuess a number between 1 and 10")
        while True:
            try:
                guess = int(input("Enter the guessed number: "))
                if guess < 1 or guess > 10:
                    raise ValueError("Guess must be between 1 and 10")
                attempts += 1
                if (guess == num):
                    print("You got it right")
                    print("Number of attempts = ", attempts)
                    break
                elif (guess < num):
                    print("Bigger number")
                    
                elif (guess > num):
                    print("Lesser number")
                    
            except ValueError as e:
                print(f"Invalid input: {e}")
        score = max(0, 10 - attempts)
        print(f"Your score: {score}")
        self.scoreboard.guess_score += score


class RockPaperScissorsGame:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def play(self):
        choices = ["rock", "paper", "scissors"]
        win_count = 0
        print("\nLet's play Rock, Paper, Scissors!")
        playing = True
        
        while playing:
            for _ in range(3):
                computer = random.choice(choices)
                player = input("Choose rock, paper, or scissors: ").lower()
                if player not in choices:
                    print("Invalid input. Skipping round.")
                    continue
                print(f"Computer chose: {computer}")
                if player == computer:
                    print("It's a tie!")
                elif (player == "rock" and computer == "scissors"):
                    print("You win!")
                    win_count += 1
                elif (player == "paper" and computer == "rock"):
                    print("You win!")
                    win_count += 1
                elif (player == "scissors" and computer == "paper"):
                    print("You win!")
                    win_count += 1
                else:
                    print("You lose!")

            print(f"Total wins: {win_count}")
            if not input("Play again? (y/n): ").lower()== "y":
                
                playing = False
            
            self.scoreboard.rps_score += win_count

class TriviaPursuitGame:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard
        self.questions = {
            "Science": [
                ("What is the full form of CPU?", "c", {"a": "Computer Processing Unit", 
                                                        "b": "Computer Principle Unit", 
                                                        "c": "Central Processing Unit",
                                                        "d": "Control Processing Unit"}),
                ("Who is the father of Computers?", "b", {"a": "James Gosling", 
                                                          "b": "Charles Babbage", 
                                                          "c": "Dennis Ritchie", 
                                                          "d": "Bjarne Stroustrup"}),
                ("Which of the following is the correct abbreviation of COMPUTER?", "d", {"a": "Commonly Occupied Machines Used in Technical and Educational Research", 
                                                                                          "b": "Commonly Operated Machines Used in Technical and Environmental Research", 
                                                                                          "c": "Commonly Oriented Machines Used in Technical and Educational Research", 
                                                                                          "d": "Commonly Operated Machines Used in Technical and Educational Research"}),
                ("Which of the following computer language is written in binary codes only?", "b", {"a": "pascal", 
                                                                                                    "b": "machine language", 
                                                                                                    "c": "C", 
                                                                                                    "d": "C#"})
            ]
        }

    def play(self):
        correct = 0
        print("\n--- Trivia Pursuit ---")
        for category, qs in self.questions.items():
            print(f"\nCategory: {category}")
            for q, ans, options in qs:
                print(q)
                for key, val in options.items():
                    print(f"  {key}) {val}")
                guesses = input("Your answer: ").lower()
                if guesses == ans:
                    print("Correct!")
                    correct += 1
                else:
                    print(f"Wrong. Correct answer was {ans}) {options[ans]}")
        print(f"Total correct answers: {correct}")
        self.scoreboard.trivia_score += correct

class PokemonCardBinderManager:
    def __init__(self):
        self.album = AlbumTracker()

    def manage(self):
        print("\nWelcome to Pokemon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("1. Add Pokemon card")
            print("2. Reset Binder")
            print("3. View current placements")
            print("4. Exit ")
            choice = input("Enter your choice: ")
            if choice == '1':
                CardBinder.input_card(self)
            elif choice == '2':
                self.album.clear_album()
            elif choice == '3':
                print("\nCurrent Cards in Binder:")
                self.album.show_contents()
            elif choice == '4':
                self.album.quit()
                break
            else:
                print("Invalid input. Try again.")


class MainProgram:
    def __init__(self):
        self.scoreboard = Scoreboard()
        self.guess_game = GuessNumberGame(self.scoreboard)
        self.rps_game = RockPaperScissorsGame(self.scoreboard)
        self.trivia_game = TriviaPursuitGame(self.scoreboard)
        self.pokemon_manager = PokemonCardBinderManager()

    def run(self):
        while True:
            print("\nSelect a function (0-5):")
            print("1. Guess Number game")
            print("2. Rock paper scissors game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall score")
            print("6. Exit program")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.guess_game.play()
            elif choice == '2':
                self.rps_game.play()
            elif choice == '3':
                self.trivia_game.play()
            elif choice == '4':
                self.pokemon_manager.manage()
            elif choice == '5':
                self.scoreboard.display_scores()
            elif choice == '6':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid input. Try again.")


if __name__ == '__main__':
    MainProgram().run()