# main.py
import os
import sys
import subprocess
from downloader import download_latest
from cleaner import wait_and_remove
from rename import replace_and_restart

def main():
    import sys

    if "--update" not in sys.argv:
        return

    exe_target = sys.argv[2]       # ex: "Explorateur_distant.exe"
    repo = sys.argv[3]             # ex: "yo-le-zz/Explorateur_distant"
    
    new_exe = exe_target + ".new"  # temporaire
    download_latest(repo, new_exe)
    wait_and_remove(exe_target)
    replace_and_restart(new_exe, exe_target)


def self_destruct():
    exe_path = os.path.abspath(sys.argv[0])

    cmd = f'''
    ping 127.0.0.1 -n 3 > nul
    del "{exe_path}"
    '''

    subprocess.Popen(
        ["cmd", "/c", cmd],
        creationflags=subprocess.CREATE_NO_WINDOW
    )

if __name__ == "__main__":
    main()
    self_destruct()
    sys.exit(0)

