from gen_random import gen_random
class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self.ignore_case = ignore_case
        self.items = items
        self.index = 0
        self.unique_list = []
        self.seen = set()


    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1

            if self.ignore_case:
                item = item.lower()

            if item not in self.seen:
                self.seen.add(item)
                return item

        raise StopIteration()

    def __iter__(self):
        return self
if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data1 = Unique(data1)
    for item in unique_data1:
        print(item)

    print('\n')
    data2 = []
    for num in gen_random(5, 1, 3):
        data2.append(num)
    unique_data2 = Unique(data2)
    for item in unique_data2:
        print(item)

    print('\n')
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data3 = Unique(data3, ignore_case=True)
    for el in unique_data3:
        print(item)

    print('\n')
    data4 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data4 = Unique(data3)
    for el in unique_data4:
        print(item)