

def main():
    print('\n Started the To-Do Application \n')
    while (1):
        command = input('$ ')
        
        # command type, command name, command args
        # Split the string seperated by space
        command_type= command.split()[0]
        command_name, command_args = parse(command)
        
        if (command_name == 'quit'):
            break

        elif (command_name == 'invalid'):
            print('Please enter a valid command') 

        elif (command_name == 'use'):
            #

        elif (command_type == 'todo'):
            #

        else:
            #



if __name__== '__main__':
    main()