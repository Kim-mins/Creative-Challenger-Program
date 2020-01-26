'''
  python/utils.preprocessor.py
    preprocess crawled data
'''
# for reading all the files of directory
import os
# for opening csv file
import csv
# Mecab(morpheme analysis library)
from konlpy.tag import Mecab


class Preprocessor:
    def __init__(self, path):
        self.m = Mecab()
        # set data(crawled data) path
        self.path = path

    def start(self):
        # get all the files from the directory(path)
        fnames = os.listdir(self.path)
        # per each data(crawled raw data)
        for fname in fnames:
            print('Opening %s ...' % fname, )
            with open(self.path+'/'+fname) as f:
                print('done!')
                reader = csv.reader(f)
                # append csv file to list 'data' line by line
                # ex) ['20180101', 'opinion', 'maeil', 'title', 'lorem ipsum', 'https://...']
                print('csv to data ...', )
                data = [tmp for tmp in reader]
                print('done!')
                # header:
                # data[*][0]: date
                # data[*][1]: topic('opinion' here)
                # data[*][2]: journal
                # data[*][3]: title
                # data[*][4]: body
                # data[*][5]: link

                # transpose data
                print('transposing data ...', )
                data = list(map(list, zip(*data)))
                print('done!')
                # Now data is in the form like ...
                # data[0]: date
                # data[1]: topic('opinion' here)
                # data[2]: journal
                # data[3]: title
                # data[4]: body
                # data[5]: link

                # Start preprocessing

                # 1)
                # Stopword Removal: remove morpheme not relevant to the text body (Just like Preposition, article, etc.., )
                # http://openuiz.blogspot.com/2016/07/mecab-ko-dic.html --> mecab tagging symbols list
                # https://pinkwink.kr/1025 --> fun somes

                # Things to remove
                # 1. UNKNOWN (errored)
                # 2. J** (Preposition)
                # 3. E** (ending)
                # 4. X** (affix)
                # 5. S** (article, non-hanguls) --> Don't know whether I should remove non-hanguls

                # tag text body
                # datum = one article(news)
                # POSs contains all the Preprocessed articles(news) with tagging info
                # POSs: (# of articles(news), preprocessed info per article(news))
                print('processing ...', )
                POSs = [self.m.pos(datum) for datum in data[4]]
                print('done!')
                # for saving memory...
                del data

                print('processing ...', )
                res = []
                length = len(POSs)
                i = 1
                # head of strings on removal
                stop_words = ['U', 'J', 'E', 'X', 'S']
                # per article(news)
                while POSs != []:
                    print('\r({i}/{length})'.format(i, length), )
                    POS = POSs[0]
                    res1 = []
                    # for saving memory...
                    while POS != []:
                        # POS[0][1][0]: head character of tag
                        hd = POS[0][1][0]
                        # if tag is on removal,
                        if hd in stop_words:
                            pass
                        # else if we need
                        else:
                            res1.append(POS[0][0])
                        POS.remove(POS[0])
                    POSs.remove(POS)
                    res.append(res1)
                    i += 1
                del POSs
                print('done!')

                # save as csv
                print('Writing result to {fname}_res.csv ...'.format(
                    fname[:-4]),)
                with open(self.path+'/'+fname[:-4]+'_res.csv', mode='w') as f:
                    writer = csv.writer(
                        f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for row in res:
                        writer.writerow(row)
                print('done!')
                print('')
                del res
