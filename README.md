# helloworld
## simple task
create two different process for tensor server:
```
python task_0.py
```
```
python task_0.py 1
```

## simple client
```
python client.py
```


which variables stores in tash 0,
executeed naive matrix multiplication in task 1
```
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

```

# Between-graph replication
 cloned from https://github.com/ischlag/distributed-tensorflow-example


# a simple split VGG16 testing model into two part [~pool3] [pool3~fc]

the messy code was shown in Cient_trail.ipynb

and before runing the ipynb ,you need to edit task.py and runs in both invpm30,invpm29(you can change it to your host)


the required pretrain vgg face model are here
[link](https://drive.google.com/open?id=0B0GW3-McRihWM0VsWkh1Q3JYTE0)
