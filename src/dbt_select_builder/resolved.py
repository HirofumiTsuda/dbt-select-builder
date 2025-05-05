class DbtSelectResolvedNode:
    """Class representing a resolved node in a dbt select statement."""

    def __init__(self, statements: list[str]):
        self._statements = statements

    def build(self) -> str:
        """Build the select statement."""
        return ",".join(self.statements)

    def append(self, node: "DbtSelectResolvedNode") -> "DbtSelectResolvedNode":
        """Append a node to the current node."""
        return DbtSelectResolvedNode(self.statements + node.statements)

    @property
    def statements(self) -> list[str]:
        """Get the statements."""
        return self._statements


class DbtSelectNodeManager:
    """Class to manage the resolved nodes."""

    def __init__(self, nodes: list[DbtSelectResolvedNode]):
        self._nodes = nodes

    def aggregate_and(self, manager: "DbtSelectNodeManager") -> "DbtSelectNodeManager":
        """Aggregate the nodes with AND."""
        manager_list = []
        for node in self.get_nodes():
            manager_list.extend([node.append(another_node) for another_node in manager.get_nodes()])
        return DbtSelectNodeManager(manager_list)

    def aggregate_or(self, manager: "DbtSelectNodeManager") -> "DbtSelectNodeManager":
        """Aggregate the nodes with OR."""
        return DbtSelectNodeManager([node for node in self.get_nodes() + manager.get_nodes()])

    def build(self) -> str:
        """Build the select statement from all nodes."""
        return " ".join(node.build() for node in self.get_nodes())

    def get_nodes(self) -> list[DbtSelectResolvedNode]:
        """Get the nodes."""
        return self._nodes
