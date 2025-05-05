from dbt_select_builder import helper

from dbt_select_builder.unresolved import (
    DbtSelectAbstractUnresolvedNode,
    DbtSelectUnresolvedNode,
    DbtSelectUnresolvedAndNode,
    DbtSelectUnresolvedOrNode,
)
import pytest


@pytest.mark.parametrize(
    ["args", "expected"],
    [
        (
            ("arg1", "arg2"),
            [
                DbtSelectUnresolvedNode("arg1"),
                DbtSelectUnresolvedNode("arg2"),
            ],
        ),
        (
            (
                DbtSelectUnresolvedAndNode(
                    DbtSelectUnresolvedNode("arg1"), DbtSelectUnresolvedNode("arg2")
                ),
                "arg3",
            ),
            [
                DbtSelectUnresolvedAndNode(
                    [
                        DbtSelectUnresolvedNode("arg1"),
                        DbtSelectUnresolvedNode("arg2"),
                    ]
                ),
                DbtSelectUnresolvedNode("arg3"),
            ],
        ),
        (
            (
                DbtSelectUnresolvedAndNode(
                    DbtSelectUnresolvedNode("arg1"), DbtSelectUnresolvedNode("arg2")
                ),
                "arg3,arg4 arg5",
            ),
            [
                DbtSelectUnresolvedAndNode(
                    [
                        DbtSelectUnresolvedNode("arg1"),
                        DbtSelectUnresolvedNode("arg2"),
                    ]
                ),
                DbtSelectUnresolvedOrNode(
                    [
                        DbtSelectUnresolvedOrNode(
                            DbtSelectUnresolvedNode("arg3"), DbtSelectUnresolvedNode("arg4")
                        ),
                        DbtSelectUnresolvedNode("arg5"),
                    ]
                ),
            ],
        ),
    ],
)
def test__convert_str_to_unresolved_node(
    args: tuple[str | DbtSelectAbstractUnresolvedNode, ...],
    expected: list[DbtSelectAbstractUnresolvedNode],
) -> None:
    """Test the conversion of strings to unresolved nodes."""
    # Convert the arguments to unresolved nodes
    unresolved_nodes = helper.convert_args_to_unresolved_node(args)
    # Check if the conversion is correct
    assert len(unresolved_nodes) == len(expected)
