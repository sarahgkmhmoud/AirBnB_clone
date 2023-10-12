#!/usr/bin/python3
"""defines a module contains the
entry point of the command interpreter"""
import cmd
from engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


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

    def do_create(self, arg):
        """Creates a new instance save it to JSON file prints its id"""
        classes = {"BaseModel": BaseModel, "User": User, "City": City, "Place": Place,
                "Amenity": Amenity, "Review": Review, "State": State}
        for k, v in classes.items():
            if (k == arg):
                my_model = v()
                print(my_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        pass

    def precmd(self, line):
        """donn't forget documentaion"""
        obj_commands = ["show"]
        classes = ["BaseModel", "User", "City", "Place", "Amenity", "Review", "State"]
        args = line.split(' ')
        if (args[0] == "create"):
            if (len(args) < 2):
                print("** class name missing **")
            elif (args[1] not in classes):
                print("** class doesn't exist **")

        elif (args[0] in obj_commands):
            if (len(args) < 2):
                print("** class name missing **")
            elif (len(args) == 2):
                if (args[1] not in classes):
                     print("** class doesn't exist **")
                else:
                    print("** instance id missing **")

            elif (len(args) >= 2 and args[1] not in classes):
                print("** class doesn't exist **")

        return cmd.Cmd.precmd(self, line)

    def default(self, line):
        """documentation"""
        print("you've entered wrong command")
        return cmd.Cmd.default(self, line)

    def postcmd(self, stop, line):
        """documentation"""
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
