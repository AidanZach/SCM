#!/usr/bin/python

import os
import shutil
import filecmp

game_file_path = 'Bin64/dbghelp.dll'


def patch_game():
    try:
        # Ensure destination directory exists
        os.makedirs(os.path.dirname(game_file_path), exist_ok=True)

        # If the file already matches our patcher binary we consider it patched
        if os.path.exists(game_file_path) and filecmp.cmp("patcher.bin", game_file_path, shallow=False):
            return 0

        shutil.copyfile("patcher.bin", game_file_path)
        return 1
    except Exception as e:
        print(e)
        return -1


def restore_game():
    try:
        if os.path.exists(game_file_path):
            os.remove(game_file_path)
            return 1
        else:
            return 0
    except Exception as e:
        print(e)
        return -1
