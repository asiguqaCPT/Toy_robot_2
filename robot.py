
robot_name ='' 
def provide_name():
    """Let's the child provide a name for the robot"""
    global robot_name
    robot_name = input('What do you want to name your robot? ')
    print(robot_name + ': Hello kiddo!')

def on_off():
    """Allows the child turn the robot on or off"""
    global robot_name
    while True:
        command = input(robot_name + ": What must I do next? ")
        if command.lower() == 'help':
            help_command()
            continue
        elif command.lower() == 'forward':
            print('> ' + robot_name + 'moved forward by ' +move_forward() + ' steps.')
            continue
        elif command.lower() == 'off':
            print(robot_name + ': Shutting down..')
            break
        else:
            print(robot_name + ': Sorry, I did not understand ' + '\''+ command + '\'.')
            continue
def move_forward():
    

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
