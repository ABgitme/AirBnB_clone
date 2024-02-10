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
        """Updates an instance based on the class name and id by adding or updating attribute."""
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
        elif len(args) < 3:
            print(HBNBCommand.ERROR_ATTR_MIS)
            return
        elif len(args) < 4:
            print(HBNBCommand.ERROR_ATT_VALUE)
            return
        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all().keys():
            print(HBNBCommand.ERROR_NO_ID_FOUND)
            return

        attribute_name = args[2]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            return

        attribute_value_str = args[3]
        if len(attribute_value_str) < 1:
            print(HBNBCommand.ERROR_ATT_VALUE)
            return

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value_str)
        obj.save()

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
