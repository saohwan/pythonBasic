"""
* 1. [클래스 상속]
* 2.  자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
* 3. 메서드 오버라이딩
* 4. super()
* 5. Python의 모든 클래스는 object 클레스를 상속한다. : 모든 것은 객체이다.
* MyClass.mro() --> 상속 관계를 보여준다.
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
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots")


class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b


siri = Siri("iphone8")

print(Siri.mro())  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

print(object)

print(dir(object))

print(object.__name__)

print(object.__repr__)

print(int.mro())
print(int.__init__(8.9))
print(int(8.9))


class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B, C):
    pass


print(D.mro())

