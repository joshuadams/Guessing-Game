import random
randomNumber = random.randint(0,10)

gameMax = 4
guess = 10.5
while guess != randomNumber and gameMax >= 1:
  guess = input('Pick a number between 0-10')
  guess = int(guess)


  if guess < randomNumber:
    print('Guess is too small')
    gameMax = gameMax - 1
    print('You have ' + str(gameMax) + " tries left")
  elif guess > randomNumber:
    print('Guess is too large')
    gameMax = gameMax - 1
    print('You have ' + str(gameMax) + " tries left")
  else:
    print('Guess is correct! Congrats! You won!')
  if gameMax == 0:
    print('Darn! You lost!')
