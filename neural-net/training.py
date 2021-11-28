import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time

text = open('../webscraping/talk_content.csv', 'rb').read().decode(encoding='utf-8')

vocab = sorted(set(text))
print(f'{len(vocab)} unique characters')
ids_from_chars = preprocessing.StringLookup(
    vocabulary=list(vocab), mask_token=None)