import random

def get_user_choice():
    user_choice = input("Select from Rock Paper or Scissor").strip().lower()
    while user_choice not in ["Rock","Paper","Scissor"]:
        print("Enter a valid choice between Rock Paper Scissor")
        user_choice = input("Select from Rock Paper or Scissor").strip().lower()
    return user_choice

def get_computer_choice():
    choice = ["Rock","Paper","Scissor"]
    random.choice(choice)

def winning_game(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie"
    elif user_choice == "Rock":
        return "You win!" if computer_choice == "Scissor" else print ("Computer Wins!")
    elif user_choice == "Paper":
        return "You win !" if computer_choice == "Rock" else print ("Computer Wins!")
    elif user_choice == "Scissor":
        return "You win !"  if computer_choice == "Paper" else print ("Computer Wins!")    
    
def play_game():
    print("Welcome Rock Paper or Scissor")

while True:
    User_Choice = get_user_choice
    Computer_choice = get_computer_choice
    print(f"You chose {User_Choice}")
    print(f"Computer choose {Computer_choice}")

    result = winning_game(get_user_choice,get_computer_choice)
    
    print(result)

    play_again = input(print("Do you want to continue playing or not Y/N")).strip().lower()
    if  play_again != "Y":
        print("Thanks for playing")
        break

if __name__ ==  "__main__":
    play_game()
