'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-21 09:10:46
LastEditors: shuike
LastEditTime: 2021-01-21 09:11:22
FilePath: /droneLanding/python/Tello/listenList.py
'''

'''
观察者模式
'''
class Observable(object):
    '''
    被监听的对象，实现类需要具体增加被监听的资源
    '''
    def __init__(self):
        self.__observers = []

    @property
    def observers(self):
        return self.__observers

    def has_observer(self):
        return False if not self.__observers else True

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def listener(self, obj=None):
        for observer in self.__observers:
            observer.update(self, obj)


class Observer(object):
    '''
    观察者，当观察的对象发生变化时，依据变化情况增加处理逻辑
    '''
    def update(self, observable, obj):
        pass




'''
基于观察者模式，实现一个简单的消息队列，当队列中有消息时，将消息发送给监听者
'''
class MyQueue(Observable):
    def __init__(self):
        super().__init__()
        self.__resource = []

    def has_message(self):
        return True if self.__resource else False

    def queue_size(self):
        return len(self.__resource)

    def add_resource(self, res):
        self.__resource.append(res)
        print("新消息进入，推送...")
        self.listener(obj=res)


class MySubOdd(Observer):
    def update(self, observable, obj):
        if isinstance(observable, MyQueue) and int(obj) % 2 != 0:
            print("I'm MySubOdd, Get Message {} from MyQueue.".format(obj))


class MySubEven(Observer):
    def update(self, observable, obj):
        if isinstance(observable, MyQueue) and int(obj) % 2 == 0:
            print("I'm MySubEven, Get Message {} from MyQueue.".format(obj))


if __name__ == "__main__":
    my_queue = MyQueue()        # 初始化一个队列
    my_sub_odd = MySubOdd()     # 初始化奇数监听者
    my_sub_even = MySubEven()   # 初始化偶数监听者

    # 将两个监听者加入监听队列
    my_queue.add_observer(my_sub_odd)
    my_queue.add_observer(my_sub_even)

    # 添加资源进队列
    my_queue.add_resource("1")
    my_queue.add_resource("3")

    my_queue.add_resource("2")
    my_queue.add_resource("4")