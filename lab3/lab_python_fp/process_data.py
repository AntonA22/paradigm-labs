import json
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

path = r'/Users/antonabaluev/Downloads/lab_python_fp/data_light.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
@print_result
def f1(arg):
    return sorted(Unique(list(field(data, 'job-name')), True))
@print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x, field(data, 'job-name')))
@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', filter(lambda x: 'программист' in x, field(data, 'job-name'))))
@print_result
def f4(arg):
    for job in list(filter(lambda x: 'программист' in x, field(data, 'job-name'))):
        salary = list(gen_random(1, 100000,200000))
        yield job + " " + str(salary[0])


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
