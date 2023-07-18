import os


def debug_clear_all_pptx(directory: str):
    for listdir_entry in os.listdir(directory):
        if os.path.isfile(listdir_entry) and os.path.splitext(listdir_entry)[-1] == ".pptx":
            os.remove(listdir_entry)


if __name__ == '__main__':
    debug_clear_all_pptx(os.getcwd())