import sublime, sublime_plugin

text = '''---
layout:    %s
title:     %s
category:  %s
description: %s
---
'''

class JkbloggerCommand(sublime_plugin.WindowCommand):
	title = 'default blogger'
	layout = 'post'
	category = 'blog'
	description = ''

	def run(self):
		fname = ''
		def done(commands):
			cs = commands.split(',')
			if not cs:
				return

			if len(cs) == 1:
				self.title = cs[0]
			if len(cs) == 2:
				self.title = cs[0]
				self.category = cs[1]
			if len(cs) == 3:
				self.title = cs[0]
				self.category = cs[1]
				self.layout = cs[2]
			self.title = self.title or 'Jkblogger'
			self.description = '%s...' % self.title

			v = self.window.new_file()
			e = v.begin_edit()
			r = text % (self.layout, self.title, self.category, self.description)
			v.insert(e, 0, r)

		self.window.show_input_panel("Input the title:", fname, done, None, None)