from dataclasses import dataclass
from enum import Enum
import sys


class OperatingSystem(Enum):
  MACOS = "macOS"
  ARCH = "Arch Linux"
  UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
  name: str
  age: int
  preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
  id: int
  manufacturer: str
  model: str
  screen_size_in_inches: float
  operating_system: OperatingSystem



laptops = [
  Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
  Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
  Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
  Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


name = input("What is your name? ")

try:
  age = int(input("What is your age? "))
except ValueError:
  print("Age must be a number.", file=sys.stderr)
  sys.exit(1)


try:
  operating_system = input("What operating system do you prefer? ")
  preferred_operating_system = OperatingSystem(operating_system)
except ValueError:
  print("That is not a valid operating system.", file=sys.stderr)
  sys.exit(1)


person = Person(
  name,
  age,
  preferred_operating_system
)

number_of_laptops = 0

for laptop in laptops:
  if laptop.operating_system == person.preferred_operating_system:
    number_of_laptops += 1


print(
  f"There are {number_of_laptops} "
  f"{person.preferred_operating_system.value} laptops available."
)

for operating_system in OperatingSystem:
  number_available = 0

  for laptop in laptops:
    if laptop.operating_system == operating_system:
      number_available += 1

  if number_available > number_of_laptops:
    print(
      f"You are more likely to get a laptop if you "
      f"are willing to use {operating_system.value}."
    )

