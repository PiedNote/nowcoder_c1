#-*- encoding=UTF-8 -*-
import requests
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
    seta.add(4)
    print seta


if __name__ == '__main__':
    print 'hello www'
   # 注释
   # demo_string()
   # demo_operate()
   # demo_buildinfunction()
   # demo_list()
   # demo_dict()
    demo_set()
