# Testing Google STT for capstone project 2021
- 2021.09.01 ~ 2021.12.09
- EWHA WOMANS UNIV. Capstone Project 2021
- STRAT TEAM 21 십중팔구 - 김소민, 김윤아, 이서정, 정세영

# Datasets
1. [YOUTUBE : MIT Introduction to Deep Learning](https://youtu.be/5tvmMX8r_OM)
- Google STT API로 Text 변환 후 요약 진행

2. [Kaggle : News Summary Dataset](https://www.kaggle.com/sunnysai12345/news-summary)
- T5 Transformer2_wandb에서 훈련 데이터로 사용

# Process
![Snipaste_2021-12-09_23-07-21](https://user-images.githubusercontent.com/53165813/145411773-9afdfe68-541d-4dd2-9ddb-10139722112c.png)

# Used API
1. Google STT API 
  - Google STT API를 이용해 youtube 동영상의 음성 추출해 텍스트로 변환

# Models
## TextRank
1. Gensim Word2vec embeddings 
- 단어를 임베딩 벡터로 변환
- https://radimrehurek.com/gensim/models/word2vec.html

3. TF-IDF : 단어의 빈도와 역문서빈도를 사용하여 DTM 내의 각 단어들마다 중요한 정도를 가중치로 주는 방법 


## BERT
- official github repository : https://github.com/google-research/bert
- bert-extractive-summarizer 라이브러리를 설치하여 추출 요약


## T5 TransFromer
1. T5_Transformer_1
  - HuggingFace 의 최첨단 변압기 프레임 워크와 PyTorch을 사용하여 결과 요약
2. T5_Transformer_2_wandb
  - News Summary Dataset를 훈련 데이터로 사용하여 모델 훈련 진행 후 요약
3. T5_Transformer_3
  - 1번을 유사하게 변형 후 요약

# Extra Link
1. [User Requirement](https://docs.google.com/spreadsheets/d/1OVuZhWP_lQq1vOBxY2rHruc4SW65KThjoJkRXUvqLa4/edit#gid=0) 
2. [Technology Video](https://youtu.be/rzK2M3J9DP0)
3. [Figma](https://www.figma.com/file/rrCpEKWmuIyt6eOQ0kb0wM/AWESUM?node-id=0%3A1)
4. [Product Manual](https://www.miricanvas.com/v/1rl2c8)
