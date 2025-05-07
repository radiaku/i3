#!/home/radia/miniconda3/bin/python3

import i3ipc

i3 = i3ipc.Connection()
tree = i3.get_tree()

# Collect all normal (non-dock) windows
windows = [w for w in tree.leaves() if w.window and w.type == "con"]

if not windows:
    exit(0)

focused = tree.find_focused()
ids = [w.id for w in windows]

try:
    idx = ids.index(focused.id)
    next_win = windows[(idx + 1) % len(windows)]
except ValueError:
    next_win = windows[0]

i3.command('[con_id=%s] focus' % next_win.id)
