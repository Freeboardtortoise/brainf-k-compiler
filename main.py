import runner
import sys


def clear():
    print("\n"*32)


clear()
print(">>>>>BRAINFUCK INTERPRITER<<<<<")


def help(baseCommand):
    if baseCommand == None:
        print("compile")
        print("run")
        print("-f     file input")
        print("-o     output file")
        print("-p     plugins")
    elif baseCommand == "compile":
        print("flags:")
        print("-f     file to compile")
        print("-o     output file name")
        print("-p     plugins to add")
    elif baseCommand == "run":
        print("run <file> <speed>")


def compile(file):
    pass


change = 0
# argument manager
if len(sys.argv) == 1:
    help(None)
    quit()

if sys.argv[1+change] == "compile":
    file = "None"
    plugins = []
    doing_plugins = []
    output = "None"
    for number, argument in enumerate(sys.argv):
        if argument == "-f":
            file = sys.argv[number+1]
        if doing_plugins:
            if argument != "-p" or "-o":
                plugins = plugins + [argument]
            else:
                doing_plugins = False
        if argument == "-p":
            doing_plugins = True
        if argument == "-o":
            output = sys.argv[number+1]
    if file == "None":
        print("no file provided")
        quit()
    if output == "None":
        output = file.split(".")[0] + ".bfc"
    with open(output, "w") as f:
        if plugins == []:
            f.write("\n")
        else:
            f.write(f"{",".join(plugins)}\n")
        with open(file, "r") as fi:
            code = fi.read()
        new = ""
        for charactor in code:
            if (charactor) == "\n":
                pass
            else:
                new = new + charactor
        f.write(new)
    print("done compiling")

if sys.argv[1+change] == "run":
    speed = int(sys.argv[3+change])
    file = sys.argv[2+change]
    with open(file, "r") as f:
        file_contents = f.read()
    plugins = file_contents.split("\n")[0].split(",")
    file_contents = file_contents.split("\n")[1]
    runner.run(file_contents, plugins, speed)
