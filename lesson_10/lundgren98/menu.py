class Menu:
    def __init__(self, commands):
        self.options = [o for o, f in commands]
        self.functions = [f for o, f in commands]

    def prompt(self):
        for i, o in enumerate(self.options):
            print(f'{i+1} {o}')
        try:
            i = int(input())
            if i < 0:
                raise IndexError
            self.functions[i-1]()
        except ValueError:
            print('Not an integer!')
            self.prompt()
        except IndexError:
            print('Not an option!')
            self.prompt()

    def run(self):
        while True:
            self.prompt()
