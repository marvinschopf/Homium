"""Main script"""
import sys
import config

def checkVersion(evil=False):
    if(not evil):
        version = sys.version_info
        if(version.major < 3):
            print("You are running Python " + str(version.major) + "." + str(version.minor) + "." + str(version.micro) + ", but at least Python 3.0.0 is required!")
            return False
        if(version.releaselevel != "final"):
            print("You aren't running the python release channel. This is okay, but we recommend you using the release channel.")
            return True
        if(config.DEBUG):
            print("Your version satisfies the requirements.")
        return True
    else:
        if(config.DEBUG):
            print("You are using evil mode, so we will skip version checking.")
        return True

def main():
    if(not checkVersion(config.EVIL_MODE)):
        exit()
