from kazoo.client import KazooClient
import random 
import time 

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

path = "/livecount/hosts" 
zk.ensure_path(path)

@zk.ChildrenWatch(path)
def watcher(children):
    print children

randy = random.randint(0,100)
node_path = path + "/node%s"%(randy)
zk.create(path=node_path, value="foobar-%s"%randy, ephemeral=True)
while 1:time.sleep(1)
