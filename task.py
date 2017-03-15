import tensorflow as tf
import sys
if len(sys.argv)<2:
    idx=0
else:
    idx=int(sys.argv[1])
cluster = tf.train.ClusterSpec({"worker": ["invpm30:2222", "invpm29:2222"]})
#cluster = tf.train.ClusterSpec({"local": ["localhost:2222"]})
server = tf.train.Server(cluster, job_name="worker", task_index=0)
#for invpm29
#server = tf.train.Server(cluster, job_name="worker", task_index=0)
server.join()
