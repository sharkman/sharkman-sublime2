
import sublime
import sublime_plugin
import os
import glob

class FindGitPortableBinaryCommand(sublime_plugin.WindowCommand):
    """
    Search for actual path for a portable git, that comes with the official
    GitHub application (this path changes every time the application updates)
    """
    def run(self, **kwargs):
        for d in glob.glob(os.path.join(os.environ["LOCALAPPDATA"], "GitHub", "PortableGit_*")):
            sublime.load_settings("Git.sublime-settings").set("git_command", os.path.join(d, "bin", "git.exe"))
            sublime.save_settings("Git.sublime-settings")
            break
