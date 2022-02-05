class LayeredPrinter():
    """
    A class to 'layer print' some values.

    ...

    Attributes
    ----------
    indent : int
        the amount of times you want the prefix character to be repeated
    character : str
        the prefix character or string

    Methods
    -------
    lprint(*args, level:int=0, indent:int=None, character:str=None):
        Print the `*args` with a prefix dependent on level, indent and character.
        If not specified, level will be 0, indent and character will be class
        variables `self.i` and `self.c`.
    """

    def __init__(self, indent:int=4, character:str=None):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            indent : int
                the amount of times you want the prefix character to be repeated
            character : str
                the prefix character or string
        """

        self.i = indent
        self.c = character

    def lprint(self, *args, level:int=0, indent:int=None, character:str=None):
        """
        Print the `*args` with a prefix dependent on level, indent and character.
        
        If not specified, level will be 0 by default, indent and character will 
        be class variables `self.i` and `self.c`.

        Parameters
        ----------
        *args : Any
            any object that can be cast to string
        indent : int
            the amount of times you want the prefix character to be repeated
        character : str
            the prefix character or string
        
        Returns
        -------
        None
        """

        ind = self.i if indent == None else indent

        if self.c == None and character == None:
            prefix =  level * ' |' + ' ├' + ind * '─' + ' '
        else:
            char = self.c if character == None else character
            prefix = level * ind * char

        output = []
        for arg in args:
            newline_split = str(arg).splitlines()
            output.extend([string for string in newline_split])

        [print(prefix + str(elem), sep=" ") for elem in output]


def lprint(*args, level:int=0, indent:int=4, character:str=None):
    """
        Print the `*args` with a prefix dependent on level, indent and character.
        
        If not specified, level will be 0 by default, indent will be 4, and character
        will look like ├─.

        Parameters
        ----------
        *args : Any
            any object that can be cast to string
        indent : int
            the amount of times you want the prefix character to be repeated
        character : str
            the prefix character or string
        
        Returns
        -------
        None
    """
    if character == None:
        prefix = level * '|' + '├' + level * indent * '─' + ' '
    else:
        prefix = level * indent * character

    output = []
    for arg in args:
        newline_split = str(arg).splitlines()
        output.extend([string for string in newline_split])

    [print(prefix + str(elem), sep=" ") for elem in output]
