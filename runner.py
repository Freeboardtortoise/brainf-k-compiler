import sys
import tty
import termios
import plugins.main as plugins

def get_char():
    """Reads a single character from stdin without requiring Enter (Unix only)."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def run(code):
    memory = [0]
    pointer = 0
    pc = 0  # program counter
    loop_stack = []
    plugin_manager = plugins.pluginManager()

    while pc < len(code):
        cmd = code[pc]
        memory, pointer, cmd, pc = plugin_manager.update(memory, pointer, cmd, pc)

        if cmd == '>':
            pointer += 1
            if pointer >= len(memory):
                memory.append(0)

        elif cmd == '<':
            pointer -= 1
            if pointer < 0:
                raise IndexError("Pointer moved left of memory start")

        elif cmd == '+':
            memory[pointer] = (memory[pointer] + 1) % 256

        elif cmd == '-':
            memory[pointer] = (memory[pointer] - 1) % 256

        elif cmd == '.':
            print(chr(memory[pointer]), end='')

        elif cmd == ',':
            memory[pointer] = ord(get_char())

        elif cmd == '[':
            if memory[pointer] == 0:
                # Skip ahead to matching ']'
                open_brackets = 1
                while open_brackets > 0:
                    pc += 1
                    if pc >= len(code):
                        raise SyntaxError("Unmatched '['")
                    if code[pc] == '[':
                        open_brackets += 1
                    elif code[pc] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(pc)

        elif cmd == ']':
            if not loop_stack:
                raise SyntaxError("Unmatched ']'")
            if memory[pointer] != 0:
                pc = loop_stack[-1]
                continue
            else:
                loop_stack.pop()

        pc += 1

