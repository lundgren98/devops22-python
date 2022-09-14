class Person:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

class Player(Person):
    def __init__(self, name, birthyear, speed, agility, strength):
        super().__init__(name, birthyear)
        self.speed = speed
        self.agility = agility
        self.strength = strength

    def __str__(self):
        s = f'({self.name}, {self.birthyear}'
        for v, n in zip((self.speed, self.agility, self.strength),
                        ("speed","agility","strength")):
            s += f', {n}={v}'
        s += ')'
        return s

class Coach(Person):
    def __init__(self, name, birthyear, voice_level):
        super().__init__(name, birthyear)
        self.voice_level = voice_level

    def __str__(self):
        return f'({self.name}, {self.birthyear}, {self.voice_level})'

class Team:
    def __init__(self):
        self.coach = None
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def switch_coach(self, coach):
        self.coach = coach

    def __str__(self):
        player_string_list = [str(player) for player in self.players]
        return f'Coach: {self.coach}, Players: {player_string_list}'

if __name__ == '__main__':
    forenames = ['Lars','Sven','Anders','Johan','Erik',
                 'Per','Nils','Gustaf','Karl','Jan']
    surnames = list(map(lambda n : f'{n}sson', forenames))
    best_team = Team()

    from random import choice, randint
    def random_name():
        return " ".join((choice(forenames), choice(surnames)))

    for i in range(10):
        fullname = random_name()
        birthyear = randint(1980,2004)
        speed, agility, strength = (randint(1,10) for x in range(3))
        player = Player(fullname, birthyear, speed, agility, strength)
        best_team.add_player(player)

    coach = Coach(random_name(), randint(1970,1995), randint(1,10))
    best_team.switch_coach(coach)
    print(f'{best_team}')
