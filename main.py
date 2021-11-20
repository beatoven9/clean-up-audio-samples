import os
import sys
import argparse
import re

def parseDirectory(inputDir, outputDir, baseName=""):
    inputPath = os.path.join(os.getcwd(), inputDir)
    inputFiles = os.listdir(inputPath)
    parsedFiles = []
    if not baseName:
        baseName = outputDir

    for f in inputFiles:
        p1 = re.compile("[abcdefgABCDEFG][#-b]?\d")
        noteName = p1.search(f).group()

        p2 = re.compile("\.[^.]+$")
        fileExtension = p2.search(f).group()
        newName = baseName + "_" + noteName + fileExtension
        parsedFiles.append((f, newName))

    return parsedFiles

def copyFiles(parsedFiles, inputDir, outputDir):
    inputPath = os.path.join(os.getcwd(), inputDir)
    outputPath = os.path.join(os.getcwd(), outputDir)
    if not os.path.isdir(outputDir):
        os.mkdir(outputDir)

    for pair in parsedFiles:
        src = inputPath + '/' + pair[0]
        dest = outputPath + '/' + pair[1]
        command = "cp " + src + ' ' + dest
        os.system(command)

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


    parsedFiles = parseDirectory(args.directory, args.output, args.name)
    copyFiles(parsedFiles, args.directory, args.output)


if __name__=="__main__":
    main()
