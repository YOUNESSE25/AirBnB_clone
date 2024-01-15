#!/usr/bin/python
"""
Console
"""
import cmd
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    class called console
    """
    prompt = "(hbnb) "
    classes_available = ["BaseModel", "User", "Amenity", "Place",
                         "Review", "State", "City"]

    def emptyline(self):
        """
        do nothing
        """
        pass

    def do_quit(self, arg):
        """
        exit the program
        """
        return True

    # aliasing
    do_EOF = do_quit

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        cmd = arg.split()

        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.classes_available:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{cmd[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id.
        """
        cmd = arg.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.classes_available:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmd[0], cmd[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        """
        cmd = arg.split()

        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.classes_available:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            k = "{}.{}".format(cmd[0], cmd[1])
            if k in objs:
                del objs[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
         Prints all string representation of all
         instances based or not on the class name
        """
        objs = storage.all()
        cmd = arg.split()
        if len(cmd) == 0:
            for key, value in objs.items():
                to_print1 = str(value)
                print(to_print1)
        elif cmd[0] not in self.classes_available:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == cmd[0]:
                    to_print2 = str(value)
                    print(to_print2)

    def do_update(self, arg):
        """
         Updates an instance based on the class name
         and id by adding or updating attribute
        """
        cmd = arg.split()
        if len(cmd) == 0:
            print("** class name missing **")
        elif cmd[0] not in self.classes_available:
            print("** class doesn't exist **")
        elif len(cmd) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(cmd[0], cmd[1])
            if key not in objs:
                print("** no instance found **")
            elif len(cmd) < 3:
                print("** attribute name missing **")
            elif len(cmd) < 4:
                print("** value missing **")
            else:
                CurlyBraces = re.search(r"\{(.*?)\}", arg)
                obj = objs[key]
                if CurlyBraces:
                    try:
                        dA = ast.literal_eval("{" + CurlyBraces.group(1) + "}")
                        namesAttrib = list(dA.keys())
                        valuesAttrib = list(dA.values())
                        try:
                            attrib_name1 = namesAttrib[0]
                            attrib_value1 = valuesAttrib[0]
                            setattr(obj, attrib_name1, attrib_value1)
                        except Exception:
                            pass
                        try:
                            attrib_name2 = namesAttrib[1]
                            attrib_value2 = valuesAttrib[1]
                            setattr(obj, attrib_name2, attrib_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    attrib_name = cmd[2]
                    attrib_value = cmd[3]
                    try:
                        attrib_value = eval(attrib_value)
                    except Exception:
                        pass
                    setattr(obj, attrib_name, attrib_value)
                    print(attrib_name, attrib_value)

                obj.save()

    def do_count(self, arg):
        """
        Counts class
        """
        objs = storage.all()
        argToCount = arg.split()
        classConteur = 0
        if argToCount:
            if argToCount[0] in self.classes_available:
                for obj in objs.values():
                    if obj.__class__.__name__ == argToCount[0]:
                        classConteur += 1
                print(classConteur)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def default(self, arg):
        """ <class name>.method() """

        dictSplitPoint = arg.split('.')
        cls_nm = dictSplitPoint[0]
        commande = dictSplitPoint[1].split('(')
        cmd_met = commande[0]
        idParam = commande[1].split(')')[0]
        method_dict = {'all': self.do_all, 'show': self.do_show, 'destroy': self.do_destroy,
                       'update': self.do_update, 'count': self.do_count}

        if cmd_met in method_dict.keys():
            return method_dict[cmd_met]("{} {}".format(cls_nm, idParam))
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
