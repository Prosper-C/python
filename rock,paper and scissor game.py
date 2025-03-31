import random

options = ("rock", "paper", "scissors")
winning_cases = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

player_score = 0
computer_score = 0
tie_score = 0
rounds = 5  # Number of rounds

print("\n🎮 Welcome to Rock, Paper, Scissors! Best of 5 rounds! 🎮")

for round_number in range(1, rounds + 1):
    print("\n" + "=" * 30)
    print(f"🏁 Round {round_number} of {rounds}")
    print("=" * 30)

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("\nEnter a choice (rock, paper, scissors): ").strip().lower()

    print(f"\n🧑 Player: {player}")
    print(f"💻 Computer: {computer}")

    if player == computer:
        print("🤝 It's a Tie!")
        tie_score += 1
    elif winning_cases[player] == computer:
        print("🎉 You Win this round! ❤️👌")
        player_score += 1
    else:
        print("😂 You Lose this round! 🤣")
        computer_score += 1

    # Display current score
    print("\n📊 Scoreboard:")
    print(f"🧑 You: {player_score} | 💻 Computer: {computer_score} | 🤝 Ties: {tie_score}")

# Final results after 5 rounds
print("\n" + "=" * 30)
print("🏆 Final Results 🏆")
print("=" * 30)
if player_score > computer_score:
    print("🎉 Congratulations! You won the game! 👏🏽")
elif player_score < computer_score:
    print("💻 Computer wins! Better luck next time! 🤖")
else:
    print("🤝 It's a draw! Well played! 👏🏽")

print("\nThanks for playing! 🎮👋")
