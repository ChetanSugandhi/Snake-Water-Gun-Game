import random

def game(): 
    print('''🌟 Welcome to the Python Snake-Water-Gun Game! 
    🌟 Let's begin the fun! 🎮
    Press 1 for Snake
    Press -1 for Water
    Press 0 for Gun
    Press 3 to Exit Game !!
    ''')

    sample_dict = {"snake": 1, "water": -1, "gun": 0}
    reverse_dict = {1: "snake", -1: "water", 0: "gun"}

    while True:
        try:
            user = input("🪄 Enter your choice (Snake, Water, Gun or 'Exit' to quit): ").lower()

            if user == "exit":
                print("\n🌟 Thanks for playing! Come back soon! 🎉")
                break

            if user not in sample_dict:
                print("\n🚫 Oops! Invalid choice. Please choose between Snake, Water, Gun, or Exit.")
                continue

            user_choice = sample_dict[user]
            computer_choice = random.choice([1, -1, 0])
            computer_move = reverse_dict[computer_choice]

            print(f"\n🧑 You chose: {user.capitalize()}")
            print(f"💻 Computer chose: {computer_move.capitalize()}")

            if user_choice == computer_choice:
                print("🤝 It's a Draw! Great minds think alike!")
            elif (user_choice == 1 and computer_choice == -1) or \
                 (user_choice == -1 and computer_choice == 0) or \
                 (user_choice == 0 and computer_choice == 1):
                print("🎉 You Win! Hurray!")
            else:
                print("😢 You Lose! Better luck next time!")

        except Exception as e:
            print(f"🚫 Unexpected error occurred: {e}")

game()
