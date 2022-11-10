import abc


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
        """
        - input: int

        - output: int

        - fibonacci
            e.g. 0, 1, 1, 2, 3, 5, ...

            - use cache
            - base case: 0, 1
            - iterate over [2, n]

        - split digit
            e.g. 152, x = 5, y = 2

            - return list: [個位, 十位, 百位, ...]
            - mod 10 取餘數 then 取商繼續 mod
                152 % 10 = 2 append
                15 % 10 = 5 append
                ...

        - permutate
            e.g. P(5 取 3), 5 * 4 * 3 = 60

            - x 的階乘取前 3 位
        """
        pass


if __name__ == '__main__':
    from unittest import TestCase

    google_phone = GooglePhone()
    taiwan_phone = TaiwanPhone()

    # test GooglePhone
    assert google_phone.price == 10
    assert google_phone.camera_count == 3
    assert google_phone.screen_size == 5

    TestCase().assertListEqual(
        google_phone.special_feature([3, 43, 62, 15, 18, 22]),
        [62, 22, 18],
    )

    # test TaiwanPhone
    assert taiwan_phone.price == 20
    assert taiwan_phone.camera_count == 1
    assert taiwan_phone.screen_size == 3
