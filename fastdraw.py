import random, sys, time

print('''
Fast Draw,

Time to test your reflexes and see if you are the fastest
draw in the west!!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears

Press Enter to begin...
''')

while True:
    print('\nIt is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # If the player pressed enter before DRAW! appearred, the input()
        # call returns almost instantly.
        print('You draw before "DRAW" appeared! You lose.')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. You win!')
        print('You are the fastest draw in the west! You win!')

    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response.startswith('Q'):
        print("Thanks for playing!")
        sys.exit()
