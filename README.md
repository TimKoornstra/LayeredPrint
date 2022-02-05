# Layered Printing in Python 3
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GPL-3.0](https://img.shields.io/github/license/TimKoornstra/LayeredPrint.svg?color=brightgreen)](https://opensource.org/licenses/GPL-3.0)

This repository contains a module that helps you print in layers in Python 3.
## About the code
Sometimes, when you're working in big files and want to test print a lot of things, it is useful to know where something might go wrong, or where in your code you are printing something. Using this module, you can either create a `LayeredPrinter` class or just use the `lprint` function directly. With this function, you can specify on what 'layer' or 'level' in your code, you are printing something.

## Functionality
The code contains a class with a function called `lprint`, as well as the loose `lprint` function. The two functions do the exact same thing: they add a prefix to regularly printed text. The entire prefix can be modified, and does not have to be the same as the one shown in the example use case. To change the prefix, you can change multiple parameters in the `lprint` function: `layer` describes the depth of the printed text, `character` is the actual character that will be used as prefix, and `indent` is the amount of times that `character` is replicated. 

Small examples: 
```
lprint('Example')
>> ├──── Example

lprint('Example 1', layer=1, indent=2, character='.')
>> ..Example 1

lprint('Example 2', layer=4, indent=4, character='-')
>> ----------------Example 2
```

The extra functionality of the `LayeredPrinter` class is that you only have to specify these extra parameters once, as opposed to every single time you want to `lprint` something. Of course, you can still change the parameters of a `LayeredPrinter.lprint` if you feel like they should not be the same as the rest of the class.

## Example use case
Let's say for example you have the following code:

![afbeelding](https://user-images.githubusercontent.com/89044870/152645637-9524edd8-3619-4409-864a-1d8704872435.png)

Which will evaluate to:
```
Starting calculation...
0
1 0
1 2
1 4
1 6
1 8
2
3 0
3 2
3 4
3 6
3 8
4
Done!
```
This might get a bit incomprehensible... Using the `lprint` function, you can specify the level of the called function, and it will print your statements in the specified hierarchy. The same code that uses `lprint`:

![afbeelding](https://user-images.githubusercontent.com/89044870/152646830-b24bbed5-eba9-4272-ae27-5a6f0984bed0.png)

Which will evaluate to:
```
├──── Starting calculation...
| ├──── 0
| | ├──── 1 0
| | ├──── 1 2
| | ├──── 1 4
| | ├──── 1 6
| | ├──── 1 8
| ├──── 2
| | ├──── 3 0
| | ├──── 3 2
| | ├──── 3 4
| | ├──── 3 6
| | ├──── 3 8
| ├──── 4
├──── Done!
```
As you can see, this is way more comprehensible than the normal output (especially when working in big files!).


## Dependencies
As of right now, this code requires no external dependencies.

## How to run
I have not made this into a package, yet. So for now, installation has to be done manually.
- Clone the repository
- Place the `__init__.py` and `LayeredPrint.py` files in your own repository. 
- You can now use them as you would use a normal package.
