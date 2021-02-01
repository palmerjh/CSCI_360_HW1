import autograder
import projectParams
import re
import os

def main():
    codePaths = projectParams.STUDENT_CODE_DEFAULT.split(',')
    # moduleCodeDict = {}
    # for cp in codePaths:
    #     moduleName = re.match('.*?([^/]*)\.py', cp).group(1)
    #     moduleCodeDict[moduleName] = readFile(cp, root=options.codeRoot)
    # moduleCodeDict['projectTestClasses'] = readFile(options.testCaseCode, root=options.codeRoot)
    # moduleDict = loadModuleDict(moduleCodeDict)

    moduleDict = {}
    for cp in codePaths:
        moduleName = re.match('.*?([^/]*)\.py', cp).group(1)
        moduleDict[moduleName] = autograder.loadModuleFile(moduleName, os.path.join('', cp))
    moduleName = re.match('.*?([^/]*)\.py', projectParams.PROJECT_TEST_CLASSES).group(1)
    moduleDict['projectTestClasses'] = autograder.loadModuleFile(moduleName, os.path.join('', projectParams.PROJECT_TEST_CLASSES))

    points = autograder.evaluate(False,'test_cases',moduleDict)
    print(points)


if __name__ == '__main__':
    main()
