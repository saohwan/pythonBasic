from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = "hello wrold"
folat_var: float = 88.9
bool_var: bool = True

list_var: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, ...] = (1, 2, 3)

dic_var: Dict[str, int] = {"hello": 47, "world": 47}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    # code
    type_check(x, int)
    type_check(y, int)
    return x + y


print(cal_add(1, 3))
#
# print(cal_add("1,", "3, djadklasdjsa"))
#
# print(cal_add([1, 3], [4, 5]))

# * isinstance(obj, class)
#
print(isinstance("asdasdasw", str))
print(isinstance(88.9, float))
"""
type hint
@Param 나의 생각:
# 규모가 큰 프로그램에서 타입으로 인해 유지보수의 문제가 발생할 수 있다.
# 그것을 방지하기 위한 방법중 "Type Hint" 가 있다.
# 그렇다고 모든 함수에 "Type Hint" 를 적용하려 하지 말자. 그것또한 생산성에 문제가 있을 수 있다.
# 정말 중요한 함수라고 생각한다면 그곳에 넣어서 올바른 타입을 지정하도록 사용하자.

pyright
@Param 나의 생각:
# 종종 서비스 배포전이나 커밋전에 테스트를 대충하고 진행하는 경우가 있었다.
# 그럴 경우 타입 에러가 발생하는 경우도 있었다.
# 하지만 pyright 라는 툴을 알게 되었고 팀원들에게 테스트용으로 공유해줘야 겠다라는 생각을 했다.
"""
