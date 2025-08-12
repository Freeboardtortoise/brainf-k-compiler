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
    if len(sys.argv) == 2:
        help("compile")
    file = "None"
    plugins = []
    doing_plugins = []
    output = "None"
    for number, argument in enumerate(sys.argv):
        if argument == "-f":
            if len(sys.argv)-1 >= number+1:
                file = sys.argv[number+1]
            else:
                print("no file provided after -f tag")
                quit()
        if doing_plugins:
            if argument != "-p" or "-o":
                plugins = plugins + [argument]
            else:
                doing_plugins = False
        if argument == "-p":
            doing_plugins = True
        if argument == "-o":
            if len(sys.argv)-1 >= number+1:
                output = sys.argv[number+1]
            else:
                print("no output path after -o tag")
                quit()
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
    if len(sys.argv) == 2:
        help("run")
        quit()
    if len(sys.argv)-1 >= 3+change:
        speed = int(sys.argv[3+change])
    else:
        speed = 0
    if len(sys.argv)-1 >= 2+change:
        file = sys.argv[2+change]
    else:
        print("no file provied")
        quit()
    try:
        with open(file, "r") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"{file} is not a valid file path")
        quit()
    plugins = file_contents.split("\n")[0].split(",")
    file_contents = file_contents.split("\n")[1]
    runner.run(file_contents, plugins, speed)
