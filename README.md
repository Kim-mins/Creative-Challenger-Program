# Creative-Challenger-Program

## 1. 연구의 필요성과 목적
 
  과거와 달리 인터넷을 통해 현대인들에게 제공되는 뉴스 정보의 양은 개인이 소화할 수 없을 정도로 많다. 또한 이 중 대부분의 뉴스 정보는 중복되는 내용을 포함한다. 이러한 상황 속에서 현대인들에게 제공되는 뉴스 정보 중 중복되는 것을 지우고, 비슷한 뉴스 기사들을 하나의 그룹으로 묶는 작업이 본 연구의 첫 번째 단계이다.
  
  우리 사회에는 언론이 특정 사안에 대해 중립적이거나 객관적이어야 한다는 믿음이 있다. 하지만 기자 개인이든, 언론사든 완전한 중립성이나 객관성을 견지하는 것은 불가능하다. 기자가 취재를 시작할 때 이미 기자의 문제의식이 개입되기 때문이다. 언론은 또 이를 게이트키핑한다. 언론은 특정 시간에 발생한 여러 사건 중 중요하다고 여기는 것을 취사 선택해 보도한다. 결국 언론은 어떤 관점에 기대어 사건을 보도할 수밖에 없고, 이는 언론의 정파성으로 드러난다. 언론사마다의 논조 차이가 확실히 드러남은 한국 사회에서 공공연히 알려져 왔다. 뉴스 소비자는 구독하는 언론사 기사들의 논조에 따라 인식이 바뀌기도 하고, 역으로 구독하는 신문에 따라 구독자의 정치적 성향을 판단하기도 한다. 이때, 상반되는 정파성을 가진 언론사들의 보도 관점에 따른 사건의 해석 차이로 인해 뉴스 소비자는 편향된 정보만을 받아들일 위험이 있다. 어떤 논조이든 간에 기사를 지속적으로 무비판적으로 받아들이게 되면 뉴스 소비자의 생각은 점점 그 논조에 맞게 물들어갈 것이다. 구독자들이 자신이 읽고 있는 기사의 논조와 성향을 파악하며 읽는 것과, 무비판적으로 흡수하는 것의 영향력 차이는 크다. 각 기사가 어떤 논조를 가졌는지 알고서 글을 읽을 수 있도록 돕는 것은 현대 뉴스 소비자들에게 큰 힘이 될 것이다. 따라서 각 뉴스 기사의 관점이 편향된 정도를 수치화하여 나타내는 것이 두 번째 단계이다.
  
  현존하는 인터넷 뉴스 통합 플랫폼들은 사용자들에게 종합적이고 객관적으로 뉴스를 소비할 수 있는 ‘장(場)’을 만들어주기 위해 노력한다. 뉴스 소비자들이 다양한 관점을 접할 수 있도록 여러 논조의 기사를 같은 비중으로 진열하고, 각 언론사의 판단을 존중하기 위해 해당 언론사의 지면이나 홈페이지에서 비중 있게 실린 기사를 우선 반영하는 등 편집에 상당한 주의를 기울인다. 하지만 이런 노력은 결국 편집자의 수작업을 거치기 때문에 개인의 추상적인 가치판단이 개입될 수 밖에 없고, 완전한 객관성을 유지하기가 불가능하다. 또한 경쟁력을 높이기 위해 많은 언론사들은 선정적인 기사를 앞세우는 등 전통적인 방식의 뉴스 통합 플랫폼은 고질적인 문제들을 안고 있다. 
  
  본 연구는 이러한 문제를 해결하기 위해 완전히 자동화된 알고리즘을 제안한다. 한번 알고리즘이 구성된 후에는 사람의 주관이 전혀 개입할 수 없는 구조를 통해 뉴스 소비자들은 보다 종합적인 시선으로 뉴스 기사를 받아들일 수 있다. 각 기사별 논조를 정량적으로 수치화함으로써 뉴스 기사의 성향을 분류하고, 치우침의 정도를 인식할 수 있다.
  
## 2. 연구 목표 및 독창성

  텍스트를 클러스터링 하는 알고리즘에 대한 연구는 다수 존재한다. 동일 사안에 대한 뉴스 기사를 하나의 그룹으로 클러스터링 하는 작업에서는 별도의 연구 없이 기존 알고리즘 중 하나를 채용할 수 있다. 다만 다양한 방법론 중 무엇이 본 연구에 가장 적합할지 찾아 적용하는 작업이 필요하다.
  
  텍스트를 바탕으로 감정의 극성을 판단하는 연구 또한 다양한 방법으로 선행되었다. 하지만 이러한 연구는 긍정-부정, 보수-진보 같은 식의 이분법적인 판단기준으로 감정을 대한 반면, 본 연구는 연속적인 값을 통해 기사의 논조를 판단한다. 이를 통해 같은 논조를 띄는 기사들끼리도 극성의 정도를 비교할 수 있는 알고리즘을 제시한다. 또한 기존 연구들은 하나의 기준만으로 텍스트의 논조를 판단했다. 반면에 본 연구는 사전에 설정한 여러 판단기준이 모두 활용될 수 있기에, 보다 유의미한 결론을 도출할 수 있으리라 기대한다.
  
##  3. 선행 연구 및 관련연구

  주어진 뉴스 기사 데이터에 대해 불용어 제거 등을 위해 형태소 분석을 실시한다. 많은 선행 연구 사례에서 정확도 개선을 위해 명사와 형용사 등을 제외한 나머지 형태소를 절삭했다. 본 연구에서는 몇 가지 형태소를 사용할 때 가장 좋은 성능을 보이는지 실험 후 채택할 계획이다.
    
  특정 형태소만 남겨진 형태의 기사를 TF-IDF(Term Frequency-Inverse Document Frequency)값으로 벡터화한다. 각 기사별 벡터를 이용해 기사 간 코사인 유사도를 계산하고, 주어진 임계값 이상의 유사도를 가진 기사들은 비슷한 기사라 판단해 같은 그룹으로 클러스터링한다. 이는 ”LexRank: Graph-based Lexical Centrality as Slience in Text Summarization(G.Erkan; R.Radev, 2004)“에서 소개된 이론을 활용한 것이다.
  
  이때 생성된 그룹을 1차 클러스터라 한다. 이제 같은 1차 클러스터 내 기사들의 논조를 분석한다. 다시 한번 코사인 유사도를 통해 유사한 논조의 기사들을 클러스터링한다. 이는 2차 클러스터라 한다. 2차 클러스터의 기사 데이터들에서 키워드를 추출하고, 추출된 키워드의 논조별 빈도수에 따라 BoW(Bag of Words)를 구성한다. 이후 2차 클러스터와 BoW를 이용해 기사의 논조점수를 도출한다.
  
“2차 클러스터와 BoW를 이용해 기사의 논조점수를 도출” 단계를 위한 알고리즘은 현재 뼈대만 완성된 상태이다. 연구를 진행하며 구조를 수정하고 어떠한 가중치 설정 상에서 가장 좋은 정확도를 보이는지 실험을 통해 밝힌다.

  본 연구에서 채택한 방법론과는 다른 방법으로 뉴스 기사에서 논조를 추출하는 연구 몇 가지를 소개한다. “텍스트 마이닝을 활용한 신문사에 따른 내용 및 논조 차이점 분석(감미아; 송민, 2012)“에서는 진보-보수의 잣대를 통해 각 논조에서 빈도수가 가장 높은 단어 10개를 추출해 상호 대조하여 논조 차이점을 분석했다. ”토픽 모델링을 이용한 신문 자료의 오피니언 마이닝에 대한 연구(강범일;송민;조화순, 2013)“에서는 토픽 모델링을 통해 기사의 토픽을 유추하고, 이를 통해 매체의 논조를 분석하였다. 두 연구 모두 뉴스의 논조를 분석한다는 측면에서 본 연구와 목적은 비슷하지만, 분석의 대상을 언론이나 매체로 설정한 반면 본 연구는 각 기사별 분석을 목표로 한다.
  
## 4. 과제 수행 계획

#### 데이터 수집 및 전처리
  근 3년간의 네이버 뉴스스탠드 정치 카테고리 기사를 python 웹 크롤링 라이브러리 Beautiful Soup를 사용해 수집한다. 이때 수집의 대상은 각 기사의 제목, 내용, 날짜, 언론사 등이다. 이후 수집된 기사 내용을 바탕으로 형태소 분석를 진행한다. 불용어를 제거하고, 사전에 설정된 형태소를 제외한 다른 글자를 절삭한 형태로 저장한다. 이후 정리된 각 기사별 텍스트 데이터를 TF-IDF값을 이용해 벡터로 변환한다.
#### 1차 클러스터 생성
  동일 사안에 대한 기사를 그룹으로 묶기 위해 각 벡터화된 텍스트 간 코사인 유사도를 계산한다. 유사도가 임계값(실험을 통해 가장 적합한 임계값을 찾아낸다) 이상인 기사들은 같은 사안에 대한 것이라 가정하고 같은 클러스터에 배정한다. 이를 1차 클러스터라 한다. 
#### 2차 클러스터 생성
  하나의 1차 클러스터는 동일 사안에 대한 기사들을 포함하고 있다. 비슷한 논조의 기사들을 구별하기 위해 1차 클러스터 속의 기사들에 대해 다시 한번 코사인 유사도를 계산한다. 유사도가 임계값 이상이면 같은 논조의 기사라고 판단해 동일 클러스터에 배정한다. 이때 생성된 클러스터를 2차 클러스터라 한다.
#### BoW(Bag of Words) 구성
  1차 클러스터 아래에 다수의 2차 클러스터가 존재한다. 2차 클러스터에서 빈도가 높은 단어를 그 2차 클러스터 내에서 특징적인 단어라고 가정한다. 각 2차 클러스터마다 BoW를 구성한다. 이때, 한 2차 클러스터에서 빈도가 높더라도, 다수의 2차 클러스터에서 등장하는 단어는 특징적이지 않다고 가정하고 BoW에서 제외한다. 모든 2차 클러스터의 BoW에 포함된 단어는 객관적인 키워드라 가정하고 따로 저장한다. 
#### 결과 추출
  새로운 기사가 입력되었을 때, 우선 기존 기사들과의 코사인 유사도를 이용해 해당하는 1차 클러스터에 배정한다. 이때 모든 1차 클러스터와의 유사도가 임계값을 넘지 못하는 경우 새로운 사안에 대한 기사라 가정하고 새로운 1차 클러스터를 생성해 그곳에 배정한다. 1차 클러스터에 배정된 이후, 해당 1차 클러스터 내 각 2차 클러스터마다의 BoW와 기사의 단어들을 비교해 논조점수를 도출한다. 이를 통해 새로운 기사가 입력되었을 때 기사의 논조를 수치화하여 정량적으로 나타낼 수 있다.
#### 차별적 접근방법
  지금까지 시행된 연구에서는 텍스트의 논조를 판단하는 기준으로 긍정-부정, 보수-진보와 같이 단순한 잣대 하나만이 사용되었기에, 철저히 이분법적인 기준으로 판단하거나 이산적인 변량으로 판단하는 것에 그친다. 하지만 본 연구에서는 각 기사의 논조를 수치화하여 정량적으로 나타내는 방법을 사용하기 때문에, 연속적인 값을 도출해낼 수 있을 뿐만 아니라 2차 클러스터의 수만큼의 논조 판단 기준을 도입한다. 연속적인 값을 사용하기에, 기존 이분법적인 방식보다 실제에 가까운 결과를 얻을 수 있다. 또한 한 가지 잣대가 아닌 여러 잣대를 통해 결과를 도출하는 방식 덕분에 보는 것을 통해 다양한 관점에서 해당 기사를 판단할 수 있다.

---
## TEAM NEWSpective
