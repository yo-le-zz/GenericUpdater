# cleaner.py
def wait_and_remove(exe_name):
    import time, os

    time.sleep(2)

    for _ in range(5):
        try:
            if os.path.exists(exe_name):
                os.remove(exe_name)
            return
        except PermissionError:
            time.sleep(1)

    raise RuntimeError("Impossible de supprimer l'ancien exe")
