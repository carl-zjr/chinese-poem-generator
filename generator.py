# -*- coding: utf-8 -*-

###########################################################################
#                                                                         #
#                       Program : compose poems                           #
#                                                                         #
###########################################################################

import tensorflow as tf
from utils.model import rnn_model
from utils.batch import vectorization
import numpy as np
import re
import sys

start_token = 'B'
end_token = 'E'
model_dir = './model/'
corpus_file = './data/poems.txt'

lr = 0.0002

def to_word(predict, vocabs):
    t = np.cumsum(predict)       
    s = np.sum(predict)             
    sample = int(np.searchsorted(t, np.random.rand(1) * s))
    if sample > len(vocabs):
        sample = len(vocabs) - 1
    return vocabs[sample]

def generate_poem(begin_word):
    batch_size = 1
    poems_vector, word_int_map, vocabularies = vectorization(corpus_file)

    input_data = tf.placeholder(tf.int32, [batch_size, None])

    end_points = rnn_model(
                            model = 'lstm',
                            input_data = input_data,
                            output_data = None,
                            vocab_size = len(vocabularies),
                            rnn_size = 128,
                            num_layers = 3,
                            batch_size = 64,
                            learning_rate = lr)
    saver = tf.compat.v1.train.Saver(tf.compat.v1.global_variables())
    init_op = tf.group(
                        tf.compat.v1.global_variables_initializer(),
                        tf.compat.v1.local_variables_initializer())
    with tf.compat.v1.Session() as sess:
        sess.run(init_op)
        checkpoint = tf.train.latest_checkpoint(model_dir)
        saver.restore(sess, checkpoint)

        x = np.array([list(map(word_int_map.get, start_token))])

        [predict, last_state] = sess.run(
                                            [end_points['prediction'], end_points['last_state']],
                                            feed_dict = {input_data : x})
        if begin_word:
            word = begin_word
        else:
            word = to_word(predict, vocabularies)   

        Poem = ''
        count = 0
        while word != end_token:
            Poem += word
            count += 1
            if count >= 1000:
                break
            x = np.zeros((1, 1))
            x[0, 0] = word_int_map[word]
            [predict, last_state] = sess.run(
                                                [end_points['prediction'], end_points['last_state']],
                                                feed_dict = {input_data : x, end_points['initial_state'] : last_state})
            word = to_word(predict, vocabularies)
        return Poem

def poet(string):
    for begin_char in string.split(','):
        if begin_char != '':
            poem_sentences = re.split('[，。]', generate_poem(begin_char))
            for s in poem_sentences:
                if s != '' :
                    print('{}.'.format(s))

    
      
    
