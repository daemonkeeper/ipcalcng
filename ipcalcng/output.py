from __future__ import  print_function

class TextOutput(object):
    def __init__(self, args, prefix):
        self.args = args
        self.prefix = prefix

    def print_out(self):
        print(self.prefix)
