class Reader():
    def __init__(self, content: str) -> None:
        self.__content = content
        self.__pointer = 0

    def __is_pointer_out_of_bound(self) -> bool:
       return self.__pointer >= len(self.__content)

    def read_char(self) -> str | None:
        if self.__is_pointer_out_of_bound():
            return None
        ch = self.__content[self.__pointer]
        self.__pointer += 1
        return ch

    def unread_char(self):
        self.__pointer = max(0, self.__pointer - 1)

    def read_until(self, needle: str):
        ch = self.read_char()
        while ch != None and ch != needle:
            ch = self.read_char()

    def expect(self, ch: str) -> bool:
        if self.__is_pointer_out_of_bound():
            return False
        return True if self.__content[self.__pointer] == ch else False

    def expect_peek(self, ch: str) -> bool:
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

    def __iter__(self):
        return self

    def __next__(self):
        if self.__is_pointer_out_of_bound():
            raise StopIteration

        self.read_until("m")

        if self.expect_peek("u") and \
            self.expect_peek("l") and \
            self.expect_peek("("):
            f_int = self.read_int()
            if not self.expect_peek(","):
                return None
            s_int = self.read_int()

            if not f_int or not s_int:
                return None
            if not self.expect_peek(")"):
                return None

            return f_int, s_int

        return None


def get_reader(filename = "input.txt"):
    file = open(filename)
    content = file.read()
    file.close()

    return Reader(content)

def part_one():
    mem = get_reader()
    total_mul = 0
    for res in mem:
        if res != None:
            f, s = res
            total_mul += f * s
    print(f"Part one: {total_mul}")



if __name__ == "__main__":
    part_one()
