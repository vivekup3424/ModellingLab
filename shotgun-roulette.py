import random
import time
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class ShotgunRoulette:
    def __init__(self):
        self.shells = ["empty"] * 5 + ["loaded"]
        random.shuffle(self.shells)
        self.player_score = 0
        self.computer_score = 0
        self.round = 1

    def display_status(self):
        print("\n" + "=" * 50)
        print(f"Round {self.round}")
        print(f"Your score: {self.player_score}")
        print(f"Computer's score: {self.computer_score}")
        print("=" * 50 + "\n")

    def player_turn(self):
        print("\nYour turn!")
        choice = input(
            "What would you like to do? (1: Check chamber, 2: Pass to computer, 3: Pull trigger): "
        )

        if choice == "1":
            print(f"\nThe chamber is {self.shells[0]}")
            return self.player_turn()
        elif choice == "2":
            print("\nYou passed to the computer!")
            return self.computer_turn()
        elif choice == "3":
            print("\nYou pull the trigger...")
            time.sleep(1)

            if self.shells[0] == "loaded":
                print("BANG! You lose this round!")
                self.computer_score += 1
                return False
            else:
                print("*click* - Empty chamber! You're safe!")
                self.shells.pop(0)
                return True
        else:
            print("\nInvalid choice. Please try again.")
            return self.player_turn()

    def computer_turn(self):
        print("\nComputer's turn...")
        time.sleep(1)

        # Simple AI: If first chamber is loaded and was checked, always pass
        # Otherwise, 70% chance to pull trigger
        if random.random() < 0.7:
            print("Computer pulls the trigger...")
            time.sleep(1)

            if self.shells[0] == "loaded":
                print("BANG! Computer loses this round!")
                self.player_score += 1
                return False
            else:
                print("*click* - Empty chamber! Computer is safe!")
                self.shells.pop(0)
                return True
        else:
            print("Computer passes back to you!")
            return self.player_turn()

    def play_round(self):
        self.shells = ["empty"] * 5 + ["loaded"]
        random.shuffle(self.shells)

        print(f"\nRound {self.round} begins!")
        print("The chamber has been loaded and shuffled...")

        current_player = "player" if random.random() < 0.5 else "computer"

        while True:
            self.display_status()

            if current_player == "player":
                if not self.player_turn():
                    break
                current_player = "computer"
            else:
                if not self.computer_turn():
                    break
                current_player = "player"

    def play_game(self):
        clear_screen()
        print("Welcome to Shotgun Roulette!")
        print("\nRules:")
        print("1. Each round has 6 chambers, 5 empty and 1 loaded")
        print("2. On your turn, you can:")
        print("   - Check the current chamber")
        print("   - Pass to the computer")
        print("   - Pull the trigger")
        print("3. First to 3 points wins")
        print("\nPress Enter to start...")
        input()

        while max(self.player_score, self.computer_score) < 3:
            self.play_round()
            self.round += 1
            input("\nPress Enter for next round...")
            clear_screen()

        print("\nGame Over!")
        if self.player_score > self.computer_score:
            print("Congratulations! You won!")
        else:
            print("Computer wins! Better luck next time!")

        print(
            f"\nFinal Score - You: {self.player_score}, Computer: {self.computer_score}"
        )


if __name__ == "__main__":
    game = ShotgunRoulette()
    game.play_game()
