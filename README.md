# simple_specification

A simple pythonic implementation of the [Specification Pattern](https://www.martinfowler.com/apsupp/spec.pdf).

## Examples

### Creating specification classes to check integer numbers

```python
from simple_specification import Specification


# hardcoded specification
class Odd(Specification):
    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % 2 != 0


# parametrized specification
class DivisibleBy(Specification):
    def __init__(self, number: int):
        self.number = number

    def is_satisfied_by(self, candidate: int) -> bool:
        return candidate % self.number == 0
```

### Instantiating the specifications

```python
>>> odd = Odd()
>>> even = ~odd
>>> div3 = DivisibleBy(3)
>>> div5 = DivisibleBy(5)
```

### Using specifications: method `is_satisfied_by(candidate)`

```python
>>> odd.is_satisfied_by(1)
True
>>> odd.is_satisfied_by(2)
False
>>> even.is_satisfied_by(3)
False
>>> even.is_satisfied_by(4)
True
>>> div3.is_satisfied_by(9)
True
>>> div5.is_satisfied_by(12)
False
```

### Combining specifications: operators `&` and `|`

```python
>>> # AND
>>> (even & div3).is_satisfied_by(6)
True
>>> (even & div3).is_satisfied_by(9)
False
>>> (even & div3 & div5).is_satisfied_by(30)
True
>>> (even & div3 & div5).is_satisfied_by(36)
False
>>>
>>> # OR
>>> (even | div3).is_satisfied_by(10)
True
>>> (even | div3).is_satisfied_by(15)
True
>>> (even | div3).is_satisfied_by(5)
False
```


### Negating specifications: operator `~`

```python
>>> # Always surround the negation with parenthesis
>>> (~odd).is_satisfied_by(2)
True
>>> (~div5).is_satisfied_by(25)
False
>>> (~div5).is_satisfied_by(11)
True
>>> (~(odd | div5)).is_satisfied_by(6)
True
>>> (~(odd | div5)).is_satisfied_by(7)
False
```

### Combining a list of specifications with `&`: class method `Specification.all(specs)`

```python
>>> all_spec = Specification.all([~even, div3, div5])
>>> all_spec.is_satisfied_by(15)
True
>>> all_spec.is_satisfied_by(30)
False
>>> all_spec.is_satisfied_by(25)
False
>>> all_spec.is_satisfied_by(6)
False
```

### Combining a list of specifications with `|`: class method `Specification.any(specs)`

```python
>>> div15 = DivisibleBy(3) & DivisibleBy(5)
>>> any_spec = Specification.any([div15, even])
>>> any_spec.is_satisfied_by(2)
True
>>> any_spec.is_satisfied_by(15)
True
>>> any_spec.is_satisfied_by(30)
True
>>> any_spec.is_satisfied_by(3)
False
>>> any_spec.is_satisfied_by(5)
False
```