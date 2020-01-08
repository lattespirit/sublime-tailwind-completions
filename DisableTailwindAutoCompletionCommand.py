import sublime
import sublime_plugin

class DisableTailwindAutoCompletionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        prefs = sublime.load_settings('Preferences.sublime-settings')
        prefs.set('tailwind_completion_enabled', False)
        prefs.save_settings('Preferences.sublime-settings')
