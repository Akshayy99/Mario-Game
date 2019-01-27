'''
contains all the symbols, constants
directions, etc
'''

# ch repr of objects
_bricks = "X"
_enemy = "E"
_empty = " "

# types of objects
types = {
    _empty : "Unassigned",
    _bricks : "Bricks",
    _enemy : "Enemy",
}

UP, LEFT, RIGHT, QUIT = range(4)
DIR = [UP, LEFT, RIGHT]
INVALID = -1

# allowed inputs
_allowed_inputs = {
    UP      : ['w', '\x1b[A'], \
    LEFT    : ['a', '\x1b[D'], \
    RIGHT   : ['d', '\x1b[C'], \
    QUIT    : ['q']
}



# scaling and move factor
x_fac, y_fac = (2, 2)

def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return INVALID


# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()


    def __call__(self):
        return self.impl()


class _GetchUnix:


    def __init__(self):
        import tty, sys


    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt


    def __call__(self):
        import msvcrt
        return msvcrt.getch()


_getch = _Getch()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=1):
    import signal
    import select
    import sys
    signal.signal(signal.SIGALRM, alarmHandler)
    # signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL, 0.6, 0.6)
    try:
        text = _getch()
        # signal.alarm(0)
        signal.setitimer(signal.ITIMER_REAL, 0)

        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

# for printing colored people
colors = {
    'Black'            : '\x1b[0;30m',
    'Blue'             : '\x1b[0;34m',
    'Green'            : '\x1b[0;32m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Green'      : '\x1b[1;32m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m'
}

ENDC = '\x1b[0m'

castle = []

castle.append(list('                             -|             |-                                    '))
castle.append(list('         -|                  [-_-_-_-_-_-_-_-]                  |-                '))
castle.append(list('         [-_-_-_-_-]          |             |          [-_-_-_-_-]                '))
castle.append(list('          | o   o |           [  0   0   0  ]           | o   o |                 '))
castle.append(list('           |     |    -|       |           |       |-    |     |                  '))
castle.append(list('           |     |_-___-___-___-|         |-___-___-___-_|     |                  '))
castle.append(list('           |  o  ]              [    0    ]              [  o  |                  '))
castle.append(list('           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----___________  '))
castle.append(list('_____----- |     ]              [ ||||||| ]              [     |                  '))	
castle.append(list('           |     ]              [ ||||||| ]              [     |                  '))
castle.append(list('       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_-_-_-_-_-_    '))
castle.append(list('      ( (__________------------_____________-------------_________) )             '))


won = []

won.append(list('_____.___.________   ____ ___      __      __________    _______    ._. ._. ._. ._.'))
won.append(list('\\__  |   |\\_____  \\ |    |   \\    /  \\    /  \\_____  \\   \\      \\   | | | | | | | |'))
won.append(list(' /   |   | /   |   \\|    |   /    \\   \\/\\/   //   |   \\  /   |   \\  | | | | | | | |'))
won.append(list(' \\____   |/    |    \\    |  /      \\        //    |    \\/    |    \\  \\|  \\|  \\|  \\|'))
won.append(list(' / ______|\\_______  /______/        \\__/\\  / \\_______  /\\____|__  /  __  __  __  __'))
won.append(list(' \\/               \/                     \\/          \\/         \\/   \\/  \\/  \\/  \\/'))


lost = []

lost.append(list('  ________    _____      _____  ___________   ____________   _________________________   ._.'))
lost.append(list(' /  _____/   /  _  \\    /     \\ \\_   _____/   \\_____  \\   \\ /   /\\_   _____/\\______   \\  | |'))
lost.append(list('/   \\  ___  /  /_\\  \\  /  \\ /  \\ |    __)_     /   |   \\   Y   /  |    __)_  |       _/  | |'))
lost.append(list('\\    \\_\  \\/    |    \\/    Y    \\|        \\   /    |    \\     /   |        \\ |    |   \   \\|'))
lost.append(list(' \\______  /\\____|__  /\\____|__  /_______  /   \\_______  /\\___/   /_______  / |____|_  /   __'))
lost.append(list('        \\/         \\/         \\/        \\/            \\/                 \\/         \\/    \\ '))


