#!/usr/bin/python3
"""defines a module contains the
entry point of the command interpreter"""
import cmd
from uuid import uuid4
from datetime import datetime
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
               "Place": Place, "Amenity": Amenity, "Review": Review,
               "State": State}

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

            if (json_file_key in storage.all()):
                print(storage.all()[json_file_key])
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

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

            if (json_file_key in storage.all()):
                del storage.all()[json_file_key]
                storage.save()
            else:
                print("** no instance found **")
                return

        else:
            print("** class name missing **")
            return

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

    def do_update(self, args):
        """ Updates an instance based on the class name and
        id by adding or updating attribute"""
        if (args):
            cmd_args = args.split(' ')
            if (cmd_args[0] not in HBNBCommand.classes):
                print("** class doesn't exist **")
                return

            if (len(cmd_args) == 1):
                print("** instance id missing **")
                return

            if (len(cmd_args) == 2):
                print("** attribute name missing **")
                return

            if (len(cmd_args) == 3):
                print("** value missing **")
                return
            objs_dict_key = cmd_args[0] + '.' + cmd_args[1]
            storage_dict = storage.all()
            if (objs_dict_key not in storage_dict.keys()):
                print("** no instance found **")
            else:
                obj = storage_dict[objs_dict_key]
                obj_dict = obj.__dict__
                attribute_name = cmd_args[2]
                attribute_value = cmd_args[3]
                if attribute_name in obj_dict:
                    obj_dict[attribute_name] = (type(obj_dict[attribute_name]))
                    (attribute_value)
                else:
                    obj_dict[attribute_name] = eval(attribute_value)
                storage.save()
        else:
            print("** class name missing **")

    def do_count(self, arg):
        """ retrieve the number of instances of a class"""
        count = 0
        if (arg in HBNBCommand.classes):
            for k, v in storage.all().items():
                cls_name = k.split(".")[0]
                if (cls_name == arg):
                    count += 1
        print(count)

    def precmd(self, line):
        """parsing the command before execution"""
        if ("." in line and "(" in line and ")" in line):
            parse_line = line.split(".")
            class_name = parse_line[0]
            parse2 = parse_line[1].split("(")
            command = parse2[0]
            parse3 = parse2[1].split(")")
            obj_id = parse3[0]
            command_line = command + " " + class_name + " " + obj_id
            return command_line
        else:
            return line

    def default(self, line):
        """default function"""
        return cmd.Cmd.default(self, line)

    def postcmd(self, stop, line):
        """documentation"""
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
