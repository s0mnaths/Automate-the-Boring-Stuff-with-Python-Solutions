import logging,random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Program Start')
guess = ''

while guess not in ('heads', 'tails'):
    logging.debug('While loop start: input guess')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Coin tossed-randint used')
if toss==0:
    toss='tails'
else:
    toss='heads'
logging.debug('Toss result: ' + str(toss) + ' Your guess: ' + str(guess))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Toss result: ' + str(toss) + ' Your guess: ' + str(guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')