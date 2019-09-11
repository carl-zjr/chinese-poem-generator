# -*- coding: utf-8 -*-

###########################################################################
#                                                                         #
#          Program : chinese poems generator based on tensorflow          #
#                                                                         #
###########################################################################

import os
import numpy as np
import tensorflow as tf
from utils.model import rnn_model
from utils.batch import vectorization, generate_batch

def paras():
    tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size.')
    tf.app.flags.DEFINE_float('learning_rate', 0.01, 'learning rate.')
    tf.app.flags.DEFINE_string('model_dir', './model', 'model save path.')
    tf.app.flags.DEFINE_string('file_path', './data/poems.txt', 'file name of poems.')
    tf.app.flags.DEFINE_string('model_prefix', 'poems', 'model save prefix.')
    tf.app.flags.DEFINE_integer('epochs', 100, 'train how many epochs.')
    FLAGS = tf.app.flags.FLAGS
    return FLAGS

def model_training(FLAGS):
    if not os.path.exists(FLAGS.model_dir):
        os.makedirs(FLAGS.model_dir)
    # poems vectorization and mapping to integers, data division to many batches
    poems_vector, word_to_int, vocabularies = vectorization(FLAGS.file_path)
    batches_inputs, batches_outputs = generate_batch(FLAGS.batch_size, poems_vector, word_to_int)
    # placeholder to build up network
    input_data = tf.compat.v1.placeholder(tf.int32, [FLAGS.batch_size, None])
    output_targets = tf.compat.v1.placeholder(tf.int32, [FLAGS.batch_size, None])

    end_points = rnn_model(
                               model = 'lstm',
                               input_data = input_data,
                               output_data = output_targets,
                               vocab_size = len(vocabularies),
                               rnn_size = 128,
                               num_layers = 3,
                               batch_size = 64,
                               learning_rate = FLAGS.learning_rate)

    saver = tf.compat.v1.train.Saver(tf.compat.v1.global_variables())
    init_op = tf.group(
                            tf.compat.v1.global_variables_initializer(),
                            tf.compat.v1.local_variables_initializer())
 
    with tf.compat.v1.Session() as sess:
        summary_writer = tf.summary.FileWriter('./graph', sess.graph)
        sess.run(init_op)

        start_epoch = 0
        checkpoint = tf.train.latest_checkpoint(FLAGS.model_dir)
        if checkpoint:
            saver.restore(sess, checkpoint)
            print("# restore from the checkpoint {}".format(checkpoint))
            start_epoch += int(checkpoint.split('-')[-1])
        print('# start training...')
        try:
            print('{:^6}{:^6}{:^16}'.format('epoch', 'batch', 'loss'))
            for epoch in range(start_epoch, FLAGS.epochs):
                n = 0
                n_chunk = len(poems_vector) // FLAGS.batch_size
                for batch in range(n_chunk):
                    loss, _, _ = sess.run(
                                            [
                                                end_points['total_loss'],
                                                end_points['last_state'],
                                                end_points['train_op']],
                                            feed_dict = {
                                                            input_data: batches_inputs[n],
                                                            output_targets: batches_outputs[n]})
                    n += 1
                    print('{:^6}{:^6}{:^16}'.format(epoch, batch, loss))
                if epoch % 6 == 0:
                    saver.save(sess, os.path.join(FLAGS.model_dir, FLAGS.model_prefix), global_step = epoch)
        except KeyboardInterrupt:
            print('[Interruption] Interrupt manually, try saving checkpoint for now...')
            saver.save(sess, os.path.join(FLAGS.model_dir, FLAGS.model_prefix), global_step = epoch)
            print('[End] Last epoch were saved, next time will start from epoch {}.'.format(epoch))

