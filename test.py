import pytest
class Hello():
    # __init__ is a definition runs itself. 
    def __init__(self): 
        print('Hello there')
        # Call another definition. 
        self.andBye()

    # This definition should be calles in order to be executed. 
    def andBye(self):
        print('Goodbye')

# Run class 
Hello()
