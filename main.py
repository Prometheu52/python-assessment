import logging as log
import sys
import os

import ppt_builder


def main(path: str):
    if not os.path.exists(path):
        log.critical("The path to the config file does not exist!")
        exit_on_failure()

    ppt_builder.ConfingDecoder(path)


def exit_on_failure():
    print("Something went wrong, check log.txt for further info!")
    exit()


if __name__ == "__main__":
    # Init logging
    log.basicConfig(filename="log.txt", encoding='utf-8', level=log.INFO,
                    format='%(asctime)s |%(levelname)s| %(message)s')
    # only one commandline arg: json config
    match len(sys.argv):
        case 1:
            log.critical("Insufficient number of arguments")
            exit_on_failure()
        case 2:
            log.info("Starting execution")
            main(sys.argv[1])
        case other:
            log.critical(f"More arguments than needed (provided: {len(sys.argv) - 1})")
            exit_on_failure()
    log.info("Finished execution")
