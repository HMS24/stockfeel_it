import os
import string
import random


LETTERS = string.ascii_letters
DIGITS = string.digits
LETTERS_AND_DIGITS = LETTERS + DIGITS


class CsvHanlder:

    def __init__(self):
        self.folder_name = 'ilovecoffee'
        self.names = [
            'may', 'phoebe', 'hayden', 'faye', 'julia',
            'kayla', 'joe', 'shawn', 'callie', 'rusty',
        ]
        self.mobile_suffix_created = set()

        self._create_folder(self.folder_name)

    def create_csv(self):
        """
        1. generate customers
            - use dataclasses 定義屬性 ??
            - prepare fake_customers
                tuple as row (
                    customer_id: random_id(),
                    customer_name: random_name(),
                    customer_mobile: random_mobile(),
                    frequency: random_frequency(),
                )
        2. csv module + context
            - write header
            - write rows
        3. clear set
        4. 如果存在 csv file 取代 or 插入 ??
            先實作取代，比較簡單。
            插入但要不重複的 mobile number 可以用 schema unique constraint
        """

    def calculate_csv(self):
        """
        1. csv module + context
            - dictreader
            - prepare rows
            - statistics module compute mean, median and mode
            - 小數點後 5 位
                - round() 浮點數不太精確
                - Decimal object 
                frequency 不是需要精確計算的欄位，用 round 簡單
        """

    @staticmethod
    def _create_folder(name):
        current_folder = os.path.dirname(__file__)
        base_dir = os.path.abspath(current_folder)

        folder_path = os.path.join(base_dir, name)

        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass

    @staticmethod
    def _random_id(length=8):
        prefix = random.choice(LETTERS)
        suffix = random.choices(LETTERS_AND_DIGITS, k=length-1)

        return prefix + ''.join(suffix)

    def _random_name(self, id):
        name = random.choice(self.names)

        return f'{name}.{id}'

    def _random_taiwan_mobile(self):
        COUNTRY_LOCAL_CODE = '+8869'
        SUFFIX_LENGTH = 8

        mobile = ''

        while (
            not mobile
            or suffix in self.mobile_suffix_created
        ):
            suffix = ''.join(random.choices(DIGITS, k=SUFFIX_LENGTH))
            mobile = f'{COUNTRY_LOCAL_CODE}{suffix}'

        self.mobile_suffix_created.add(suffix)

        return mobile

    @staticmethod
    def _random_frequency(min=0, max=20):
        return random.randint(min, max)


if __name__ == '__main__':
    c = CsvHanlder()
