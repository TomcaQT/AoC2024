import pyperclip
from typing import Any

def print_c(x: Any):
    print(x)
    pyperclip.copy(x)

def nums(n: list) -> list[int]:
    return list(map(int, n))
