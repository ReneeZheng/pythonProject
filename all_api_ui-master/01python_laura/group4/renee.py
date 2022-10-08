from string import Template

# 字符串
a = r'hello\nworld'
print(a)

# 列表和元组
lst = ["hello", "world"]
print(lst[0])
print(lst[1])
print(lst[-1])
# 切片
num = [1, 2, 3, 4, 5, 6, 7, 8]
print(num[3:5])
print(num[-3:-1])
print(num[3:])
print(num[:])
# 步长
num1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(num1[3:6:3])
print(num1[::3])
print(num1[-3:2:-2])
# 序列相加
a = ['hello'] + ['world']
print(a)
b = 'hello,' + 'world'
print(b)
# 乘法
a = 'hello' * 3
print(a)
a = [2, 3] * 3
print(a)
# in
a = ['hello', 'world']
print('hello' in a)
print('he' in a)
# 长度、最大值、最小值
num2 = [2, 45, 23, 3435]
print(len(num2))
print(max(num2))
print(min(num2))

# 列表
print(list('hello'))
print(list({'hello': 1, 'world': 2}))
# 修改列表
a = ['hello', 'world']
a[1] = 'renee'
print(a)
# 删除列表
a = ['2', 'sz', 'sdf', 'hello', 'world']
del (a[1])
print(a)
del (a[2:])
print(a)
# 切片赋值
a = ['2', 'sz', 'sdf', 'hello', 'world']
a[:-2] = 'renee'
print(a)
a[:-2] = ['renee']
print(a)

# 列表方法
# append()
a = ['hello']
a.append('world')
print(a)
# clear()
a = ['hello']
a.clear()
print(a)
# copy()
a = [1, 2, 3]
b = a
print(b)
b[1] = 4
print(a)
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)
print(b)
# count()
a = [3, 4, 5, 4]
print(a.count(2))
print(a.count(4))
# extend()
a = [1, 3, 4]
b = [2, 5]
b.extend(a)
print(b)
print(a)
# index()
a = ['2', 'sz', 'sdf', 'hello', 'world']
b = a.index('sdf')
print(b)
# inset()
a = [1, 3, 4]
a.insert(2, 'renee')
print(a)
# pop()
a = [1, 3, 4]
b = a.pop(1)
print(b)
print(a)
# remove()
a = ['2', 'sz', 'sdf', 'hello', 'world']
a.remove('2')
print(a)
# reverse()
a = ['2', 'sz', 'sdf', 'hello', 'world']
a.reverse()
print(a)
# sort()
a = [3, 56, 2, 5, 1]
a.sort()
print(a)
a.reverse()
print(a)
a = ['a', 'abcde', 'abc', 'abcd', 'world1']
a.sort(key=len)
print(a)
a.sort(reverse=True)
print(a)
# sorted()
a = [3, 56, 2, 5, 1]
b = sorted(a)
print(a)
print(b)

# 元组
x = 1, 2, 3
print(x)
print(tuple([1, 2, 3]))
print(tuple('abc'))

# 字符串格式化
# 模板
a = Template("我是$name, 来自$org团队")
b = a.substitute(name='renee', org='HPP1')
print(b)
# 转换说明符
a = '我是%s, 来自%s团队' % ('renee', 'HPP1')
print(a)
# format
a1 = '我是{}, 来自{}团队'.format('renee', 'HPP1')
a2 = '我是{1}, 来自{0}团队'.format('HPP1', 'renee')
a3 = '我是{name}, 来自{org}团队'.format(name='renee', org='HPP1')
a4 = '我是{name}, {1}, {0}, 来自{org}团队'.format(1, 2, name='renee', org='HPP1')
print(a1)
print(a2)
print(a3)
print(a4)
lst = ['renee', 'HPP1']
a = '我是{obj[0]}, 来自{obj[1]}团队'.format(obj=lst)
print(a)
# f-string
name, org = 'renee', 'HPP1'
a = f'我是{name}, 来自{org}团队'
print(a)
# 字符串方法
# find()
str_value = 'hello world'
b = str_value.find('o')
a = str_value.find('s')
print(a)
print(b)
# join()
a = ['3', 'a', 'b']
b = '-'.join(a)
print(b)
# lower()
name = 'Renee Zheng'
name_small = name.lower()
name_big = name.upper()
print(name_small)
print(name_big)
# replace()
name = 'Renee Zheng'
name_repl = name.replace('Zheng', '郑')
print(name_repl)
import re
name = 'Renee,\'Zheng;zhang'
n = re.sub(r'[,\';]', '.', name)
print(n)
# split()
name = 'org; name; age'
lst_name = name.split(';')
print(lst_name)
# strip()
str_value = ' hello world '
value = str_value.strip()
print(value)
str_value = ' hello world ! #'
value = str_value.strip(' # !')
print(value)

# 字典
dict_value = {'name': 'renee', 'org': 'HPP1'}
print(dict_value)
dict_value = {}
print(dict_value)
lst_item = [('name', 'org'), ('renee', 'HPP1')]
dict_tans = dict(lst_item)
print(dict_tans)
dict_2 = dict(name='renee', org='HPP1')
print(dict_2)
# 使用字典
dict_value = {'name': 'renee', 'org': 'HPP1'}
value = dict_value['name']
print(value)
dict_len = len(dict_value)
print(dict_len)
dict_value['sex'] = 'female'
print(dict_value)
del dict_value['org']
print(dict_value)
is_exist_sex = 'sex' in dict_value
print(is_exist_sex)
is_exist_org = 'org' in dict_value
print(is_exist_org)
# 字典常用方法
dict_value = {'name': 'renee', 'org': 'HPP1'}
org_value = dict_value.get('org')
print(org_value)
item_value = dict_value.items()
print(item_value)
key_value = dict_value.keys()
print(key_value)
values = dict_value.values()
print(values)
pop_item = dict_value.pop('org')
print(pop_item)
person = {'name': 'linda', 'org': 'HPD1'}
dict_value.update(person)
print(dict_value)

# 赋值
a = 1, 2, 3
print(a)
m1, m2, m3 = a
print(m1, m2, m3)
x, y, *z = 1, 2, 3, 4
print(x, y, z)
m1, *m2, m3 = 'hello'
print(m1, m2, m3)
x = y = z = 'hello'
print(x, y, z)
x = 2
x += 2
print(x)

# 条件语句
name = 'renee'
if name.endswith('e'):
    print('e是结尾')
elif name.endswith('b'):
    print('是b为结尾')
else:
    print('既不是a结尾也不是b结尾')

# 循环
x = 1
while x < 10:
    print(x)
    x += 1

lst_value = ['this', 'is', 'suzhou']
for item in lst_value:
    print(item)

lst_value = ['this', 'is', 'suzhou']
for item in lst_value:
    if item == 'is':
        break
    print(item)

lst_value = ['this', 'is', 'suzhou']
for item in lst_value:
    if item == 'is':
        continue
    print(item)

name_list = ['renee', 'linda', 'amy']
for ix, value in enumerate(name_list):
    print(ix, value)

name_list = ['renee', 'linda', 'amy']
age = [23, 22, 21]
value = list(zip(name_list, age))
print(value)
for nm, ag in zip(name_list, age):
    print(nm, ag)

name_list = ['renee', 'linda', 'amy']
for i in name_list:
    if i == 'c':
        break
else:
    print('没有符合的条件')

name_lst = [1, 2, 3, 4, 5]
lst_value = [value for value in name_lst if value % 2 == 0]
print(lst_value)


# 函数
def add(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    print(add.__doc__)
    return a + b


sum_value = add(1, 2)
print(sum_value)


value = ['hello', 'world']


def change_list(new_value_lst):
    new_value_lst.append('no')


change_list(value)
print(value)


def hello_1(greeting, name):
    print(greeting, name)


def hello_2(name, greeting):
    print(name, greeting)


hello_1('hello', 'world')
hello_2('hello', 'world')


def hello_1(greeting, name='renee'):
    print(greeting, name)


hello_1(greeting='zheng')


def hello_1(greeting, name):
    print(greeting, name)


def hello_2(name, greeting):
    print(name, greeting)


hello_1(greeting='zheng', name='renee')


def hello_1(greeting, location, name='renee'):
    print(greeting, location, name)


hello_1('zheng', 'suzhou')


def hello_1(greeting, location, name='renee'):
    print(greeting, location, name)


hello_1('zheng', 'suzhou', name='linda')


def print_params(*params):
    print(params)


print_params('张三')
print_params('张三', '李四')


def print_params(x, *y, z):
    print(x, y, z)


print_params(1, 2, 3, 4, z='zhangsan')


def print_params(**kwargs):
    print(kwargs)


print_params(name='renee', org='HPP1')


def print_params(*args, **kwargs):
    print(args)
    print(kwargs)


print_params(1, 2, 3, name='renee', org='HPP1')


def add(x,y):
    print(x+y)


params = (1, 2)
add(*params)


def with_starts(name, org):
    print(name, org)


value = {'name': 'renee', 'org': 'HPP1'}
with_starts(**value)


# 类、对象
class Person:

    def say(self):
        print('我是人类')


class MalePerson(Person):

    def say(self):
        print('我是男人')


class FemalePerson(Person):

    def say(self):
        print('我是女人')


class Person:

    def __init__(self):
        self.name = 'renee'
        self.org = 'HPP1'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


person1 = Person()
print(person1.get_name())
person1.set_name('linda')
print(person1.get_name())


class Person:

    def say(self):
        print('我是父类')


class FemalePerson(Person):

    def eat(self):
        print('女人在吃东西')


person1 = FemalePerson()
person1.say()
person1.eat()


class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('aa')
        else:
            print('no')


class SongBird(Bird):

    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Sq'

# 静态方法和静态类


class MyClass:

    @staticmethod
    def show():
        print('静态方法')

    @classmethod
    def display(cls):
        print('静态类')
