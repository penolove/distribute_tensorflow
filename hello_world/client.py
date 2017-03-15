import tensorflow as tf

with tf.device("/job:local/task:0"):
  weights_1 = tf.Variable(tf.random_normal([2, 2]))
  weights_2 = tf.Variable(tf.random_normal([2, 2]))

with tf.device("/job:local/task:1"):
  product=tf.matmul(weights_2, weights_1) 
with tf.Session("grpc://localhost:2222") as sess:
  init_op = tf.global_variables_initializer() 
  sess.run(init_op)
  for _ in range(10000):
    w=sess.run(product)
print w
