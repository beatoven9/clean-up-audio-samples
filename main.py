import os
import sys
import argparse
import re

def parseDirectory(inputDir, outputDir, baseName=""):
    targetDir = os.path.join(os.getcwd(), inputDir)
    print("Target dir is: ", targetDir)
    files = os.listdir(targetDir)
    if not baseName:
        baseName = outputDir

    for f in files:
        p1 = re.compile("[abcdefgABCDEFG][#-b]?\d")
        noteName = p1.search(f).group()

        p2 = re.compile("\.[^.]+$")
        fileExtension = p2.search(f).group()
        newName = baseName + "_" + noteName + fileExtension
        print(newName)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory')
    parser.add_argument('-n', '--name')
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', '--verbose')
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode")

    if not (args.directory and args.output):
        print("You need an input and output")

    print(args.output)

    parseDirectory(args.directory, args.output, args.name)



if __name__=="__main__":
    main()
