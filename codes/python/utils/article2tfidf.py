'''
  compose word vector by TF-IDF vectorization
'''

# for reading directory
import os
# for read csv file (preprocessed data)
import csv
# path
path = '../data/res'
# read path's file list
fnames = os.listdir(path)
# for each files
article_words = []
for fname in fnames:
  with open(path+'/'+fname) as f:
    reader = csv.reader(f)
    articles = [tmp for tmp in reader]
    for article in articles:
      article_words += article
# remove repetition
# from 62197921 to 192672 (length of list article_words)
article_words = list(set(article_words))

# 이제 TF-IDF 뽑아야 함. sklearn으로 할 수 있는 듯