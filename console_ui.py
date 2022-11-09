import random
import Pokemon
import copy


class GameUI:
    def __init__(self):
        """
        Initializer of the GameUI class.
        Initializes menu texts and player/opponent pokemon setups
        """
        self.menu_text = "Welcome to Pokemon Avonic!\n p - Play\n q - Quit\n"
        self.wrong_input_text = "That was not one of the given options. Please insert one of the given values.\n"
        self.select_pokemon_text = "Select a Pokemon\n n - Next Pokemon\n p - Previous Pokemon\n s - Select Pokemon\n"
        self.idle_pokemon_text = "Do you want to fight, reselect or quit?\n f - Fight\n" \
                                 " r - Reselect\n q - Quit to main menu\n"
        self.fight_pokemon_text = "Do you want to attack or switch pokemon?\n a - Attack\n s - Switch\n" \
                                  " dc - Details on current pokemon\n do - Details on opponent pokemon\n"
        self.attack_select_text = "Select the number of the attack you want to use\n"
        self.you_lost_text = "You lost the fight, returning to main menu\n"
        self.you_won_text = "You won the fight! returning to selection menu\n"

        self.pokemon = None
        self.opponents = None
        self.current_pokemon = None
        self.opponent_pokemon = None

    def start_game(self):
        """
        Presents the player with the main menu
        @return: -
        """
        self.reset_game()
        play_or_quit_in = input(self.menu_text)
        while play_or_quit_in.lower() not in ["p", "q"]:
            play_or_quit_in = input(self.wrong_input_text)

        if play_or_quit_in == 'p':
            self.current_pokemon = self.pokemon_select_menu(self.pokemon)
            self.pokemon_idle_menu()

        if play_or_quit_in == 'q':
            exit()

    def pokemon_select_menu(self, pokemon_list):
        """
        Presents the player with the pokemon select menu
        @param pokemon_list: the list of pokemon to select from
        @return: the selected pokemon
        """
        pokemon_idx = 0
        selecting = True
        selected_pokemon = None

        print(self.select_pokemon_text)
        print(pokemon_list[pokemon_idx])
        pokemon_select_in = input()

        while selecting:
            while pokemon_select_in.lower() not in ["n", "p", "s"]:
                pokemon_select_in = input(self.wrong_input_text)

            if pokemon_select_in == "s":
                selecting = False
                break

            if pokemon_select_in == "n":
                if pokemon_idx >= 4:
                    print("You have reached the last pokemon in the list")
                else:
                    pokemon_idx += 1

            if pokemon_select_in == "p":
                if pokemon_idx <= 0:
                    print("You have reached the first pokemon in the list")
                else:
                    pokemon_idx -= 1

            print(self.select_pokemon_text)
            print(pokemon_list[pokemon_idx])
            pokemon_select_in = input()

        selected_pokemon = pokemon_list[pokemon_idx]
        print(f"U selected:\n{selected_pokemon.name}!")
        return selected_pokemon

    def pokemon_idle_menu(self):
        """
        Presents the player with the intermediate menu to select a different pokemon, fight or quit
        @return: -
        """
        idle_menu_select = input(self.idle_pokemon_text)
        while idle_menu_select.lower() not in ["f", "r", "q"]:
            idle_menu_select = input(self.wrong_input_text)

        if idle_menu_select.lower() == "f":
            self.fight_menu()

        if idle_menu_select.lower() == "r":
            self.current_pokemon = self.pokemon_select_menu(self.pokemon)
            self.pokemon_idle_menu()

        if idle_menu_select.lower() == "q":
            self.start_game()

    def fight_menu(self):
        """
        Presents the player with the combat menu by selecting to attack, select a different pokemon or request details
        on the pokemon in battle.
        @return: -
        """
        # Create an independent copy so that the original list of opponents does not get adjusted
        self.opponent_pokemon = copy.deepcopy(self.pokemon_select_menu(self.opponents))
        fight_is_over = False
        won = False

        while not fight_is_over:
            fight_menu_select = input(self.fight_pokemon_text)
            while fight_menu_select.lower() not in ["a", "s", "dc", "do"]:
                fight_menu_select = input(self.wrong_input_text)

            if fight_menu_select.lower() == "dc":
                print(self.current_pokemon)
                continue

            if fight_menu_select.lower() == "do":
                print(self.opponent_pokemon)
                continue

            if fight_menu_select.lower() == "s":
                self.pokemon_select_menu(self.pokemon)

            if fight_menu_select.lower() == "a":
                self.player_attack()
                if self.health_below_zero(self.opponent_pokemon):
                    print(self.you_won_text)
                    won = True
                    break

            self.opponent_attack()
            if self.health_below_zero(self.current_pokemon):
                print(self.you_lost_text)
                break

        if won:
            self.pokemon_idle_menu()
        else:
            self.start_game()

    def player_attack(self):
        """
        Handles the attacks performed by the player by getting an attack from the player and applying the damage to the
        opponent. Followed by a feedback message of the attack
        @return:
        """
        print(self.attack_select_text)
        self.current_pokemon.print_attacks()
        attack_select_number = input()

        while not self.attack_input_is_int(attack_select_number):
            attack_select_number = input(self.wrong_input_text)
        attack_select_number = int(attack_select_number)
        received_damage = self.opponent_pokemon.receive_damage(self.current_pokemon.attacks[attack_select_number])
        if received_damage == 0:
            print(f"(Opponent) {self.opponent_pokemon.name} evaded the attack")
        else:
            print(f"(Opponent) {self.opponent_pokemon.name} was hit for {received_damage} points of damage")

    def opponent_attack(self):
        """
        Handles the attacks performed by the computer by selecting a random attack applying the damage to the player.
        Followed by a feedback message of the attack
        @return: -
        """
        attack_select_number = random.randint(0,len(self.opponent_pokemon.attacks)-1)
        received_damage = self.current_pokemon.receive_damage(self.opponent_pokemon.attacks[attack_select_number])
        if received_damage == 0:
            print(f"(Player) {self.current_pokemon.name} evaded the attack")
        else:
            print(f"(Player) {self.current_pokemon.name} was hit for {received_damage} points of damage")

    def attack_input_is_int(self, input):
        """
        Determine if the input is in integer format
        @param input: The console input
        @return:
        """
        try:
            val = int(input)
            if val > len(self.current_pokemon.attacks)-1:
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def health_below_zero(pokemon):
        """
        Checks if the pokemon has died
        @param pokemon: the pokemon to check
        @return: a boolean indicating if the pokemon is dead or not
        """
        return pokemon.health <= 0

    def reset_game(self):
        """
        Resets the game by intializing new player pokemon and opponents
        @return:
        """
        self.pokemon = [Pokemon.Pokemon1(), Pokemon.Pokemon2(), Pokemon.Pokemon3(),
                        Pokemon.Pokemon4(), Pokemon.Pokemon5()]
        self.opponents = [Pokemon.Pokemon1(), Pokemon.Pokemon2(), Pokemon.Pokemon3(),
                          Pokemon.Pokemon4(), Pokemon.Pokemon5()]
        self.current_pokemon = None
        self.opponent_pokemon = None
