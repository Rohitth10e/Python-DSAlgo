class Cookie:
    def __init__(self, color):
        self.color = color
    
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
cookie_one = Cookie('green')
cookie_two = Cookie('yellow')

print(cookie_one.get_color())
print(cookie_two.get_color())
cookie_two.set_color('purple')
print(cookie_two.get_color())

class LinkedList:
    def __init__(self, value):
        pass
    # all other methods