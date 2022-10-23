
print('CHOOSE GAME')
print('hint: its a single digit greater than 5')
secret_number = 9
guess_count = 0
guess_limit = 3
# i used i priorly but then i after selecting i and
# right clicking i used 'refractor' to replace its name
while guess_count < guess_limit:
    guess = int(input('Guess: '))
# input interprets the value as a string ALWAYS so if we
# we want an integer value we NEED to put int usse pehle
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('oops you failed')

