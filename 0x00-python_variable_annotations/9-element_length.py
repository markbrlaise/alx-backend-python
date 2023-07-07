#!/usr/bin/env python3
"""task_9
"""

from ast import List
from typing import Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
