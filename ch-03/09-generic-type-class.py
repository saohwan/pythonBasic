"""
* 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""

from typing import Union, Optional, Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")


class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호를 해독하는 코드
        # 복잡
        bbb: Optional[ARM] = None
        pass


robot1 = Robot[int, int](1232131, 1823230)
robot2 = Robot[str, int]("1678131", 7687676)
robot3 = Robot[float, str](8989.131, "7878889")


class Siri(Generic[T, K], Robot[T, K]):
    pass


siri1 = Siri[int, int](1232131, 1823230)
siri2 = Siri[str, int]("1678131", 7687676)
siri3 = Siri[float, str](8989.131, "7878889")

print(siri1.arm)


# * function

def test(x: T) -> T:
    print(x)
    print(type(x))
    return x


test(898)
