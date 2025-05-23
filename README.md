# dbt-select-builder

## What is this repository?

A builder to help you create a select / exclude clause for dbt.

## Why does this library exist?

The format of select / exclude clauses in dbt supports only `','` and `' '` (white-space) denoting 'and' and 'or', respectively. Besides parentheses are not supported. Therefore, to create a complicated select clause you often decompose factors into one-line. An example is shown below.

```math
A \land (B \lor C) \Rightarrow A,B \ A,C
``` 

The left side is a logical expression and the right side is a dbt-select expression. Since parentheses are not supported, it is required to expand your logical expression by yourself.

## How is this library installed?

This library has been uploaded to [`PyPI`](https://pypi.org/project/dbt-select-builder/).

You can get that using the `pip` command.

```sh
pip install dbt-select-builder
```

## How is this library used?

Using this library, the following can be written in python code in a straightforward way.

```python
from dbt-select-builder import (
    dbt_and,
    dbt_or
)

dbt_and(
    "A",
    dbt_or(
        "C", "D"
    )
).resolve().build()
# "A,C A,D" is returned!
```

Also, strings with `','` and `' '` are supported.

```python
from dbt-select-builder import (
    dbt_and,
    dbt_or
)

dbt_and(
    "A,B",
    "C D"
).resolve().build()
# "A,B,C A,B,D" is returned!
```

