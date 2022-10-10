import random


class GuessNumber:
    def __init__(self):
        self.random_number = 0
        self.max_value = 100
        self.min_value = 1
        self.attempt = True

    def start(self):
        self.generate_random_number()
        self.ask_random_value()

        try:
            while self.attempt:
                if self.random_value_guess > self.random_number:
                    print('guess a lower value')
                    self.ask_random_value()
                elif self.random_value_guess < self.random_number:
                    print('guess a higher value')
                    self.ask_random_value()
                elif self.random_value_guess == self.random_number:
                    self.attempt = False
                    print('congratulations, you got it right!')
        except:
            print('Ops, something is wrong :( ')
            self.ask_random_value()

    def ask_random_value(self):
        self.random_value_guess = int(input('Guess a Number: '))

    def generate_random_number(self):
        self.random_number = random.randint(self.min_value, self.max_value)


guess = GuessNumber()
guess.start()
