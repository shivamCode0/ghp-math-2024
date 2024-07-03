from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import math
import random

Rce = Enum("Rce", ["DEFAULT"])


def clamp(minimum, value, maximum):
    return max(minimum, min(value, maximum))


@dataclass
class Person:
    rizz: float  # [0, 1]
    gdr: bool  # male=true
    age: int
    rce: Rce
    iq: int

    def mating_chance(self, other) -> float:
        if self.gdr == other.gdr:
            return 0
        return clamp(
            0,
            (
                0.28
                * (0.7 + 0.3 * self.rizz * other.rizz)
                * (1 - abs(self.rizz - other.rizz))
                * clamp(0, 1 - min(abs(self.age - other.age), 5) / 100, 1)
            )
            ** 0.8,
            1,
        )

    def death_chance(self) -> float:
        # uses age, iq, gender
        return 0.01 * clamp(0, 1 - (0.5 * self.age / 100 + 0.3 * self.iq / 100 + 0.2) * (0.9 if self.gdr else 1), 1)

    def get_offspring(self, other) -> Person:
        return Person(rizz=(self.rizz + other.rizz) / 2, gdr=bool(random.getrandbits(1)), rce=self.rce)


if __name__ == "__main__":
    p1 = Person(rizz=0.995, gdr=True, age=20, rce=Rce.DEFAULT, iq=100)
    p2 = Person(rizz=0.995, gdr=False, age=20, rce=Rce.DEFAULT, iq=100)
    print(p1.mating_chance(p2))
    print(p1.death_chance())

    p1 = Person(rizz=0.5, gdr=True, age=18, rce=Rce.DEFAULT, iq=90)
    p2 = Person(rizz=0.5, gdr=False, age=25, rce=Rce.DEFAULT, iq=100)
    print(p1.mating_chance(p2))
    print(p1.death_chance())
