from .simple_argument import SimpleArgument

import logging

class WithArgument:
    def __init__(self, simple_argument: SimpleArgument):
        logging.debug(simple_argument)
        self.simple_argument = simple_argument

    def get_answer(self):
        return self.simple_argument.answer