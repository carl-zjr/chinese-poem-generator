# -*- coding:utf-8 -*-

from train import paras, model_training
from generator import poet
from utils.filter import clean_cn_corpus

if __name__ == '__main__':
    # input data clean
    # clean_cn_corpus('./data/poems.txt', 'all')
    
    # training
    FLAGS = paras()
    model_training(FLAGS)

    # generate poem by input char
    poet('月')

    
