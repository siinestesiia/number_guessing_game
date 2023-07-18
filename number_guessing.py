''' Number guessing game '''
from random import randint

class NumberGuessing:
    def __init__(self):
        self.number = randint(1, 10)
        self.counter = 0
        self.greet_user()
        self.user_guess()

    def greet_user(self):
        greetings = '\t-- Welcome to the number guessing game --\n'.upper()
        greetings += 'You have to guess the secret number between 1 and 10. '
        greetings += 'You only have 3 chances. Good luck!\n'
        print(greetings)

    def user_guess(self):
        while self.counter != 3:
            print(f'Chances remaining: {3 - self.counter}.')    
            guess = input('Guess the number: ')
            self.counter += 1
            
            if int(guess) == int(self.number):
                print('Congratulations, you won!!')
                self.counter = 3
            elif int(guess) != self.number and self.counter != 3:
                print('Wrong number! Guess again.')
            elif int(guess) != self.number and self.counter == 3:
                print('Gamer Over!'.upper())
                print(f'\nThe secret number was: {self.number}')


game = NumberGuessing()
