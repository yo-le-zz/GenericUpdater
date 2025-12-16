# rename.py
import os
import subprocess

def replace_and_restart(new_exe, final_exe):
    os.rename(new_exe, final_exe)
    subprocess.Popen([final_exe])
