from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
  name: str
  date_of_birth: date
  preferred_operating_system: str

  def is_adult(self) -> bool:
    today = date.today()

    age = today.year - self.date_of_birth.year

    if (today.month, today.day) < (
      self.date_of_birth.month,
      self.date_of_birth.day,
    ):
      age -= 1

    return age >= 18


imran = Person(
  "Imran",
  date(2000, 5, 10),
  "Ubuntu"
)

print(imran)
print(imran.is_adult())