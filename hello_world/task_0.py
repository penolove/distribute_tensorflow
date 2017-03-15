import tensorflow as tf
import sys
if len(sys.argv)<2:
    idx=0
else:
    idx=int(sys.argv[1])
#cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
cluster = tf.train.ClusterSpec({"local": ["localhost:2222"]})
server = tf.train.Server(cluster, job_name="local", task_index=idx)
server.join()
