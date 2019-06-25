from collections import defaultdict


def simple_assembler(program):
    reg = defaultdict(int)
    program = [cmd.split() for cmd in program]
    pointer = 0
    
    def mov(x, y):
        reg[x] = reg[y] if y in reg else int(y)
        
    def inc(x):
        reg[x] += 1
        
    def dec(x):
        reg[x] -= 1

    def jnz(x, y):
        if reg.get(x) or x.isdigit():
            nonlocal pointer
            pointer += int(y)-1
    
    loc = locals()
    while pointer < len(program):
        handler, *args = program[pointer]
        loc[handler](*args)

        pointer += 1

    return reg
