import os
from pprint import pprint
class OsUtils:
    def __init__(self):
        """

        :rtype: None
        """

    def print_directory_contents(self, os_path):
        directory_contents = os.listdir(os_path)
        pprint('Dcirectory %s contains: %s' % (os_path, directory_contents))
        return directory_contents
