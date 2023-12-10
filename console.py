#!/usr/bin/python3
"""Contains entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User}

    def do_create(self, args):
        """Creates a new instance"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split(" ")[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.classes[class_name]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        arguments = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)
        class_name = arguments[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            ClassName = HBNBCommand.classes[class_name]
            if len(arguments) == 1:
                print("** instance id missing **")
                return
            id = arguments[1].strip("\"")
            key = f"{class_name}.{id}"
            retrieved_instances = storage.all()
            instance = retrieved_instances.get(key)
            if not instance:
                print("** no instance found **")
                return
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arguments = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)
        class_name = arguments[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            ClassName = HBNBCommand.classes[class_name]
            if len(arguments) == 1:
                print("** instance id missing **")
                return
            id = arguments[1].strip("\"")
            key = f"{class_name}.{id}"
            retrieved_instances = storage.all()
            value = retrieved_instances.pop(key, None)
            if not value:
                print("** no instance found **")
                return
            value.save()

    def do_all(self, arg):
        """Prints the string representation of all instances"""
        all = []
        if arg:
            class_name = arg.split(" ")[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

        retrieved_instances = storage.all()
        for value in retrieved_instances.values():
            all.append(str(value))
        if all:
            print(all)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arguments = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', arg)
        class_name = arguments[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        id = arguments[1].strip("\"")
        key = f"{class_name}.{id}"
        retrieved_instances = storage.all()
        instance = retrieved_instances.get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(arguments) == 2:
            print("** attribute name missing **")
            return
        attr_name = arguments[2]
        if len(arguments) == 3:
            print("** value missing **")
            return
        attribute = " ".join(arguments[3:]).strip("\"")
        try:
            attribute = int(attribute)
        except ValueError:
            try:
                attribute = float(attribute)
            except ValueError:
                pass
        setattr(instance, attr_name, attribute)
        instance.save()

    def emptyline(self):
        """Don't execute anything with empty line + ENTER"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the cmd"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
