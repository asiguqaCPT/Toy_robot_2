
x = 0
y = 0
robot_name =''
command = ''
direction = 0
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
            move_forward()
            continue
        elif 'back' in command.lower():
            move_back()
            continue
        elif 'sprint' in command.lower():
            sprint()
            continue
        elif 'right' in command.lower():
            move_right()
            print(' > ' + robot_name + ' turned right.')
            print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
            continue
        elif 'left' in command.lower():
            move_left()
            print(' > ' + robot_name + ' turned left.')
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
    global x
    if ' ' in command:
        new_command = command.split(' ')
        if direction == 0:
            y += int(new_command[1])
            if y > 200 or y < -200:
                y -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 1:
            x += int(new_command[1])
            if x > 100 or x < -100:
                x -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 2:
            y -= int(new_command[1])
            if y > 200 or y < -200:
                y += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 3:
            x -= int(new_command[1])
            if x > 100 or x < -100:
                x += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        
def move_back():
    global y
    global x
    if ' ' in command:
        new_command = command.split(' ')
        if direction == 0:
            y -= int(new_command[1])
            if y > 200 or y < -200:
                y += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved back by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 1:
            x -= int(new_command[1])
            if x > 100 or x < -100:
                x += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved back by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 2:
            y += int(new_command[1])
            if y > 200 or y < -200:
                y -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved back by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
        elif direction == 3:
            x += int(new_command[1])
            if x > 100 or x < -100:
                x -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return
            else:
                print(' > ' + robot_name + ' moved back by ' + new_command[1] + ' steps.')
                print(' > ' + robot_name + ' now at position ' + str(track_position()).replace(' ','') + '.')
                return

def sprint(num):
    

def move_forward_2():
    global y
    global x
    if ' ' in command:
        new_command = command.split(' ')
        if direction == 0:
            y += int(new_command[1])
            if y > 200 or y < -200:
                y -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                return
        elif direction == 1:
            x += int(new_command[1])
            if x > 100 or x < -100:
                x -= int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                return
        elif direction == 2:
            y -= int(new_command[1])
            if y > 200 or y < -200:
                y += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                return
        elif direction == 3:
            x -= int(new_command[1])
            if x > 100 or x < -100:
                x += int(new_command[1])
                print(robot_name + ': Sorry, I cannot go outside my safe zone.')
                return
            else:
                print(' > ' + robot_name + ' moved forward by ' + new_command[1] + ' steps.')
                return

    
def move_right():
    global direction
    if direction < 3:
        direction += 1
    else:
        direction = 0

def move_left():
    global direction
    if direction > 0:
        direction -= 1
    else:
        direction = 3

def track_position():
    global x
    global y
    return x,y

def help_command():
    print('I can understand these commands:')
    print('OFF  - Shut down robot')
    print('HELP - provide information about commands')
    print('FORWARD - move robot forward')
    print('BACK - move robot backwards')
    print('RIGHT - move robot right')
    print('SPRINT - give robot extra speed')
    print()

def robot_start():
    """This is the entry function, do not change"""
    global x, y, robot_name, command, direction
    x = 0
    y = 0
    robot_name =''
    command = ''
    direction = 0
    
    provide_name()
    on_off()

if __name__ == "__main__":
    robot_start()
