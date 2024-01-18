from tree.node import Node


class TreeBuilder:
    FOLDER_SEPARATOR = '\\'

    FILE_SIZE_SEPARATOR = ' '

    def _find_child(self, name: str, node: Node) -> Node | None:
        found_children = None
        for child in node.children:
            if child.name == name:
                found_children = child
        return found_children

    def _add_folder_in_tree(self, root: Node, full_path: str, size):
        folders = full_path.split(self.FOLDER_SEPARATOR)
        current_node = root
        for folder in folders[:-1]:
            child = self._find_child(folder, current_node)
            if child is None:
                child = Node(folder)
                current_node.children.add(child)
            current_node = child
        current_node.children.add(Node(folders[-1], size))

    def _get_data_from_path(self, path: str) -> (str, int | None):
        data = path.split(self.FILE_SIZE_SEPARATOR)
        full_path = data[0]
        size = None
        if len(data) == 2:
            size = int(data[1])
        return full_path, size

    def build(self, paths: list[str]) -> Node:
        root = Node(None)
        for path in paths:
            full_path, size = self._get_data_from_path(path)
            self._add_folder_in_tree(root, full_path, size)
        return root
