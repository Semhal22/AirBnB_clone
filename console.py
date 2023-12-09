#!/usr/bin/python3
"""Contains entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Don't execute anything with empty line + ENTER"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the cmd"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
