class Person:
    def __init__(self, first='', last='', eye_color='', age=0):
        self.first = first
        self.last = last
        self.eye_color = eye_color
        self.age = age

    # def __repr__(self):
    #     return (repr(self.first) + ' ' +
    #         repr(self.last) + ' ' +
    #         repr(self.eye_color) + ' ' +
    #         repr(self.age))
    
    # def __str__(self):
    #     return str('Name: ' +
    #         self.first + ' ' +
    #         self.last +
    #         ', Eye Color: ' +
    #         self.eye_color +
    #         ', Age: ' + str(self.age))


if __name__ == "__main__":

    person1 = Person('john', 'smith', 'brown', 50)

    print(person1)
    print(repr(person1))
    print(str(person1))
