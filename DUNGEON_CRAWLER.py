









def start_menu():
    print("===== DUNGEON EXPLORER =====")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("\nEnter your name: ")
            print(f"Welcome to Dungeon Explorer, {name}!")
            print("You must survive 10 rooms to escape!")
            print()
            # main menu needs to happen here
            break
        elif choice == 2:
            print("STILL WORKING ON LOADING FUNCTION")
            break
        elif choice == 3:
            print("Goodbye traveller, come back when you aren't afraid of the dungeon...")
            break
        else:
            print("Invalid Number.")


    


def main():
    start_menu()








if __name__ == "__main__":
    main()