"""Day 17: Chronospatial Computer"""

from sys import stdin


class Computer:
    """Class for the elf computer."""
    def __init__(self, regA: int, regB: int, regC: int, program: list[int]):
        self.regA, self.regB, self.regC = regA, regB, regC
        self.program = program
        self.instruction = 0
        self.output: list[int] = []

    def combo(self, op: int) -> int:
        """Returns the value of combo operators. Operators less than 4 are
        themselves. Otherwise, 4 is register A, 5 is register B, and 6 is
        register C.
        """
        return op if op < 4 else [self.regA, self.regB, self.regC][op - 4]

    def dv(self, op: int):
        """Performs the division operation used by adv, bdv, and cdv"""
        return self.regA // 2 ** self.combo(op)

    def adv(self, op: int):
        """Sets register A to A / 2^combo(op)."""
        self.regA = self.dv(op)

    def bxl(self, op: int):
        """Sets register B to B XOR op."""
        self.regB = self.regB ^ op

    def bst(self, op: int):
        """Sets register B to combo(op) mod 8."""
        self.regB = self.combo(op) % 8

    def jnz(self, op: int):
        """Jumps the instruction pointer to op if A != 0."""
        if self.regA != 0:
            self.instruction = op
        else:
            self.instruction += 2

    def bxc(self, _: int):
        """Sets register B to B XOR C. Ignores its operand."""
        self.regB = self.regB ^ self.regC

    def out(self, op: int):
        """Prints combo(op) mod 8."""
        self.output.append(self.combo(op) % 8)

    def bdv(self, op: int):
        """Sets register B to A / 2^combo(op)."""
        self.regB = self.dv(op)

    def cdv(self, op: int):
        """Sets register B to A / 2^combo(op)."""
        self.regC = self.dv(op)

    def run(self):
        """Runs the program until the instruction pointer is past the end of
        the program.
        """
        opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

        end = len(self.program)

        while self.instruction < end:
            opcode = self.program[self.instruction]
            op = self.program[self.instruction + 1]
            opcodes[opcode](op)
            if opcode != 3:
                self.instruction += 2


def tests():
    """Tests for this module."""
    c = Computer(0, 0, 9, [2, 6])
    c.run()
    assert c.regB == 1

    c = Computer(10, 0, 0, [5, 0, 5, 1, 5, 4])
    c.run()
    assert c.output == [0, 1, 2]

    c = Computer(2024, 0, 0, [0, 1, 5, 4, 3, 0])
    c.run()
    assert c.output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]

    c = Computer(0, 29, 0, [1, 7])
    c.run()
    assert c.regB == 26

    c = Computer(0, 2024, 43690, [4, 0])
    c.run()
    assert c.regB == 44354

    c = Computer(729, 0, 0, [0, 1, 5, 4, 3, 0])
    c.run()
    assert c.output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def main(input_string: str) -> list[int]:
    """Reads registers and a program from stdin and runs the program."""
    lines = input_string.splitlines()
    regA = int(lines[0].split()[-1])
    regB = int(lines[1].split()[-1])
    regC = int(lines[2].split()[-1])

    program = [int(x) for x in lines[4].split()[-1].split(',')]
    c = Computer(regA, regB, regC, program)
    c.run()
    return c.output


if __name__ == '__main__':
    tests()
    print(','.join([str(x) for x in main(stdin.read())]))
