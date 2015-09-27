#inheritance
class Parent():
    def print_last_name(self):
        print('Dirir')
class Child(Parent):

    def print_first_name(self):
        print('Ibrahim')
    def print_last_name(self):
        print('Ahmed')
Ibrahim = Child()
Ibrahim.print_first_name()
Ibrahim.print_last_name()
