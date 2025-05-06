from dbt_select_builder import dbt_and, dbt_or
import pytest


@pytest.mark.parametrize(
    "args, expected",
    [
        (dbt_and("arg1", "arg2"), "arg1,arg2"),
        (dbt_or("arg1", "arg2"), "arg1 arg2"),
        (dbt_or(dbt_and("arg1", "arg2"), "arg3,arg4 arg5"), "arg1,arg2 arg3,arg4 arg5"),
    ],
)
def test_operator(args, expected: str) -> None:
    """Test the operator functions."""
    assert args.resolve().build() == expected
