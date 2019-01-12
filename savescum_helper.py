import os
import sys
import time
import shutil

HELP_TEXT = """ \
USAGE:
    python3 savescum-helper.py <save_location> [backup_directory]"""


def main():
    if len(sys.argv) == 1:
        exit(HELP_TEXT)

    save = sys.argv[1]
    backup = sys.argv[2] if len(sys.argv) == 3 else "backup"

    if not os.path.isdir(backup):
        os.mkdir(backup)

    last_modify = 0
    last_size = 0

    while True:
        stats = os.stat(save)
        if stats.st_mtime != last_modify and stats.st_size != last_size:
            last_modify = stats.st_mtime
            last_size = stats.st_size
            base_name, extension = os.path.splitext(save_location)
            date = time.strftime("_%Y-%m-%d_%H-%M-%S", time.localtime(last_modify))
            file_name = base_name + date + extension
            shutil.copy2(save, os.path.join(backup, file_name))
            print(f"Backup created for {save}: {file_name}")

        time.sleep(5)


if __name__ == "__main__":
    main()
