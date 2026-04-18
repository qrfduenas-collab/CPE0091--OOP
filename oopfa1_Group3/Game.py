import random
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

def choose_class(name):
    print(name + ", choose your class:")
    print("1. Swordsman")
    print("2. Archer")
    print("3. Magician")

    choice = input("Enter choice: ")

    if choice == "1":
        return Swordsman(name)
    elif choice == "2":
        return Archer(name)
    elif choice == "3":
        return Magician(name)
    else:
        print("Invalid choice, default is Swordsman")
        return Swordsman(name)

def show_hp(p1, p2):
    print("\n--- HP STATUS ---")
    print(p1.getUsername() + " HP: " + str(p1.getHp()))
    print(p2.getUsername() + " HP: " + str(p2.getHp()))
    print("-----------------\n")

def attack(player, opponent):
    print("\n" + player.getUsername() + "'s turn!")
    print("Choose your action:")

    options = []

    if hasattr(player, "basicAttack"):
        options.append("1. Basic Attack")
    if hasattr(player, "slashAttack"):
        options.append("2. Slash Attack")
    if hasattr(player, "rangedAttack"):
        options.append("3. Ranged Attack")
    if hasattr(player, "magicAttack"):
        options.append("4. Magic Attack")

    for opt in options:
        print(opt)

    choice = input("Enter choice: ")

    if choice == "1" and hasattr(player, "basicAttack"):
        player.basicAttack(opponent)

    elif choice == "2" and hasattr(player, "slashAttack"):
        player.slashAttack(opponent)

    elif choice == "3" and hasattr(player, "rangedAttack"):
        player.rangedAttack(opponent)

    elif choice == "4" and hasattr(player, "magicAttack"):
        player.magicAttack(opponent)

    else:
        print("Invalid choice! Default attack used.")
        if hasattr(player, "basicAttack"):
            player.basicAttack(opponent)

def game(p1, p2):
    while p1.getHp() > 0 and p2.getHp() > 0:
        attack(p1, p2)
        if p2.getHp() <= 0:
            break

        attack(p2, p1)
        show_hp(p1, p2)

    if p1.getHp() > 0:
        print(p1.getUsername() + " wins!")
        return 1
    else:
        print(p2.getUsername() + " wins!")
        return 2

def main():
    wins1 = 0
    wins2 = 0

    while True:
        print("\n=== MENU ===")
        print("1. Single Player")
        print("2. Player vs Player")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            player1 = choose_class("Player")
            player2 = Boss("Monster")

        elif choice == "2":
            player1 = choose_class("Player 1")
            player2 = choose_class("Player 2")

        elif choice == "3":
            print("Exiting game...")
            break

        else:
            print("Invalid choice")
            continue

        result = game(player1, player2)

        if result == 1:
            wins1 += 1
        else:
            wins2 += 1

        print("\n=== SCORE ===")
        print("Player 1 Wins:", wins1)
        print("Player 2 Wins:", wins2)

        again = input("Play again? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    main()