class GroupOverflowError(Exception):
    def __init__(self, message='Group overflow (more than 10 students)'):
        self.message = message
        super().__init__(self.message)