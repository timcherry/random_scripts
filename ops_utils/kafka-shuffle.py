from random import shuffle
import tempfile
import os
import time

topic_name = "pns.stream"
num_partitions = 2
broker_ids  = [6, 7, 8]
sleep_time = 5 * 60
zookeeper_hosts = "zookeeper2.staging.livefyre.com,zookeeper3.staging.livefyre.com,zookeeper5.staging.livefyre.com"

command = "/opt/kafka/bin/kafka-reassign-partitions.sh --reassignment-json-file %s --zookeeper %s --execute"

json_template = """
{"partitions":
    [{"topic": "%s",
    "partition": %s,
    "replicas": [%s] }],
    "version":1
}
"""
for part in range(num_partitions):
    shuffle(broker_ids)
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(json_template%(topic_name,
                                  part,
                                  ",".join(map(str, broker_ids))))
        temp.close()
        command_str = command %(temp.name, zookeeper_hosts)
        print "Running %s" %(command_str)
        os.system(command_str)
        print "Sleeping %s"%(sleep_time)
        time.sleep(sleep_time)

