from abc import ABCMeta, abstractmethod
from dbt_select_builder.resolved import (
    DbtSelectResolvedNode,
    DbtSelectNodeManager,
)


class DbtSelectAbstractUnresolvedNode(metaclass=ABCMeta):
    """Abstract class for an unresolved node in a dbt select statement."""

    @abstractmethod
    def resolve(self) -> DbtSelectNodeManager:
        """Solve this node to a resolved state."""
        raise NotImplementedError("Subclasses must implement this method.")


class DbtSelectUnresolvedNode(DbtSelectAbstractUnresolvedNode):
    """Class representing an unresolved node in a dbt select statement."""

    def __init__(self, statement: str):
        self.statement = statement

    def resolve(self) -> DbtSelectNodeManager:
        """Solve this node to a resolved state."""
        return DbtSelectNodeManager([DbtSelectResolvedNode([self.statement])])


class DbtSelectUnresolvedAndNode(DbtSelectAbstractUnresolvedNode):
    """Class representing an unresolved AND node in a dbt select statement."""

    def __init__(self, *args: DbtSelectAbstractUnresolvedNode):
        self.nodes = args

    def resolve(self) -> DbtSelectNodeManager:
        """Solve this node to a resolved state."""
        resolved_nodes = [node.resolve() for node in self.nodes]
        manager = resolved_nodes[0]
        resolved_nodes = resolved_nodes[1:]
        for node in resolved_nodes:
            manager = manager.aggregate_and(node)
        return manager


class DbtSelectUnresolvedOrNode(DbtSelectAbstractUnresolvedNode):
    """Class representing an unresolved OR node in a dbt select statement."""

    def __init__(self, *args: DbtSelectAbstractUnresolvedNode):
        self.nodes = args

    def resolve(self) -> DbtSelectNodeManager:
        """Solve this node to a resolved state."""
        resolved_nodes = [node.resolve() for node in self.nodes]
        manager = resolved_nodes[0]
        resolved_nodes = resolved_nodes[1:]
        for node in resolved_nodes:
            manager = manager.aggregate_or(node)
        return manager
