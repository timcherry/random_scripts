from random import shuffle
import tempfile
import os
import time
import subprocess
import argparse
import re

"""
This script automates:
http://kafka.apache.org/documentation.html#basic_ops_cluster_expansion
"""

"""
Tried writing this to run in parallel(threads) but got the following:
java.io.IOException: Connection reset by peer
    at sun.nio.ch.FileDispatcherImpl.read0(Native Method)
    at sun.nio.ch.SocketDispatcher.read(SocketDispatcher.java:39)
    at sun.nio.ch.IOUtil.readIntoNativeBuffer(IOUtil.java:225)
    at sun.nio.ch.IOUtil.read(IOUtil.java:193)
    at sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:375)
    at org.apache.zookeeper.ClientCnxn$SendThread.doIO(ClientCnxn.java:859)
    at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1157)
Current partition replica assignment
"""

sleep_time = 5 * 60

json_template = """
{"partitions":
    [{"topic": "%s",
    "partition": %s,
    "replicas": [%s] }],
    "version":1
}
"""

topic_re = re.compile("Topic:(\S+)\tPartitionCount:(\d+)\tReplicationFactor:(\d+)\tConfigs:")

def shuffle_parts(broker_ids, topic, num_partitions, zookeeper_hosts):
    command = "/opt/kafka/bin/kafka-reassign-partitions.sh --reassignment-json-file %s --zookeeper %s --execute"

    for part in range(num_partitions):
        shuffle(broker_ids)
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(json_template%(topic,
                                  part,
                                  ",".join(map(str, broker_ids))))
            temp.close()
            command_str = command %(temp.name, zookeeper_hosts)
            print "Running %s" %(command_str)
            os.system(command_str)
        print "Sleeping %s"%(sleep_time)
        time.sleep(sleep_time)

def get_all_topics(zookeeper_hosts):
    command = "/opt/kafka/bin/kafka-topics.sh --describe --zookeeper %s"

    proc = subprocess.Popen(command%(zookeeper_hosts), stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    topics = []
    for line in out.splitlines():
        match = topic_re.match(line)
        if not match: continue
        (topic, num_partitions, rep_factor) = match.groups()
        topics.append((topic, int(num_partitions)))
    return topics

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shuffle Kafka Partitions.')
    parser.add_argument('--zookeeper')
    parser.add_argument('--broker_ids')

    args = parser.parse_args()
    broker_ids = args.broker_ids.split(",")
    topics = get_all_topics(args.zookeeper)

    for (topic, num_partions) in topics:
        shuffle_parts(broker_ids, topic, num_partions, args.zookeeper)
