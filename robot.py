
x = 0
y = 0
robot_name =''
command = ''
def provide_name():
    """Let's the child provide a name for the robot"""
    global robot_name
    robot_name = input('What do you want to name your robot? ')
    print(robot_name + ': Hello kiddo!')

def on_off():
    """Allows the child turn the robot on or off"""
    global robot_name
    global command
    while True:
        command = input(robot_name + ": What must I do next? ")
        if command.lower() == 'help':
            help_command()
            continue
        elif 'forward' in command.lower():
            print(' > ' + robot_name + ' moved forward by ' + str(move_forward()) + ' steps.')
            print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
            continue
        elif command.lower() == 'off':
            print(robot_name + ': Shutting down..')
            break
        else:
            print(robot_name + ': Sorry, I did not understand ' + '\''+ command + '\'.')
            continue
def move_forward():
    global y
    if ' ' in command:
        new_command = command.split(' ')
        y += int(new_command[1])
        return int(new_command[1])
    pass

def track_position():
    global x
    global y

    return x,y
def help_command():
    print('I can understand these commands:')
    print('OFF  - Shut down robot')
    print('HELP - provide information about commands')
    print('FORWARD - move robot forward')
    print()

def robot_start():
    """This is the entry function, do not change"""
    provide_name()
    on_off()
if __name__ == "__main__":
    robot_start()
