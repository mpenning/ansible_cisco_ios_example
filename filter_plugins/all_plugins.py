from pprint import pprint
import json

class FilterModule(object):
    """Define all custom filters in FilterModule()"""
    def __init__(self, *args, **kwargs):
        pass

    def filters(self):
        """Important: return a dictionary with all known filters"""
        return {'my_filter': self.my_filter}

    def my_filter(self, cmd_output=None):
        """Do something with the cmd_output text"""
        assert cmd_output is not None

        lines = cmd_output["stdout_lines"]

        return lines
