from dbt_select_builder.helper import check_args, convert_args_to_unresolved_node
from dbt_select_builder.unresolved import (
    DbtSelectUnresolvedAndNode,
    DbtSelectAbstractUnresolvedNode,
    DbtSelectUnresolvedOrNode,
)


def dbt_and(*args: str | DbtSelectAbstractUnresolvedNode) -> DbtSelectUnresolvedAndNode:
    """Create an AND node from the given arguments."""
    check_args(args)
    return DbtSelectUnresolvedAndNode(*convert_args_to_unresolved_node(args))


def dbt_or(*args: str | DbtSelectAbstractUnresolvedNode) -> DbtSelectUnresolvedOrNode:
    """Create an OR node from the given arguments."""
    check_args(args)
    return DbtSelectUnresolvedOrNode(*convert_args_to_unresolved_node(args))
