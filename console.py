#!/usr/bin/python3
"""Contains entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
               'City': City, 'Place': Place, 'Review': Review, 'State': State}

    def onecmd(self, line):
        """Execute multiple commands separated by a semicolon."""
        commands = line.split(';')
        for command in commands:
            if command:
                cmd.Cmd.onecmd(self, command.strip())
        return False

    def precmd(self, line):
        """Called before any do_ methods"""
        if '.all()' in line:
            return 'all ' + line.split('.')[0]
        elif '.count()' in line:
            return 'count ' + line.split('.')[0]
        elif '.show(' in line:
            id = line.split('.')[1][5:-1]
            return 'show ' + line.split('.')[0] + " " + id
        elif '.destroy(' in line:
            id = line.split('.')[1][8:-1]
            return 'destroy ' + line.split('.')[0] + " " + id
        elif '.update(' in line:
            class_name, second_args = line.split('.', 1)
            first, value = second_args.split(', ', 1)
            id = first[7:]
            dictionary = eval(value[:-1])
            if isinstance(dictionary, dict):
                commands = []
                for key, value in dictionary.items():
                    key = key.strip("\"")
                    commands.append(f"update {class_name} {id} {key} {value}")

                return ";".join(commands)
            else:
                first, attr_name, value = second_args.split(', ', 2)
                value = value[:-1]
                attr_name = attr_name.strip("\"")
                return f"update {class_name} {id} {attr_name} {value}"

        return line

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
            else:
                ClassName = HBNBCommand.classes[class_name]
                retrieved_instances = storage.all(ClassName)
                for obj in retrieved_instances.values():
                    all.append(str(obj))

                if all:
                    print(all)
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

    def do_count(self, arg):
        """Count the number of instances of a Class"""
        count = 0
        if arg:
            class_name = arg.split(" ")[0]
            if class_name in HBNBCommand.classes:
                ClassName = HBNBCommand.classes[class_name]
                retrieved_instances = storage.all(ClassName)
                count = len(retrieved_instances)
                print(count)

    def emptyline(self):
        """Don't execute anything with empty line + ENTER"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """Exit the cmd"""
        print()
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
