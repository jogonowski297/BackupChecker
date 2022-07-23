class Errors:
    def __init__(self):
        self.errors = 0

    def add_error(self):
        self.errors+=1

    def get_errors(self):
        return self.errors