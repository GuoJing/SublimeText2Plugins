import sublime_plugin

#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__),
#                "/Library/Python/2.7/site-packages/"))

from isort import SortImports


class IsortCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        contents = []
        selections = self.view.sel()
        for selection in selections:
            contents.append(self.view.substr(selection))
        contents = ''.join(contents)
        contents = contents + '\n'
        new_contents = SortImports(file_contents=contents).output
        if self.view.sel():
            lines = self.view.line(self.view.sel()[0])
            self.view.replace(edit, lines, new_contents)

