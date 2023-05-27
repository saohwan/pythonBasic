from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# * type alias

Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]

X = int

x: X = 8


def cal(v: Value) -> Value:
    # ddmasda
    return v


# * dict alias

ddd: Dict[str, Union[str, int]] = {"heelo": "world", "world": "wow!!", "hee": 17}


class Point(TypedDict):
    x: int
    y: float
    z: str


point: Point = {"x": 8, "y": 8.4, "z": "12"}
