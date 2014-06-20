from gevent import monkey
monkey.patch_all()

import gevent
import time

THOUSAND = 1000
HUN_THOUSAND = 1000 * 100

class StupidTimer(object):
    def __init__(self, func_str):
        self.func_str = func_str

    def __enter__(self,):
        self.start = time.time()

    def __exit__(self, typ, value, tb):
        self.stop = time.time()
        elapse = self.stop - self.start
        print "%s elapsed =  %s" % (self.func_str, elapse)

def foo():
    with StupidTimer("foo"):
        for i in range(20 * HUN_THOUSAND):
            if not i % (10 * THOUSAND):
                gevent.sleep(0)

def bar():
    with StupidTimer("bar"):
        # Should be twice as fast as foo
        for i in range(10 * HUN_THOUSAND):
            if not i % THOUSAND:
                gevent.sleep(0)

bar_greenlet = gevent.spawn(bar)
foo_greenlet = gevent.spawn(foo)
bar_greenlet.join()
foo_greenlet.join()


"""
output:

foo elapsed =  5.43327593803
bar elapsed =  7.62788200378
vagrant@cas1.localdev.livefyre.com:/livefyre/chronos$
vagrant@cas1.localdev.livefyre.com:/livefyre/chronos$
vagrant@cas1.localdev.livefyre.com:/livefyre/chronos$ ./env/bin/python gevent_timer_test.py
foo elapsed =  3.88819098473
bar elapsed =  5.36551403999

"""
