class WithScalarArgument:
    def __init__(self, simple_argument, scalar_value):
        self.simple_argument = simple_argument
        self.scalar_value = scalar_value

    def get_scalar_value(self):
        return self.scalar_value