"""
#* 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않을 경우
#* 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
#* 2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Robot:
    # 클래스 변수 : 인스턴스들이 공유하는 함수.
    __population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age

        else:
            raise TypeError("invalid range to age")

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b + 1

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"we have {cls.__population} robots")


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요.")


class Bixby(Robot):
    def say_samsung(self):
        print("hello my samsung.")


class Bixbyko(Robot):
    def say_samsung(self):
        print("안녕 삼성")


class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)


Bix = BixbyCal("Saohwan", 28)

r = Bix.cal_add(2, 3)

print(r)

# 위 소스코드는 BixbyCal 클래스를 정의하는 파이썬 코드입니다. BixbyCal 클래스의 인스턴스를 생성할 때 name과 age라는 인자를 전달합니다. __init__ 메서드는 클래스 인스턴스가 생성될
# 때 자동으로 호출되는 메서드입니다. 이 메서드는 객체가 생성될 때 객체의 초기화를 담당합니다.
#
# BixbyCal 클래스의 __init__ 메서드는 Robot 클래스의 인스턴스를 생성합니다. Robot 클래스는 name과 age라는 두 개의 인자를 받아 객체를 생성합니다. BixbyCal 클래스의
# __init__ 메서드에서는 Robot 클래스의 인스턴스를 self.Robot이라는 이름의 인스턴스 변수에 할당합니다.
#
# 따라서, BixbyCal 클래스의 객체가 생성될 때 Robot 클래스의 객체도 함께 생성되고 self.Robot 인스턴스 변수에 저장됩니다. 이후 cal_add 메서드를 사용할 때
# self.Robot.cal_add로 Robot 클래스의 cal_add 메서드를 호출할 수 있게 됩니다. 이것은 BixbyCal 클래스와 Robot 클래스를 연결하는 중요한 역할을 합니다.
