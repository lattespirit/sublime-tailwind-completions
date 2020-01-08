import sublime
import sublime_plugin

class EnableTailwindAutoCompletionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings('TailwindAutoCompletion.sublime-settings')
        prefs.set('tailwind_completion_enabled', True)
        prefs.save_settings('TailwindAutoCompletion.sublime-settings')
