#!/usr/bin/python3
import cmd
import models
import importlib
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    valid_classes = {'BaseModel': BaseModel}
    ERROR_ATT_VALUE = "** value missing **"
    ERROR_NO_ID_FOUND = "** no instance found **"
    ERROR_CLASS_NOT_EXIST = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_CLASS_NAME_MIS = '** class name missing **'
    ERROR_ATTR_MIS = "** attribute name missing **"

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""

        args = self.Parser(arg)
        if not args[0]:
            print(HBNBCommand.ERROR_CLASS_NAME_MIS)
            return
        class_name = arg.split()[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return

        new_instance = HBNBCommand.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

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
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        objects = models.storage.all()

        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        class_name = args[0]

        try:
            # Check if the class exists in models.BaseModels.py
            module = importlib.import_module("models.BaseModels")
            getattr(module, class_name)  # Raise AttributeError if not found
        except (ModuleNotFoundError, AttributeError):
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        if args[0] not in models.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.save()

    def validate_class_name(self, arg):
        """Validates if the class_name argument is a valid class"""
        args = arg.split(' ')
        class_name = args[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS_NOT_EXIST)
            return False
        return class_name

    def Parser(self, arg):
        """tokenize and Counts the number of arguments passed to the console.

        Args:
            arg: The raw input string from the console.

        Returns:
            The number of arguments, excluding the command itself.
        """
        commads = shlex.split(arg)
        return commads
if __name__ == '__main__':
    HBNBCommand().cmdloop()
