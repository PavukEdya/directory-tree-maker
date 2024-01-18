from tree.node import Node


class TreeSerializer:
    ROOT_NAME = None

    def _is_root(self, node: Node):
        return node.name == self.ROOT_NAME

    def serialize(self, root: Node) -> list[str]:
        if root is None:
            return []

        tree_by_lines = []
        stack = [(root, 0)]
        while len(stack) > 0:
            current_node, indent_level = stack.pop()
            is_root = self._is_root(current_node)
            child_indent_level = 0 if is_root else indent_level + 1
            if not is_root:
                tree_by_lines.append(f'{" " * indent_level}{current_node.name}')
            for child in reversed(current_node.children):
                stack.append((child, child_indent_level))

        return tree_by_lines
