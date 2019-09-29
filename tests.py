from simple_specification import Specification


class Odd(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % 2 != 0


class Even(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % 2 == 0


class DivisibleBy(Specification):
    def __init__(self, number: int):
        self.number = number

    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % self.number == 0


def test_is_satisfied_by():
    odd = Odd()
    even = Even()
    assert odd.is_satisfied_by(1)
    assert not odd.is_satisfied_by(2)
    assert not even.is_satisfied_by(3)
    assert even.is_satisfied_by(4)


def test_and():
    even = Even()
    div3 = DivisibleBy(3)
    div5 = DivisibleBy(5)
    assert (even & div3).is_satisfied_by(6)
    assert not (even & div3).is_satisfied_by(9)
    assert (even & div3 & div5).is_satisfied_by(30)
    assert not (even & div3 & div5).is_satisfied_by(36)


def test_or():
    even = Even()
    div3 = DivisibleBy(3)
    assert (even | div3).is_satisfied_by(10)
    assert (even | div3).is_satisfied_by(15)
    assert not (even | div3).is_satisfied_by(5)


def test_invert():
    odd = Odd()
    div5 = DivisibleBy(5)
    assert (~odd).is_satisfied_by(2)
    assert not (~div5).is_satisfied_by(25)
    assert (~div5).is_satisfied_by(11)
    assert (~(odd | div5)).is_satisfied_by(6)


def test_all():
    odd = Odd()
    div3 = DivisibleBy(3)
    div5 = DivisibleBy(5)
    spec = Specification.all([odd, div3, div5])
    assert spec.is_satisfied_by(15)
    assert not spec.is_satisfied_by(30)
    assert not spec.is_satisfied_by(25)
    assert not spec.is_satisfied_by(6)


def test_any():
    even = Even()
    div15 = DivisibleBy(3) & DivisibleBy(5)
    spec = Specification.any([div15, even])
    assert spec.is_satisfied_by(2)
    assert spec.is_satisfied_by(15)
    assert spec.is_satisfied_by(30)
    assert not spec.is_satisfied_by(7)
