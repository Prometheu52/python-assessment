import json
import sys
import logging as log
import os

from pptx import Presentation

def main(path: str):
    if not os.path.exists(path):
        log.critical("The provided path does not exists")
        exit_on_failure()

    try:
        json_file = open(path)
        config: object = json.load(json_file)
    except OSError as err:
        log.critical(f"Could not open file with error: {err}")
        exit_on_failure()
    except ValueError as err:
        log.critical(f"The provided file is not in a valid json format, error: {err}")
        exit_on_failure()

    # Presentation raises ValueError if the file is not a ppt file
    prs = Presentation()

    for i in prs.slide_layouts:
        print(i)

def exit_on_failure():
    print("Something went wrong, check the log.txt for further info!")
    exit()

if __name__ == "__main__":
    # TODO: Check if the python-pptx modul is installed
    # Init logging
    log.basicConfig(filename="log.txt", encoding='utf-8', level=log.INFO, format='%(asctime)s |%(levelname)s| %(message)s')
    # only one commandline arg: json config
    match len(sys.argv):
        case 1:
            log.critical("Insufficient number of arguments")
            exit_on_failure()
        case 2:
            log.info("Starting execution")
            # print(f"argv: {sys.argv[1]}")
            main(sys.argv[1])
        case other:
            log.critical(f"More arguments than needed (provided: { len(sys.argv)-1 })")
            exit_on_failure()
    log.info("Finished execution")
