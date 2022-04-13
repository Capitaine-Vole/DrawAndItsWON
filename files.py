import os
from re import X

def checkFileExistance(name):
    try:
        f = open(name)
        return True
    except IOError:
        with open(name, "x") as f:
            f.close()
            return False
    finally:
        f.close()

def createFilet(name):
    with open(name, "x") as f:
        f.close()

def readFile(name):
    with open(name, "r") as f:
        content = f.read()
        f.close()
        return content

def writeFile(name, content):
    with open(name, "a") as f:
        for x in content:
            f.write(x + "\n")
        f.close()

def clearFile(name):
    with open(name, "w") as f:
        f.truncate()
        f.close()

def removeWords(name, content):
        with open(name, "r") as f:
            lines = f.readlines()
            print(lines)
            f.close()
        with open(name, "w") as f:
            x = lines.strip(content)
            f.write(x)
            f.close()