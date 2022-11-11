import os

FOLDER_NAME = 'ilovecoffee'


class CsvHanlder:

    def __init__(self):
        current_folder = os.path.dirname(__file__)
        base_dir = os.path.abspath(current_folder)

        folder_path = os.path.join(base_dir, FOLDER_NAME)

        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass

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
        3. 如果存在 csv file 取代 or 插入 ??
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
    def _random_id(length=8):
        """
        1. random module
            - 從 [a-zA-Z] 挑 1 個
            - 從 [a-zA-Z0-9] 挑 length - 1 個
            - join 上述所挑選的
        """

    def _random_name(self):
        """
        1. define names = [...]
        2. random module
            - 從 names 挑 1 個
            - join(names, self.id)
        """

    @staticmethod
    def _random_taiwan_mobile():
        """
        1. 不能重複 use cache_set 
        2. random module
            - 從 [0-9] 挑 8 個 e.g. 09`12567891`
            - 判斷前一 step 的數字 in cache_set
                - 有，回到前一 step
                - 沒有
                    - join(+8869, random_num)
                    - add random_num in set
        """

    @staticmethod
    def _random_frequency(min=0, max=20):
        """
        1. random module
            randint(min, max)
        """


if __name__ == '__main__':
    c = CsvHanlder()
