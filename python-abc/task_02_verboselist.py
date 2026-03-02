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
        #  checks if object was provided
        if object is None:
            item = super().pop()
        else:
            #  checks if object is valid
            if object < 0 or object >= len(self):
                raise IndexError("Object you're trying to pop is out of range")
            item = super().pop(object)

        print("Popped {} from the list".format(item))
        return item
