#!/usr/bin/python3
"""defines a module contains the
entry point of the command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """A class inherit from Cmd class"""
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel, "User": User, "City": City,
            "Place": Place, "Amenity": Amenity, "Review": Review, "State": State}

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
        if (arg):
            if (arg not in HBNBCommand.classes):
                print("** class doesn't exist **")
            else:
                for k, v in HBNBCommand.classes.items():
                    if (k == arg):
                        my_model = v()
                        my_model.save()
                        print(my_model.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if (args):
            cmd_args = args.split(' ')
            if (cmd_args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
                return

            if (len(cmd_args) == 1):
                print("** instance id missing **")
                return

            json_file_key = cmd_args[0] + '.' + cmd_args[1]

            try:
                print(storage.all()[json_file_key])
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        if (args):
            cmd_args = args.split(' ')
            if (cmd_args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
                return

            if (len(cmd_args) == 1):
                print("** instance id missing **")
                return

            json_file_key = cmd_args[0] + '.' + cmd_args[1]
            try:
                del_obj_key = json_file_key
                del storage.all()[del_obj_key]
                storage.save()
            except KeyError:
                print("** no instance found **")

        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        all_objs = []

        if (arg):
            if (arg in HBNBCommand.classes):
                for k, v in storage.all().items():
                    cls_name = k.split(".")[0]
                    if (cls_name == arg):
                        all_objs.append(str(v))
            else:
                print("** class doesn't exist **")
                return

        else:
            for k, v in storage.all().items():
                all_objs.append(str(v))
        print(all_objs)

    def precmd(self, line):
        """donn't forget documentaion"""

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
