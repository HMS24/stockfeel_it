class PhoneBase:
    """
    把手機的共同 member 抽象化成介面，其餘各款手機繼承後實作 methods
    """

    def __init__(self):
        pass

    def special_feature(self):
        pass


class GooglePhone(PhoneBase):

    def __init__(self):
        super().__init__()

    def special_feature(self, nums):
        """
        - input: list of int

        - output: list of int

        - determine num is even and > 10

        - descending order
            use sorted(reverse=True)
        """


class TaiwanPhone(PhoneBase):

    def __init__(self):
        super().__init__()

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
