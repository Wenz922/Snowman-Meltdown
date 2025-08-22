import game_logic


if __name__ == "__main__":
    while True:
        game_logic.play_game()
        replay_option = input("Play again (y/n)?: ").lower().strip()
        if replay_option != "y":
            print("Thanks for playing Snowman Meltdown!")
            break
