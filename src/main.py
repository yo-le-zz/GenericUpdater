# main.py
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

if __name__ == "__main__":
    main()

