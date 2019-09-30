from __future__ import annotations

from functools import reduce
from typing import Any, Iterable


class Specification:
    def is_satisfied_by(self, candidate: Any) -> bool:
        raise NotImplementedError  # pragma: nocover

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
