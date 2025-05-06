# `ReviewAI` - <영화리뷰 감성측정 AI 사이트(딥러닝 개인 프로젝트(2차)>🎬 <br>
1. 작업 기간 : 2025. 03. 25 ~ 2025. 03. 26
2. 주제 : 영화리뷰 감성측정 AI 사이트
3. 목적 : 영화 산업에서 소비자 선호도를 파악하는 데 중요한 영화 리뷰 데이터를 분석하고, 리뷰의 감성(긍정/부정)을 예측하는 영화리뷰 감성측정 AI 사이트 프로젝트입니다. 이를 통해 향후 영화 제작을 위한 참고 데이터를 제공하는 것을 주목적으로 합니다.
4. 주요 기능 : 영화리뷰 기반으로 감성 분석 <br>
* 영화리뷰 감성 PPT 자료 <br> <br>
<img width="958" alt="image" src="https://github.com/user-attachments/assets/9f41f602-fe31-492b-9726-aac98a39dabe" />
<br>
https://github.com/hsy2493/movielstm/issues/1#issue-3042721993 <br><br>

5. 작업 툴 : 
* 사용 언어 : python <br>
* 딥러닝 모델 정의 : LSTM 모델 <br>
* UI : streamlit <br>
* 데이터 프로파일링 (EDA) : ydata_profiling <br>
<br>

6. 결과물 : <br>

## <화면 구현(streamlit 기반)> <br>
(1) 영화리뷰 기반으로 감성 분석 <br>
<img width="1021" alt="image" src="https://github.com/user-attachments/assets/b9105d06-8696-4db3-bce0-4ef834470911" /> <br>
<설명> <br>
-리뷰 작성란에 영화 리뷰 입력 후, 예측하기 버튼 클릭 시, 영화리뷰 감성(긍정/부정)이 측정된다.<br>
- 감성 측정 - 화면구현 (streamlit 기반) 상세 코드 <br>
https://github.com/hsy2493/movielstm/blob/main/app.py<br>

## <기능 구현> <br>
(1) 데이터 수집 <br>
<img width="1009" alt="image" src="https://github.com/user-attachments/assets/0e76fbaa-26b4-4a47-8bf2-cd84e058c6e8" /> <br>
<img width="999" alt="image" src="https://github.com/user-attachments/assets/1add8bdb-f309-4cc8-ba1a-ebd88c7bfaab" /> <br>
<설명> <br>
-영화리뷰 감성 측정에 사용되는 텍스트데이터로, 테스트용(test)과 훈련용(train)의 약 150000개의 데이터를 사용했다.<br>
-테스트용은 긍정으로, 훈련용은 부정으로 사용된다. <br>
- 데이터 수집 자료(test.txt/train.txt) <br>
https://github.com/hsy2493/movielstm/tree/main/movie/dataset <br>
- 영화리뷰 데이터 수집 출처 (txt) <br>
https://github.com/e9t/nsmc <br>

(2) 데이터 분석 (EDA 기반)<br>
- 데이터 분석 과정 상세 코드 <br>
https://github.com/hsy2493/movielstm/blob/main/movie/movie.ipynb <br>
- 데이터 분석 자료 (EDA) <br>
https://github.com/hsy2493/movielstm/blob/main/movie/report/train_data_EDA_report.html <br>
<img width="865" alt="image" src="https://github.com/user-attachments/assets/656a67a8-1090-42a5-9089-7c9cca475a5d" /> <br>
<설명> <br>
-고유 ID와 Label 간의 상관관계 히트맵 <br>
-고유 ID : 감성 측정에서 실제로 사용되지는 않다. <br>
-Label : 부정과 긍정을 나타내는 감성 요인이다.
-리뷰(Document) : 단어의 빈도와 감성(부정/긍정) 관계를 분석할때 사용되는 요인이다. <br>

<br>
<img width="864" alt="image" src="https://github.com/user-attachments/assets/3a16b630-ed46-4a0e-9129-124b316545ff" /> <br>
<설명> <br>
-결측치 : 데이터 전처리로 결측치(0개)는 없다. <br>
-중복값 : 데이터 전처리로 중복값(0개)은 없다. <br> 

<br>
<img width="863" alt="image" src="https://github.com/user-attachments/assets/fcdcd3c3-c088-496d-8949-bfc00cdedf21" />
 <br>
<설명> <br>
-ID : 고유 ID  <br>
-Document : 영화 리뷰 내용  <br>
-Label : 부정 0, 긍정 1  <br>

<br>
(3) 데이터 학습 및 모델정의 <br>
- AI 모델 정의 및 학습 과정 (LSTM 모델) <br>
https://github.com/hsy2493/movielstm/blob/main/movie/movie.ipynb <br>
<img width="887" alt="image" src="https://github.com/user-attachments/assets/5786315f-a629-4612-976f-abc060506f71" /> <br>
<img width="867" alt="image" src="https://github.com/user-attachments/assets/16ef9744-075e-4542-b2c0-977c2b559f23" /> <br>
<img width="836" alt="image" src="https://github.com/user-attachments/assets/d04cea05-609f-467c-be58-e9bfa4e86a8d" /> <br>
<img width="876" alt="image" src="https://github.com/user-attachments/assets/708e2d94-6128-4233-b1e1-699d83365f0c" /> <br>
<img width="868" alt="image" src="https://github.com/user-attachments/assets/e6b584c5-e721-45c2-b8a8-6d56a69af855" /> <br>

<설명> <br>
-데이터 전처리 : 단어 5000개 선택 후, 단어 빈도수를 숫자(부정 0, 긍정 1)로 설정하여 테스트를 진행한다. <br>
-모델 정의 : LSTM 시계열 모델 정의 <br>
-컴파일 : 최적화 알고리즘 Adam로 가중치 업데이트하고, Loss로 이진 분류를 진행한다. <br>
-모델 학습 : 64개의 샘플 데이터로 총 10번의 학습을 반복하여 수행한다. 훈련용 데이터 20%를 사용한다.<br>
-학습 결과 : 모델 학습 결과를 곡선으로 시각화 한 것으로, 손실률(Accuracy)은 적고, 정확도(Loss)은 높은 편으로 나타난다. <br>

<br>
<b> 
6. 성과 <br>
- kaggle 사이트 이외에 GitHub 등에서 텍스트 데이터셋 수집이 가능함. <br>
- 텍스트(text) 데이터셋을 활용하여, 딥러닝 프로젝트 모델 정의 및 데이터 학습이 가능함. <br>
- MacOS용 라이브러리 Font를 활용하여, 막대 그래프 시각화에 AppleGothic.ttf 폰트를 적용하는 것을 학습함.
</b>







