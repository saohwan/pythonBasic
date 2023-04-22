"""
#* polymorphism
#* 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.
#* 같은 형태의 코드가 다른 동작을 하도록 하는 것
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
        return a + b

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
        print("안녕하세요.")
