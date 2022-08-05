#!/usr/bin/python3
""" console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Representation entry point of the command interpreter."""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit(0)

    def help_quit(self):
        """ Help document to quit the program."""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Command to quit the program."""
        exit(0)

    def help_EOF(self):
        """ Help document to quit the program for EOF."""
    
    def emptyline(self):
        """ Empty line."""
        pass

    def handler(signal_received, frame):
        """Handle the SIGINT or CTRL-C signal."""
        print("^C")
        exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
