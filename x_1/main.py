import abc

from utils import (
    fib_of,
    to_digits,
    permutate,
)


class PhoneBase(metaclass=abc.ABCMeta):

    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    @abc.abstractmethod
    def special_feature(self):
        pass


class GooglePhone(PhoneBase):

    def __init__(self):
        super().__init__(price=10, camera_count=3, screen_size=5)

    def special_feature(self, nums):
        return sorted(
            [num for num in nums if num > 10 and num % 2 == 0],
            reverse=True,
        )


class TaiwanPhone(PhoneBase):

    def __init__(self):
        super().__init__(price=20, camera_count=1, screen_size=3)

    def special_feature(self, num):
        fib_num = fib_of(num)
        units_digit, tens_digit, *_ = to_digits(fib_num)

        return permutate(tens_digit, units_digit)


if __name__ == '__main__':
    # test GooglePhone
    google_phone = GooglePhone()

    assert google_phone.price == 10
    assert google_phone.camera_count == 3
    assert google_phone.screen_size == 5

    from unittest import TestCase

    TestCase().assertListEqual(
        google_phone.special_feature([3, 43, 62, 15, 18, 22]),
        [62, 22, 18],
    )

    # test TaiwanPhone
    taiwan_phone = TaiwanPhone()

    assert taiwan_phone.price == 20
    assert taiwan_phone.camera_count == 1
    assert taiwan_phone.screen_size == 3

    assert taiwan_phone.special_feature(10) == 120
    assert taiwan_phone.special_feature(12) == 24
