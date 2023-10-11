#!/usr/bin/python3
"""defines a module contains the
entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A class inherit from Cmd class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """override the method and shouldn't execute any thing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
