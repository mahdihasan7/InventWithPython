import random, shutil, sys, time

PAUSE = 0.2
DENSITY = 0.10

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newLine automatically, so reduce the width by one:
WIDTH -= 1

def main():
    print('Duckling Screensaver')
    print('Press CTRl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # See if we should create a ducklling in this lane:
            if (ducklingObj == None and random.random() <= DENSITY):
                # Place a duckling in this lane:
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Draw a duckling if there is one in this lane:
                print(ducklingObj.getNextBodyPart(), end='')
                # Delete the duckling if we've finished drawing it:
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # Draw five spaces since there is no duckling here.
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # Chubby ducklings can only have beady eyes.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        headStr = ''
        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '

        if self.direction == RIGHT:
            headStr += ' ('

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            headStr += ' '

    def getBodyStr(self):
        bodyStr = '('
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'

        if self.body == CHUBBY:
            bodyStr += ' '

            return bodyStr
    
    def getFeetStr(self):
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '
    
    def getNextBodyPart(self):
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
