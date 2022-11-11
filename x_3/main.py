import os
import string
import random
import csv


LETTERS = string.ascii_letters
DIGITS = string.digits
LETTERS_AND_DIGITS = LETTERS + DIGITS


class CsvHanlder:

    folder_name = 'ilovecoffee'
    file_name = 'customers.csv'
    names = [
        'may', 'phoebe', 'hayden', 'faye', 'julia',
        'kayla', 'joe', 'shawn', 'callie', 'rusty',
    ]
    fake_customers_count = 2

    def __init__(self):
        current_dir = os.path.dirname(__file__)
        base_dir = os.path.abspath(current_dir)

        self.folder_path = os.path.join(base_dir, self.folder_name)
        self.file_path = os.path.join(self.folder_path, self.file_name)
        self.mobile_suffix_created = set()

        try:
            os.mkdir(self.folder_path)
        except FileExistsError:
            pass

    def create_csv(self):
        customers = []

        for _ in range(self.fake_customers_count):
            customer_id = self._random_id()

            customers.append({
                'customer_id': customer_id,
                'customer_name': self._random_name(customer_id),
                'customer_mobile': self._random_taiwan_mobile(),
                'frequency': self._random_frequency(),
            })

        # 清掉判斷手機號碼的 cache
        self.mobile_suffix_created.clear()

        with open(self.file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=customers[0].keys())

            writer.writeheader()
            writer.writerows(customers)

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
    c.create_csv()
