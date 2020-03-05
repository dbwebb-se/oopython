"""
Example program for showing how we can create a dynamicall menu program.
This way we don't need a big if-statement structure to handle different cases.
Instad we utilize a dictionay and getattr().
In the dictionary we have the meny choice as key and the name for the method
that handles the chocice as value.
With getattr() look for and retrieve a method in self with the method name from
the dictionary and the call the method.

Additionally we type the explanation for the choice a method handles in its
docstring. We can then use the module inspect and its function getdoc() to
return the docstring. With theses tools we can dynamically create the
menu print aswell.

The interesting methods are:
__init__(): here we create the dict with choice and method name
main(): contains the main loop where we would have the giant if-statement
_get_method(): uses getattr() to return reference to choice method
_print_menu(): uses _get_method() and getdoc() to create and print menu()

To take it one step further we could extract the dictionary to its own file.
That way this file would only containe the code and the other file would
contain the "data". It would make this code little bit more clean.
"""
import inspect
import sys

class Handler():
    """
    Simple handler class with a menu
    """

    def __init__(self):
        self._options = {
            "1": "add_value",
            "2": "remove",
            "q": "quit",
        }

    def main(self):
        """
        Entrypoint for program
        """
        while True:
            self._print_menu()
            c = input("Enter: ")
            try:
                self._get_method(c)()
            except KeyError:
                input("Invalid choice!\nPress any key to continue")

    def _print_menu(self):
        """
        Use docstring from methods to print options for the program
        https://docs.python.org/3/library/inspect.html#inspect.getdoc
        """
        menu = "-------------------------\n"
        # loop over all options in dictionary
        for key in sorted(self._options):
            # Use _get_method to dynamically get method
            method = self._get_method(key)
            # Use getdoc to get docstring from method
            docstring = inspect.getdoc(method)

            # format meny choice text
            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(menu,)

    def _get_method(self, method_name):
        """
        Use function getattr() to dynamically get value of an attribute.
        https://docs.python.org/3.7/library/functions.html#getattr
        If attribute is a method, a reference to the method is returned.
        For an example, https://www.journaldev.com/16146/python-getattr
        """
        return getattr(self, self._options[method_name])

    @staticmethod
    def add_value():
        """
        Add a value to datastructure
        """
        input("Add a value to add... ")

    @staticmethod
    def remove():
        """
        Remove a value from datastructure
        """
        input("remove a value to remove... ")

    @staticmethod
    def quit():
        """
        Exit program
        """
        sys.exit()



if __name__ == "__main__":
    h = Handler()
    h.main()
