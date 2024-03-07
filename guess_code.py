from random import randint

def generate_code():
    code = [str(randint(0, 9)) for _ in range(4)]
    return "".join(code)

def input_number():
    while True:
        guess = input('Enter your variant: ')
        if len(guess) != 4 or not guess.isdigit():
            print('Please enter correct code')
            continue
        return guess

def check_guess(secret_number, guessed_number):
    bulls = sum(1 for s, g in zip(secret_number, guessed_number) if s == g)
    return bulls

# Пример использования
secret_number = generate_code()
# print("Secret number:", secret_number)
attempts = 0
while True:
    guessed_number = input_number()
    bulls = check_guess(secret_number, guessed_number)
    print(f"Bulls: {bulls}")
    attempts += 1
    if bulls == 4:
        print("You guessed the number!")
        print(f"ygadal za {attempts} popitok")
        break

a = input('do you wanna play again? ')