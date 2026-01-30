Eighth Project/ ~class and object~

*__init__
    -its a constructor and runs when you create an object
    -mainly used when creating a private instance attribute because that's where you initialize your object's attributes
    
*class - a blueprint for creating objects( in C = struct)
    -keyword telling python "you're creating a blueprint"
    -defines data & behavior(functions)
        *data(attributes) - variables belonging to an object
    *method
        -a function inside a class

*object - an instance(in C = custom data type)
    -each object can store its own value(data)
        *data(attributes)
            -normal attribute
                -can be accessed and changed from anywhere
            -private attribute
                -private instance have __ in front of them |eg| __object
                -blocks direct access and can only be used inside the class
                -usage:
                    protect object's data
                    control over how value changes
                    avoid bugs

*method
    a function inside a class

*@
    decorator
        a function that wraps another function/ adds or modifies another function/ and it doesnt change the original function

*setter


~Task Explanantion~
Task 0:
(ONLY)create a class named Square
    
Task 1:
__init__ - it defines data when the instance is created

task 2:
----

task 3:
** 2 - raise power of 2

task 4:
*property
    a builtin function
    property() is a constructor that takes a function and returns a property object.
        *property object
            stores a getter
*size.setter
    a builtin function
    works in pair with @property; links a setter to the property
    makes a method the setter for the size property

task 5:

task 6:

