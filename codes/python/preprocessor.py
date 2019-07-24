'''
  크롤링한 파일 전처리 하는 파트
  csv파일에 있는 
'''
# 디렉토리 내의 파일을 읽기 위함
import os
# csv 파일 열기
import csv
# 리스트 처리 쉽게
import numpy as np
# Mecab(형태소 분석 라이브러리)
from konlpy.tag import Mecab
m = Mecab()
# 드라이브 내의 data path 설정
path = './data'
# 해당 디렉토리 내의 모든 파일 이름을 리스트 형태로 긁어옴
fnames = os.listdir(path)
# 각 파일마다 처리
for fname in fnames:
  print(f'Opening {fname} ...', end='')
  with open(path+'/'+fname) as f:
    print('done!')
    reader = csv.reader(f)
    # csv파일 한 줄 한 줄을 data에 담음(','로 split됨)
    # ex) ['20180101', 'opinion', '세계일보', '사설 “핵단추 내 책상 위에 항상 있다”는 김정은 신년사', ..., ...]
    print(f'csv to data ...', end='')
    data = [tmp for tmp in reader]
    print('done!')
    # header:
    # data[*][0]: 날짜
    # data[*][1]: 토픽(당연히 opinion)
    # data[*][2]: 신문사
    # data[*][3]: 제목
    # data[*][4]: 본문
    # data[*][5]: 링크
    
    # transpose data
    print(f'transposing data ...', end='')
    data = list(map(list, zip(*data)))
    print('done!')
    # 이제 데이터는
    # data[0]: 날짜
    # data[1]: 토픽(당연히 여긴 다 opinion)
    # data[2]: 신문사
    # data[3]: 제목
    # data[4]: 본문
    # data[5]: 링크
    
    # 형태소 분석 및 불용어 제거
    
    # 불용어 제거: 전치사, 관사 등과 같이, 문서의 특징을 표현하는 데에 필요없는 요소들을 제거
    # 태깅 정보를 토대로 내가 불용어 리스트를 만들어도 될 듯?
    # mecha의 태깅 문자가 뭔지 .. --> http://openuiz.blogspot.com/2016/07/mecab-ko-dic.html 참고함
    # https://pinkwink.kr/1025 여기 재밌는거 많은 듯. 논조 파악도 있는 것 같음

    # 제거할 것 리스트
    # 1. UNKNOWN (오류난 것)
    # 2. J** (전치사)
    # 3. E** (선어말 어미, 어말 어미)
    # 4. X** (접두사, 접미사)
    # 5. S** (부호, 한글 이외) --> 한글 이외를 지워도 될 지 모르겠음.. 영어로 된 용어 있을 수도?
    
    # 기사 본문 품사 태깅
    # datum은 기사 하나
    # POSs에 모든 기사의 형태소 분석 + 품사 태깅된 정보를 담음
    # POSs 의미: (기사 개수, [(형태소1, 품사1), (형태소2, 품사2), ...])
    print(f'형태소 분석 및 품사 태깅 중 ...', end='')
    POSs = [m.pos(datum) for datum in data[4]]
    print('done!')
    # 메모리 부족 때문에 지움. data 내의 다른 값들이 필요하면 따로 빼야 함
    del data
    
    print('불용어 제거 중 ...', end='')
    res = []
    length = len(POSs)
    i = 1
    # 불용어 태그 첫 글자
    stop_words = ['U', 'J', 'E', 'X', 'S']
    # 메모리가 부족해서, 기사 본문을 하나씩 지우면서 진행
    while POSs != []:
      print(f'\r({i}/{length})', end='')
      POS = POSs[0]
      res1 = []
      # 메모리가 부족해서, 태깅된 형태소를 하나씩 지우면서 진행
      while POS != []:
        # POS[0][1][0]: 태그의 첫 번째 글자
        hd = POS[0][1][0]
        # 제거할 형태소면
        if hd in stop_words:
          pass
        # 필요한 형태소면
        else:
          res1.append(POS[0][0])
        POS.remove(POS[0])
      POSs.remove(POS)
      res.append(res1)
      i += 1
    del POSs
    print('done!')
    
    # csv로 저장
    print(f'Writing result to {fname[:-4]}_res.csv ...', end='')
    with open(path+'/'+fname[:-4]+'_res.csv', mode='w') as f:
      writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      for row in res:
        writer.writerow(row)
    print('done!')
    print('')
    del res
    
    
    # 진행 상황 나타내는 부분도 추가하면 재밌을 듯? 1/100