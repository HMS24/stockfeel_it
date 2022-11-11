import os
import string
import random
import csv
import statistics as st
from dataclasses import (
    dataclass,
    asdict,
    fields,
)


LETTERS = string.ascii_letters
DIGITS = string.digits
LETTERS_AND_DIGITS = LETTERS + DIGITS


@dataclass
class Customers:
    customer_id: str = ""
    customer_name: str = ""
    customer_mobile: str = ""
    frequency: int = 0


class CsvHanlder:

    folder_name = 'ilovecoffee'
    file_name = 'customers.csv'
    field_names = [field.name for field in fields(Customers)]

    names = [
        'may', 'phoebe', 'hayden', 'faye', 'julia',
        'kayla', 'joe', 'shawn', 'callie', 'rusty',
    ]

    rows_count = 500

    def __init__(self):
        current_dir = os.path.dirname(__file__)
        base_dir = os.path.abspath(current_dir)

        self.folder_path = os.path.join(base_dir, self.folder_name)
        self.file_path = os.path.join(self.folder_path, self.file_name)

        # 判斷手機號碼是否重複的 cache
        self.mobile_suffix_created = set()

        try:
            os.mkdir(self.folder_path)
        except FileExistsError:
            pass

    def create_csv(self):
        customers = []

        for _ in range(self.rows_count):
            customer_id = self._random_id()

            customers.append(asdict(
                Customers(
                    customer_id=customer_id,
                    customer_name=self._random_name(customer_id),
                    customer_mobile=self._random_taiwan_mobile(),
                    frequency=self._random_frequency(),
                )
            ))

        # 每次產生完記得清掉手機號碼的 cache
        self.mobile_suffix_created.clear()

        with open(self.file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.field_names)

            writer.writeheader()
            writer.writerows(customers)

    def calculate_csv(self):
        with open(self.file_path, 'r', newline='') as f:
            reader = csv.DictReader(f, delimiter=',')

            frequency_list = [
                int(Customers(**row).frequency) for row in reader
            ]

            # use round(), 假設 frequency 的統計數字可以不用太精準
            mean = round(st.mean(frequency_list), 5)
            median = round(st.median(frequency_list), 5)
            mode = round(st.mode(frequency_list), 5)

            print(f'算術平均數: {mean:.5f}')
            print(f'中位數: {median:.5f}')
            print(f'眾數: {mode:.5f}')

    @ staticmethod
    def _random_id(length=8):
        prefix = random.choice(LETTERS)
        suffix = random.choices(LETTERS_AND_DIGITS, k=length-1)

        return prefix + ''.join(suffix)

    def _random_name(self, id):
        return f'{random.choice(self.names)}.{id}'

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
    c.calculate_csv()
