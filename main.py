from file.file_manager import FileManager
from tree.tree_serializer import TreeSerializer
from tree.tree_builder import TreeBuilder


class DirectoryTreePrinter:
    _tree_serializer = TreeSerializer()

    _tree_builder = TreeBuilder()

    _file_manager = FileManager()

    def __init__(self, input_file_path, output_file_path):
        self._input_file_path = input_file_path
        self._output_file_path = output_file_path

    def print_tree(self):
        paths = self._file_manager.read_lines(self._input_file_path)
        tree = self._tree_builder.build(paths)
        tree_by_lines = self._tree_serializer.serialize(tree)
        self._file_manager.write_lines(self._output_file_path, tree_by_lines)


if __name__ == '__main__':
    app = DirectoryTreePrinter(
        r'Путь до файла чтения',
        r'Путь до файла записи'
    )
    app.print_tree()