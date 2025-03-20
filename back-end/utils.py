import numpy as np
from sklearn.preprocessing import LabelEncoder

def pad_tags(tags, max_tags=5):
    tag_list = tags.split(',')
    tag_list = tag_list[:max_tags]

    while len(tag_list) < max_tags:
        tag_list.append('')

    return tag_list
