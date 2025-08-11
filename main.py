import runner
print(">>>>>BRAINFUCK INTERPRITER<<<<<")

values = brainfuck_ascii_list = [
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",     # 0–15
    "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",     # 16–31
    " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",  # 32–47
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?",  # 48–63
    "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",  # 64–79
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_",  # 80–95
    "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  # 96–111
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", ""     # 112–127
]
import sys
def help(baseCommand):
    if baseCommand == None:
        print("compile")
        print("run")
        print("-f     file input")
        print("-o     output file")
        print("-p     plugins ")
    elif baseCommand == "compile":
        print("compile <file> <plugins>")
    elif baseCommand == "run":
        print("run <file> <speed>")

def compile(file):
    pass
    
change = 0
#argument manager
if len(sys.argv) > 1+change:
    print("more than one argument")
else:
    help(None)
    quit()

if sys.argv[1+change] == "compile":
    print("compiling")
    tag = "None"
    file = "None"
    for number, argument in enumerate(sys.argv):
        if argument == "-f":
            file = sys.argv[number+1]
    if file == "None":
        print("no file provided")
    else:
        print(file)
        with open(file, "r") as f:
            file_contents = f.read()
        runner.run(file_contents)
