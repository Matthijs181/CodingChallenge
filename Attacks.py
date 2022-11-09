import random


class Attack:
    """
    Attack class which stores an attack with its specifications (damage and hit chance) and resulting attack
    """
    def __init__(self, name, damage, hit_chance):
        """
        Initializer of the attack class
        @param name: The name of the attack
        @param damage: The amount of damage the attack does
        @param hit_chance: The chance of the attack being a hit (in percentages)
        """
        self.name = name
        self.damage = damage
        self.hit_chance = hit_chance

    def attack(self):
        """
        Initiates the attack by determining if the attack is a hit or miss
        @return:
        """
        rnd_value = random.randint(0,100)
        if rnd_value < self.hit_chance:
            return self.damage  # A hit equals to the attack damage
        return 0  # A missed attack equals 0 damage

    def __str__(self):
        """
        String overwrite that prints the name, damage and hit chance of the attack
        @return: A formatted string to display name, damage and hit chance
        """
        return f"{self.name}: Damage: {self.damage}, hit chance = {self.hit_chance}\n"


class Attacks:
    """
    A class that stores multiple attacks and can create a random list of attacks from it
    """
    def __init__(self):
        """
        Initializer of the attack class that makes a set of attacks
        """
        self.attacks = {
            Attack("attack1", 10, 100),
            Attack("attack2", 20, 100),
            Attack("attack3", 30, 80),
            Attack("attack4", 40, 80),
            Attack("attack5", 50, 60),
            Attack("attack6", 60, 60),
            Attack("attack7", 70, 40),
            Attack("attack8", 80, 40)
        }

    def create_random_attackset(self,n_attacks):
        """
        Creates a random list of attacks of a given amount
        @param n_attacks: The amount of attacks to make
        @return: A random list of attacks with a length of n_attacks
        """
        rnd_attacks = random.choices([*self.attacks], k=n_attacks)
        return rnd_attacks
