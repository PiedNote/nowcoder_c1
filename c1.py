#-*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello WORLD'
    print stra.capitalize()


def demo_operate():
    print 1+2
    print True, not True, 2 << 3
    x = 2.3
    print x, type(x)


def demo_buildinfunction():
    x = 2
    print x+2


def demo_list():
    lista = [1, 2, 3]
    print lista
    listb = ['a', 1.1, 'b']
    print listb
    lista.extend(listb)
    print lista


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def demo_dict():
    dicta = {1: 2, 2: 'a'}
    print dicta
    dictb = {'+': add, '-': sub}
    print dictb['+'](1, 5)
    print dictb.get('-')(10, 2)
    dictb[3] = 12
    print dictb
    for key, value in dictb.items():
        print 'key value:', key, value


def demo_set():
    seta = set((1, 2, 3))
    setb = set((2, 3, 4))
    print seta
    print setb
    print seta.intersection(setb), seta & setb
    print seta.union(setb)


def demo_random():
    a = random.random()*100
    b = random.randint(5, 50)
    c = random.choice(range(0, 100, 3))
    d = random.sample(range(5, 50), 4)
    e = [1, 2, 4, 11, 32, 23, 14]
    random.shuffle(e)
    print a, b, c, d, e


def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('\d')
    p2 = re.compile('[\d]+')
    print p1.findall(str)
    print p2.findall(str)
    aa = 'yy1021-11-21ji-ew'
    p3 = re.compile('\d{4}-\d{2}-\d{2}')
    print p3.findall(aa)


if __name__ == '__main__':
    print 'hello www'
   # 注释
   # demo_string()
   # demo_operate()
   # demo_buildinfunction()
   # demo_list()
   # demo_dict()
   # demo_set()
   # demo_random()
    demo_re()
