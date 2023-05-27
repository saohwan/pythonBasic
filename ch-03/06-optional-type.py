# * Optional type
from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx: Optional[str] = foo("amamov")


# xxx = None


class Node:
    # 인자 값이 없을 경우 = None 으로 default 값을 설정할 수 있다.
    def __init__(self, data: int, node: Optional["Node"] = None):  # -> 자기 자신을 인스턴스에 넣을 경우 "" 사용 또는, Optional 사용.

        self.data = data
        self.node = node


node2 = Node(12)

node1 = Node(27, node2)

node0 = Node(30, node1)
