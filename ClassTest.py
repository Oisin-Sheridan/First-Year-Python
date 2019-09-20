class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
    	self.new = 7

    def f(self):
        return 'hello world'

sample = MyClass()
sample.i = "hello"
print(sample.new)