from typing import List

class Reader():
    def __init__(self, content: str, respect_inst: bool) -> None:
        self.__content = content
        self.__respect_inst = respect_inst
        self.__pointer = 0
        self.__enabled = True

    def __is_pointer_out_of_bound(self) -> bool:
       return self.__pointer >= len(self.__content)

    def peek(self):
        if self.__is_pointer_out_of_bound():
            return None
        return self.__content[self.__pointer]

    def read_char(self) -> str | None:
        if self.__is_pointer_out_of_bound():
            return None
        ch = self.__content[self.__pointer]
        self.__pointer += 1
        return ch

    def unread_char(self):
        self.__pointer = max(0, self.__pointer - 1)

    def read_until(self, needles: List[str]):
        ch = self.read_char()
        while ch != None and not ch in needles:
            ch = self.read_char()
        return ch

    def expect(self, ch: str) -> bool:
        if self.__is_pointer_out_of_bound():
            return False
        return True if self.__content[self.__pointer] == ch else False

    def expect_read(self, ch: str) -> bool:
        exp = self.expect(ch)
        if exp:
            self.read_char()
            return True
        else:
            return False

    def read_int(self) -> int | None:
        int_builder = ""

        curr_ch = self.read_char()
        while curr_ch != None and curr_ch.isdigit():
            int_builder += curr_ch
            curr_ch = self.read_char()
        # I can probably handle the loop without the need of `unread_char`
        self.unread_char()

        try:
            return int(int_builder)
        except ValueError:
            return None

    def expect_peek_seq(self, seq: str):
        for ch in seq:
            exp = self.expect_read(ch)
            if not exp:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self) -> tuple[int, int] | None:
        if self.__is_pointer_out_of_bound():
            raise StopIteration

        starting_seq = self.read_until(["m", "d"])
        if starting_seq == "m":
            possible_mul_seq = self.expect_peek_seq("ul(")
            if not possible_mul_seq:
                return None

            f_int = self.read_int()
            if not self.expect_read(","):
                return None
            s_int = self.read_int()

            if not f_int or not s_int:
                return None
            if not self.expect_read(")"):
                return None

            if self.__enabled:
                return f_int, s_int
            else:
                return None
        elif starting_seq == "d" and self.__respect_inst:
            if not self.expect_read("o"):
                return None

            peeked = self.peek()
            if peeked == "n":
                possible_neg_seq = self.expect_peek_seq("n't()")
                if not possible_neg_seq:
                    return None
                self.__enabled = False
            elif peeked == "(":
                possible_pos_seq = self.expect_peek_seq("()")
                if not possible_pos_seq:
                    return None
                self.__enabled = True


        return None


def get_reader(filename = "input.txt", respect_inst = False):
    file = open(filename)
    content = file.read()
    file.close()

    return Reader(content, respect_inst)

def part_one():
    mem = get_reader()
    total_mul = 0
    for res in mem:
        if res != None:
            f, s = res
            total_mul += f * s
    print(f"Part one: {total_mul}")

def part_two():
    mem = get_reader(respect_inst=True)
    total_mul = 0
    for res in mem:
        if res != None:
            f, s = res
            total_mul += f * s
    print(f"Part two: {total_mul}")


if __name__ == "__main__":
    part_one()
    part_two()
