"""
#* 추상화 : abstraction
#* 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
#* 공토의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인한다.
#* __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class Robot:
    """
    [Robot Class]
    Author: 이상완
    Role: ????
    """

    # 클래스 변수 : 인스턴스들이 공유하는 함수.
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name
        # self.code = code
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots")

    @staticmethod
    def this_is_robot_class():
        print("yes!!")


siri = Robot("siri")
jarvis = Robot("jarvis")
bixby = Robot("bixby")

# print(Robot.__dict__)
#
# print(siri.__dict__)
#
# print(jarvis.__dict__)
#
# siri.cal_add(2, 3)
#
# print(siri.population)
#
# siri.how_many()
#
# Robot.say_hi(siri)

# print(dir(siri))
# print(dir(Robot))
#
# print(Robot.__doc__)
#
# print(siri.__class__)

print(Robot.this_is_robot_class())
print(siri.this_is_robot_class())
