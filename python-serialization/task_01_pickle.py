import pickle
#  converts a python object into byte stream that can be saved or sent 
#  uses "wb" for writing bytes & "rb" for reading bytes
class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
      
    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            obj = pickle.load(f)
        return obj
