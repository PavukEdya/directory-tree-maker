class FileManager:
    WRITE_SEPARATOR = '\n'

    READ_SEPARATOR = '\n'

    INCORRECT_LINE = ''

    def _line_correct(self, line: str) -> bool:
        return line != self.INCORRECT_LINE

    def _clean_line(self, line: str):
        return line.replace(self.INCORRECT_LINE, '')

    def read_lines(self, file_path: str) -> list[str]:
        lines = []
        with open(file_path, 'r') as file:
            for line in file.read().split(self.READ_SEPARATOR):
                if self._line_correct(line):
                    lines.append(line)
        return lines

    def write_lines(self, file_path: str, lines: list[str]):
        with open(file_path, 'w+') as file:
            text = self.WRITE_SEPARATOR.join(lines)
            file.write(text)
