import tensorflow as tf

@tf.function
def addition():
    return 1 + foo  # Noncompliant: using non‑local variable

foo = 4
addition()

foo = 10
addition()
