import os
import random
import time
import pygame

# Hide the Pygame support prompt
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# Initialize Pygame mixer
pygame.mixer.init()


def type_text(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 0


class GuessTheNumberGame:
    def __init__(self):
        self.players = []
        self.grid_size = 0
        self.difficulty = 0

    def play_sound(self, sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    def welcome_message(self):
        self.play_sound("sound/welcome.wav")
        type_text("WELCOME TO THE 'GUESS THE NUMBER' GAME!")
        time.sleep(2)

    def instructions(self):
        valid_input = False
        while not valid_input:
            ins = input("Do you want me to explain the instructions? yes/no\n")
            self.play_sound("sound/correct.wav")
            if ins == "yes":
                type_text("Each player will guess the number.")
                time.sleep(1)
                type_text("For every correct digit in the correct place, the player will get a gold.")
                time.sleep(1)
                type_text("For every correct digit in the wrong place, the player will get a silver.")
                time.sleep(1)
                type_text("The game will end for a player if he or she guesses the number correctly.")
                time.sleep(1)
                type_text("The player who takes the least number of guesses will win.")
                time.sleep(1)
                type_text("So, let's get started!")
                print("")
                time.sleep(2)
                valid_input = True
            elif ins == "no":
                print("Cool, let's get started!")
                print("")
                time.sleep(2)
                valid_input = True
            else:
                self.play_sound("sound/incorrect.wav")
                print("Invalid input. Please try again.")

    def select_difficulty(self):
        self.play_sound("sound/welcome.wav")
        print("Difficulty levels:")
        print("1. Easy: Guess a 3 digit number")
        print("2. Medium: Guess a 4 digit number")
        print("3. Hard: Guess a 5 digit number")
        print("")
        time.sleep(2)

        valid_input = False
        while not valid_input:
            choice = int(input("Enter your choice: "))
            self.play_sound("sound/correct.wav")
            if 1 <= choice <= 3:
                self.difficulty = choice
                valid_input = True
            else:
                self.play_sound("sound/incorrect.wav")
                print("Invalid input. Please try again.")

    def add_players(self):
        for m in range(2):
            print(f"\n---------------PLAYER {m + 1}---------------\n")
            name = input("Enter your name: ")
            self.play_sound("sound/correct.wav")
            self.players.append(Player(name))

    def start_game(self):
        for player in self.players:
            print(f"\n---------------{player.name}---------------\n")
            num = random.randint(10 ** (self.difficulty + 1), 10 ** (self.difficulty + 2) - 1)
            x = list(str(num))
            i = 0
            print("Enter a number: ")
            while True:
                n = input()
                self.play_sound("sound/correct.wav")
                if len(n) != self.difficulty + 2:
                    self.play_sound("sound/incorrect.wav")
                    print(f"Please enter a number having {self.difficulty + 2} digits")
                    continue
                gold = 0
                silver = 0
                for p in range(self.difficulty + 2):
                    if n[p] == x[p]:
                        gold += 1
                        x[p] = "1000000"
                for p in range(self.difficulty + 2):
                    for q in range(self.difficulty + 2):
                        if n[p] == x[q]:
                            silver += 1
                            x[q] = "1000000"
                if gold == self.difficulty + 2:
                    self.play_sound("sound/winner.wav")
                    print("You guessed it right!")
                    break
                k = "golds" if gold != 1 else "gold"
                l = "silvers" if silver != 1 else "silver"
                self.play_sound("sound/correct.wav")
                print(f"{gold} {k}, {silver} {l}")
                i += 1
                x = list(str(num))
            player.guesses = i
            print(f"\nYou have taken {i} guesses\n")
            time.sleep(2)

    def announce_winner(self):
        time.sleep(2)
        self.play_sound("sound/correct.wav")
        print("Game over")
        time.sleep(2)
        if self.players[0].guesses == self.players[1].guesses:
            self.play_sound("sound/winner.wav")
            print("Oops, It's a TIE!")
        else:
            winner = min(self.players, key=lambda player: player.guesses)
            self.play_sound("sound/winner.wav")
            print(f"Congratulations, {winner.name} WINS!")
        print("")
        time.sleep(2)
        self.play_sound("sound/welcome.wav")
        type_text("Goodbye from 'NJ PRODUCTION'")
        input("")

    def run(self):
        self.welcome_message()
        self.instructions()
        self.select_difficulty()
        self.add_players()
        self.start_game()
        self.announce_winner()


if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.run()
