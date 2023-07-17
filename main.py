import json
import sys
import logging as log
import os

def main(path: str) -> None:
    if not os.path.exists(path):
        log.critical("The provided path does not exists")
        exit()

    try:
        file = open(path)
    except OSError as err:
        log.critical(f"Could not open file with error: {err}")
        exit()
    config = json.load(file)

    for i in config["presentation"]:
        print(i)


if __name__ == "__main__":
    # Init logging
    log.basicConfig(filename="log.txt", encoding='utf-8', level=log.INFO, format='%(asctime)s |%(levelname)s| %(message)s')
    # only one commandline arg: json config
    match len(sys.argv):
        case 1:
            log.critical("Insufficient number of arguments")
            exit()
        case 2:
            log.info("Starting execution")
            print(f"argv: {sys.argv[1]}")
            main(sys.argv[1])
        case other:
            log.critical(f"More arguments than needed (provided: { len(sys.argv)-1 })")
            exit()
    log.info("Finished execution")
