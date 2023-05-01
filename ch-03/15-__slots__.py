"""
# 객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
# __slots__을 통해 변수를 관리 :
# 파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다.
# __dict__를 통해 관리되는 객체의 성능을 최적화한다. -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소한다.
"""


class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("amamov", 12)

print(wos.__dict__)

wos.__dict__["hello"] = "world"

print(wos.__dict__)


class WithSlotClass:
    __slots__ = ["name", "age"]  # => dict 형태가 아닌 list 형태로 사용하게끔 선언.

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("amamov", 12)

# print(ws.__dict__)

print(ws.__slots__)

import timeit


# * 메모리 사용량 비교


def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=9999999)
no_slot_time = timeit.repeat(repeat(wos), number=9999999)

print("use slot :", min(use_slot_time))
print("no slot :", min(no_slot_time))

# 무작정 slot을 사용하는게 좋은건 아니다, 추후에 소스코드가 완성되고 속도를 비교하여 개선이 필요하닥 생각이 된다면. 그때해도 좋다.
# 그게 리팩토링이다.
