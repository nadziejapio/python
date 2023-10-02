class Jar:
    cookies = 0
    cap = 0
    def __init__(self, capacity=12):
        if int(capacity) > 0:
            self.cap = capacity
        else:
            raise ValueError()
    def __str__(self):
        return self.cookies*"🍪"

    def deposit(self, n):
        if int(n) > self.cap - self.cookies:
            raise ValueError()
        else:
            self.cookies += int(n)

    def withdraw(self, n):
        if int(n) > self.cookies:
            raise ValueError()
        else:
            self.cookies -= int(n)

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.cookies