import sublime, sublime_plugin

templates = dict(
    py = """# filename
# -*- coding: utf-8 -*-

class %s:
    def __init__(self):
        pass

    @classmethod
    def get(cls, id):
        pass

    @classmethod
    def gets(cls, ids):
        return [cls.get(id) for id in ids]

    @classmethod
    def add(cls, *args, **kargs):
        pass

    def update(self, *args, **kargs):
        self._clear_cache()

    def delete(self):
        self._clear_cache()

    def _clear_cache(self):
        pass
    """,
)

default_template = """class %s:

"""

class GenCommand(sublime_plugin.WindowCommand):

    def run(self):
        fname = ''
        def done(commands):
            cs = commands.split(',')
            try:
                code, class_name = cs
            except:
                code, class_name = 'py', 'SomeClass'
            v = self.window.new_file()
            e = v.begin_edit()
            text = templates.get(code, default_template)
            r = text % class_name
            v.insert(e, 0, r)

        self.window.show_input_panel("Input the type and class name:", fname, done, None, None)
