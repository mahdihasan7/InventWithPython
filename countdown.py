import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        # Clear the screen by printing several newLines:
        print('\n' * 60)

        # Get the hours/minutes/seconds from secondsLeft:
        # 7265 is 2 Hours:
        hours = str(secondsLeft // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopRow    + '   ' + mTopRow    + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1) # Insert a one-second pause.
        secondsLeft -= 1

except KeyboardInterrupt:
    print('Countdown')
    sys.exit() # When Ctrl-C is pressed, end the program.
