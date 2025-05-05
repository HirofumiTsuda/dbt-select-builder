from dbt_select_builder.unresolved import (
    DbtSelectAbstractUnresolvedNode,
    DbtSelectUnresolvedNode,
    DbtSelectUnresolvedAndNode,
    DbtSelectUnresolvedOrNode,
)

DbtUnsolvedNodeType = (
    DbtSelectAbstractUnresolvedNode | DbtSelectUnresolvedAndNode | DbtSelectUnresolvedOrNode
)


def check_args(args: tuple[str | DbtUnsolvedNodeType, ...]) -> bool:
    """Check if the arguments are valid."""
    if len(args) == 0:
        raise ValueError("No arguments provided.")
    for arg in args:
        if not isinstance(arg, (str, DbtSelectAbstractUnresolvedNode)):
            raise TypeError(
                f"Invalid argument type: {type(arg)}. Expected str or DbtSelectUnresolvedNode."
            )
    return True


def convert_args_to_unresolved_node(
    args: tuple[str | DbtUnsolvedNodeType, ...],
) -> list[DbtSelectAbstractUnresolvedNode]:
    """Convert a list of strings to unresolved nodes."""
    return [_convert_str_to_unresolved_node(arg) for arg in args]


def _convert_str_to_unresolved_node(
    arg: str | DbtSelectAbstractUnresolvedNode,
) -> DbtSelectAbstractUnresolvedNode:
    """Convert a string to an unresolved node."""
    if isinstance(arg, DbtSelectAbstractUnresolvedNode):
        return arg
    if arg.count(",") == 0 and arg.count(" ") == 0:
        return DbtSelectUnresolvedNode(arg)
    and_nodes = [
        DbtSelectUnresolvedAndNode(*[DbtSelectUnresolvedNode(node) for node in split_or.split(",")])
        for split_or in arg.split(" ")
    ]
    return DbtSelectUnresolvedOrNode(*and_nodes)
