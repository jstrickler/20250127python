import sys
import os.path

unix_rel = "bin/spam.txt"  # Unix relative path
unix_abs = "/usr/local/bin/ham"  # Unix absolute path

win_rel = r"spam\ham.doc"  # Windows relative path
win_unc = r"\\spam\ham\eggs\toast\jam.doc"  # Windows UNC path

if sys.platform == 'win32':  # Are we on Windows?
    print("win_rel:", win_rel)
    print("win_unc:", win_unc)
    print("dirname(win_rel):", os.path.dirname(win_rel))  # Just the folder name
    print("dirname(win_unc):", os.path.dirname(win_unc))
    print("basename(win_rel):", os.path.basename(win_rel))  # Just the file (or folder) name
    print("basename(win_unc):", os.path.basename(win_unc))
    print("isabs(win_rel):", os.path.isabs(win_rel))  # Is it an absolute path?
    print("isabs(win_unc):", os.path.isabs(win_unc))
else:  # Mac/Linux
    print("unix_rel:", unix_rel)
    print("unix_abs:", unix_abs)
    print("dirname(unix_rel):", os.path.dirname(unix_rel))  # Just the folder name
    print("dirname(unix_abs):", os.path.dirname(unix_abs))
    print("basename(unix_rel):", os.path.basename(unix_rel))  # Just the file (or folder) name
    print("basename(unix_abs):", os.path.basename(unix_abs))
    print("isabs(unix_rel):", os.path.isabs(unix_rel))  # Is it an absolute path?
    print("isabs(unix_abs):", os.path.isabs(unix_abs))
    print(f"os.path.expanduser('~'): {os.path.expanduser('~')}")
    print(f"os.path.expanduser('~root'): {os.path.expanduser('~root')}")
    