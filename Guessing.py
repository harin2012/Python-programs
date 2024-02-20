import tkinter as tk
from tkinter import messagebox
import random


class Player:
    def __init__(self, name, guess):
        self.name = name
        self.guess = guess


class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.players = []
        self.target_number = random.randint(1, 100)

        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack()

        self.num_players_label = tk.Label(
            self.entry_frame, text="Number of Players:")
        self.num_players_label.grid(row=0, column=0, padx=5, pady=5)

        self.num_players_entry = tk.Entry(self.entry_frame)
        self.num_players_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_entries_button = tk.Button(
            self.entry_frame, text="Add Entries", command=self.add_entries)
        self.add_entries_button.grid(row=0, column=2, padx=5, pady=5)

        self.player_frame = tk.Frame(master)
        self.player_frame.pack()

        self.player_entries = []

        self.start_game_button = tk.Button(
            master, text="Start Game", command=self.start_game)
        self.start_game_button.pack(pady=10)

        self.exit_button = tk.Button(
            master, text="Exit", command=self.master.destroy)
        self.exit_button.pack(pady=10)

    def create_player_entries(self):
        num_players = self.num_players_entry.get()
        if not num_players:
            messagebox.showerror(
                "Error", "Please enter the number of players.")
            return

        num_players = int(num_players)
        for i in range(len(self.players), len(self.players) + num_players):
            player_label = tk.Label(
                self.player_frame, text=f"Player {i+1} Name:")
            player_label.grid(row=i, column=0, padx=5, pady=5)
            player_name_entry = tk.Entry(self.player_frame)
            player_name_entry.grid(row=i, column=1, padx=5, pady=5)

            player_guess_label = tk.Label(
                self.player_frame, text="Guessing Number:")
            player_guess_label.grid(row=i, column=2, padx=5, pady=5)
            player_guess_entry = tk.Entry(self.player_frame)
            player_guess_entry.grid(row=i, column=3, padx=5, pady=5)

            self.player_entries.append((player_name_entry, player_guess_entry))

    def add_entries(self):
        self.create_player_entries()

    def start_game(self):
        results = []
        for player_entry in self.player_entries:
            name = player_entry[0].get()
            guess = player_entry[1].get()

            if not name or not guess:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    messagebox.showerror(
                        "Error", "Guessing number should be between 1 and 100.")
                    return
            except ValueError:
                messagebox.showerror(
                    "Error", "Guessing number should be numeric.")
                return

            if guess == self.target_number:
                results.append(
                    f"The player {name} guessed the correct number!")
            else:
                difference = abs(guess - self.target_number)
                results.append(
                    f"The player {name} is {'close' if difference <= 10 else 'far away'} to the target number: {difference}")

        messagebox.showinfo(
            "Game Results", f"Target number is {self.target_number}\n\n" + "\n".join(results))


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
