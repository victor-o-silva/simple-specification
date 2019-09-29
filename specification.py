from __future__ import annotations

from functools import reduce
from typing import Any, Iterable


class Specification:
    def is_satisfied_by(self, candidate: Any) -> bool:
        raise NotImplementedError

    def __and__(self, other: Specification) -> Specification:
        class And(Specification):
            def is_satisfied_by(inner_self, candidate: Any) -> bool:
                return self.is_satisfied_by(candidate) and other.is_satisfied_by(candidate)
        return And()

    def __or__(self, other: Specification) -> Specification:
        class Or(Specification):
            def is_satisfied_by(inner_self, candidate: Any) -> bool:
                return self.is_satisfied_by(candidate) or other.is_satisfied_by(candidate)
        return Or()

    def __invert__(self) -> Specification:
        class Not(Specification):
            def is_satisfied_by(inner_self, candidate: Any) -> bool:
                return not self.is_satisfied_by(candidate)
        return Not()

    @classmethod
    def all(cls, specs: Iterable[Specification]) -> Specification:
        return reduce(lambda a, b: a & b, specs)

    @classmethod
    def any(cls, specs: Iterable[Specification]) -> Specification:
        return reduce(lambda a, b: a | b, specs)


class Odd(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return bool(candidate % 2)


class Even(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return not candidate % 2


class DivisibleBy3(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return not candidate % 3


class DivisibleBy5(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return not candidate % 5


odd = Odd()
even = Even()
div3 = DivisibleBy3()
div5 = DivisibleBy5()
# specification = (div3 & div5) | even
specification = Specification.any([(div3 & div5), even])
# specification = Specification.all([odd, div3, div5])
print(specification.is_satisfied_by(30))

