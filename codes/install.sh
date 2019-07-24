#!/bin/bash
sudo apt-get install openjdk-8-jdk python-dev python3-dev
sudo pip3 install konlpy jpype1-py3
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
tar zxfv mecab-0.996-ko-0.9.2.tar.gz
cd './mecab-0.996-ko-0.9.2' && ./configure && make && make check && sudo make install
wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
tar zxfv mecab-ko-dic-2.1.1-20180720.tar.gz
cd './mecab-ko-dic-2.1.1-20180720' && ./autogen.sh && ./configure && make && make check && sudo make install
