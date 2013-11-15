import os
from fabric.api import env
from fabric.operations import run, put,get

env.hosts = ['ct17.prod.livefyre.com',
            "ct63.prod.livefyre.com",
            "ct65.prod.livefyre.com",
            "ct66.prod.livefyre.com",
            "ct68.prod.livefyre.com",
            "ct70.prod.livefyre.com",
            "ct71.prod.livefyre.com",
            "ct72.prod.livefyre.com",]

def scp_logs():
    os.mkdir("%s"%env.host_string)
    get("/var/log/livefyre/perseids-access-2013-11-14*", "./%s/"%env.host_string)

def tar_logs():
    # make sure the directory is there!
    run("sudo tar -zcvf stream.tgz /var/log/supervisor/stream/")

def get_logs():
    scp_logs()
