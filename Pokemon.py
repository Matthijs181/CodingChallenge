from Attacks import Attacks


class Pokemon:
    """
    Parent class of the pokemon
    """
    def __init__(self, name, max_health, attacks):
        """
        Initializer of the pokemon parent class
        @param name: The name of the pokemon
        @param max_health: The maximum health of the pokemon
        @param attacks: A list of attacks that the pokemon can perform
        """
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attacks = attacks

    def __str__(self):
        """
        String overwrite to display the pokemon name, health and attacks
        @return: A formatted string to display the pokemon details
        """
        attacks_str = ''.join(["| " + attack.__str__() for attack in self.attacks])
        return f"| ==========================================\n"\
               f"| {self.name}\n" \
               f"| Health: {self.health}/{self.max_health}\n" \
               f"| ------------------------------------------\n"\
               f"| Attacks:\n{attacks_str}"\
               f"| ==========================================\n"

    def print_attacks(self):
        """
        Prints a list of the attacks of this pokemon
        @return: -
        """
        print(''.join([f"({i}) " + attack.__str__() for i, attack in enumerate(self.attacks)]))

    def receive_damage(self, incoming_attack):
        """
        Handle the damage of an incoming attack on the pokemon by adjusting its health
        @param incoming_attack: The attack that is performed by the other pokemon
        @return: The damage that was applied to the pokemon
        """
        damage = incoming_attack.attack()
        self.health -= damage
        return damage


# Child classes to generate different pokemon
class Pokemon1(Pokemon):
    def __init__(self):
        super().__init__("pokemon1", 100, Attacks().create_random_attackset(2))


class Pokemon2(Pokemon):
    def __init__(self):
        super().__init__("pokemon2", 50, Attacks().create_random_attackset(4))


class Pokemon3(Pokemon):
    def __init__(self):
        super().__init__("pokemon3", 80, Attacks().create_random_attackset(3))


class Pokemon4(Pokemon):
    def __init__(self):
        super().__init__("pokemon4", 120, Attacks().create_random_attackset(1))


class Pokemon5(Pokemon):
    def __init__(self):
        super().__init__("pokemon5", 75, Attacks().create_random_attackset(4))
