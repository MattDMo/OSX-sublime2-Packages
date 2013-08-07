import sublime_plugin
from datetime import datetime


class TimeStampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # formatting options at http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
        stamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")  # 2013-07-18 14:54:23 UTC
        for r in self.view.sel():
            if r.empty():
                self.view.insert(edit, r.a, stamp)
            else:
                self.view.replace(edit, r,   stamp)