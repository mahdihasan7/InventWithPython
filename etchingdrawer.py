import shutil, sys

UP_DOWN_CHAR            = chr(9474)
LEFT_RIGHT_CHAR         = chr(9472)
DOWN_RIGHT_CHAR         = chr(9484)
DOWN_LEFT_CHAR          = chr(9488)
UP_RIGHT_CHAR           = chr(9492)
UP_LEFT_CHAR            = chr(9496)
UP_DOWN_RIGHT_CHAR      = chr(9500)
UP_DOWN_LEFT_CHAR       = chr(9508)
DOWN_LEFT_RIGHT_CHAR    = chr(9516)
UP_LEFT_RIGHT_CHAR      = chr(9524)
CROSS_CHAR              = chr(9532)

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newLine automatically, so reduce the width by one:
CANVAS_WIDTH -= 1
# Leave room at the bottom few rows for the command info lines.
CANVAS_HEIGHT -= 5


def getCanvasString(canvasData, cx, cy):
    canvasStr = ''

    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # Add the line character for this point to canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'
    return canvasStr
def main():

    canvas = {}
    cursorX = 0
    cursorY = 0
    moves = []

    while True:
        print(getCanvasString(canvas, cursorX, cursorY))
        
        print('WASD keys to move, H for help, C to clear, '
              + 'F to save, or QUIT.')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif response == 'H':
            print('''
            Enter a W, A, S, and D characters to move the cursor and
            draw a line behind it as it moves. For example, ddd
            draws a line going right and sssdddwwwaaa draws a box.
            ''')
            print('You can save your drawing to a text file by entering F.')
            input('Press Enter to return to the program...')
            continue
        elif response == 'C':
            canvas = {}
            cursorX = 0
            cursorY = 0
            moves.append('C')
            continue
        elif response == 'F':
            try:
                print('Enter filename to save to:')
                filename = input('> ')

                # Make sure the filename ends with .txt:
                if not filename.endswith('.txt'):
                    filename += '.txt'
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(''.join(moves) + '\n')
                    file.write(getCanvasString(canvas, None,None))
                print(f'Drawing saved to {filename}')
            except Exception as e:
                print(f'ERROR: Could not save file. Details: {e}')
            continue

        for command in response:
            if command not in ('W', 'A', 'S', 'D'):
                continue
            moves.append(command)

            # Initialize the first point in canvas
            if (cursorX, cursorY) not in canvas:
                canvas[(cursorX, cursorY)] = set()

            # Update canvas and cursor based on movement
            if command == 'W' and cursorY > 0:
                canvas[(cursorX, cursorY)].add(command)
                canvas[(cursorX, cursorY)].add('S')
                cursorY -= 1
            elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
                canvas[(cursorX, cursorY)].add(command)
                canvas[(cursorX, cursorY)].add('W')
                cursorY += 1
            elif command == 'A' and cursorX > 0:
                canvas[(cursorX, cursorY)].add(command)
                canvas[(cursorX, cursorY)].add('D')
                cursorX -= 1
            elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
                canvas[(cursorX, cursorY)].add(command)
                canvas[(cursorX, cursorY)].add('A')
                cursorX += 1
            
            # Ensure new cursor poistion is in canvas
            if (cursorX, cursorY) not in canvas:
                canvas[(cursorX, cursorY)] = set()

if __name__ == "__main__":
    main()
