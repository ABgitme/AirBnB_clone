#!/usr/bin/python3
"""HBNB Command Line Interface

This module provides a command-line interface (CLI) for
managing instances of various classes in the HBNB application.
It allows users to create, show, update,
and delete instances of specified classes.

Classes:
    HBNBCommand: A command-line interpreter that
    accepts user input and executes corresponding commands.

"""
import cmd
import models
import importlib
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNB Command Line Interface

    A command-line interpreter that accepts
    user input and executes corresponding commands.
    The commands include creating, showing, updating,
    and deleting instances of specified classes.

    Attributes:
        valid_classes (dict): A dictionary containing valid class
            names as keys and corresponding class references.
        ERROR_ATT_VALUE (str): Error message for missing attribute value.
        ERROR_NO_ID_FOUND (str): Error message for no instance found.
        ERROR_CLASS_NOT_EXIST (str): Error message for non-existent class.
        ERROR_ID (str): Error message for missing instance id.
        ERROR_CLASS_NAME_MIS (str): Error message for missing class name.
        ERROR_ATTR_MIS (str): Error message for missing attribute name.
        prompt (str): Prompt string for the command line interface.
    """
    valid_classes = {
        'BaseModel': BaseModel, 'User': User,
        'Amenity': Amenity, 'City': City, 'State': State,
        'Place': Place, 'Review': Review
    }

    ERROR_ATT_VALUE = "** value missing **"
    ERROR_NO_ID_FOUND = "** no instance found **"
    ERROR_CLASS_NOT_EXIST = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_CLASS_NAME_MIS = '** class name missing **'
    ERROR_ATTR_MIS = "** attribute name missing **"
    ERROR_SYNTAX = "** syntax error **"

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit the program.")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def help_emptyline(self):
        print("Does nothing on empty input.")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""

        args = self.Parser(arg)
        if len(args) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME_MIS)
            return
        class_name = args[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return

        new_instance = HBNBCommand.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        print("Creates a new instance of a model\
                and saves it to the database.")
        print("Usage: create <class name>")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = self.Parser(arg)
        if len(args) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME_MIS)
            return
        elif len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return
        elif args[0] not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print(HBNBCommand.ERROR_NO_ID_FOUND)
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = self.Parser(arg)
        if len(args) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME_MIS)
            return
        elif len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print(HBNBCommand.ERROR_NO_ID_FOUND)
        else:
            del storage.all()[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = self.Parser(arg)
        if not args:
            # If no arguments provided, print all instances of all classes
            instances = []
            for obj_id, obj in storage.all().items():
                instances.append(str(obj))
            print(instances)
        elif args[0] in self.valid_classes:
            # If a valid class name is provided, print instances of that class
            instances = []
            for obj_id, obj in storage.all().items():
                class_name = obj.__class__.__name__
                if class_name == args[0]:
                    instances.append(str(obj))
            print(instances)
        else:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute."""
        args = self.Parser(arg)
        if not args:
            print(HBNBCommand.ERROR_CLASS_NAME_MIS)
            return
        elif args[0] not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return
        elif len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key not in storage.all().keys():
                print(HBNBCommand.ERROR_NO_ID_FOUND)
            elif len(args) < 3:
                print(HBNBCommand.ERROR_ATTR_MIS)
            elif len(args) < 4 or len(args[3]) < 1:
                print(HBNBCommand.ERROR_ATT_VALUE)
            else:
                attribute_name = args[2]
                if attribute_name in ['id', 'created_at', 'updated_at']:
                    return
                attribute_value_str = args[3]
                obj = storage.all()[key]
                setattr(obj, attribute_name, attribute_value_str)
                obj.save()

    def help_update(self):
        print("Updates an instance based on the class\
                name and id by adding or updating attribute.")
        print("Usage: update <class name> <id>\
                <attribute name> <attribute value>")

    def Parser(self, arg):
        """tokenize and Counts the number of arguments passed to the console.

        Args:
            arg: The raw input string from the console.

        Returns:
            The number of arguments, excluding the command itself.
        """
        commads = shlex.split(arg)
        return commads

    def default(self, arg):
        """ handle the default behaviour of the command module"""
        args = arg.split('.')
        method_args = []
        if len(args) != 2:
            print(HBNBCommand.ERROR_SYNTAX)
            return False

        class_name, method_str = args
        method_name = method_str.split('(')
        if method_name[0] in ['show', 'destroy', 'update']:
            if len(method_name) > 1:
                method_args = method_name[1].strip(')').split(',')
                method_args = [
                    argval.strip().strip('"') for argval in method_args
                ]

        method_dict = {
            'update': self.do_update,
            'destroy': self.do_destroy,
            'show': self.do_show,
            'all': self.do_all,
            'count': self.do_count
        }

        method = method_dict.get(method_name[0])
        if method:
            if method_args:
                return method(f"{class_name} {' '.join(method_args)}")
            else:
                return method(f"{class_name} {''}")

        print(HBNBCommand.ERROR_SYNTAX)
        return False

    def do_count(self, arg):
        """counts the number of objects"""
        command = shlex.split(arg)
        if command[0] in self.valid_classes:
            count = 0
            for obj_key, obj in storage.all().items():
                class_name = obj_key.split('.')[0]
                if class_name == command[0]:
                    count += 1
            print(count)
        else:
            print(HBNBCommand.ERROR_SYNTAX)
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
