#!/usr/bin/python3
class VerboseList(list):

    def append(self, object):
        super().append(object)
        print("Added {} to the list".format(object))

    def extend(self, objects):
        super().extend(objects)
        print("Extended the list with {} items.".format(len(objects)))

    def remove(self, object):
        if object in self:
            print("Removed {} from the list.".format(object))
            super().remove(object)
        else:
            print("{} cannot be founf in list".format(object))

    def pop(self, object=None):
        #  remove last element. Coutntinue with customm behaviour
        if object is None:      #  checks if object was provided
            item = super().pop()
        else:
            if object < 0 or object >= len(self):   #  checks if object is valid
                raise IndexError("Object you're trying to pop is out of range")
            item = item = super().pop(object)

        print("Popped {} from the list".format(item))
