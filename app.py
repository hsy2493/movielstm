# streamlit 실행 : streamlit run app.py
import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model # 딥러닝 모델 
from sklearn.feature_extraction.text import TfidfVectorizer # 벡터화
from sklearn.preprocessing import MinMaxScaler # 데이터 정규화
# scikit-learn
# pip 업데이트 : pip install [패키지명] --upgrade 

# css
def load_css(): # css 로드 함수
    with open("movie/static/style.css") as f: # 외부에서 css 파일 불러오기
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
        # streamlit에서 html 해석 적용(보안상으로 html 미지원)

# css를  로드 streamlit에 적용
load_css()

@st.cache_data # streamlit 함수 캐시
# 데이터 로드 함수
def load_resources():
    # 학습된 모델 로드
    model = load_model('movie/model/movie_best_model.h5') 
    
    # 데이터 로드
    train_df = pd.read_csv("movie/dataset/ratings_train.txt", sep='\t', encoding='utf-8', usecols=['document']) # 훈련용
    train_df = train_df.dropna() # 결측치 제거
    
    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer(max_features=5000) # 5000개의 단어 선택
    X_train_tfidf = vectorizer.fit_transform(train_df['document']).toarray() # 단어를 숫자로 변환(0,1)
    # 데이터 정규화
    scaler = MinMaxScaler(feature_range=(0, 1)) # 범위 0,1로 지정
    scaler.fit(X_train_tfidf) # 문자를 숫자로 변환
    
    return model, vectorizer, scaler # 모델, 전처리(벡터화, 정규화)

model, vectorizer, scaler = load_resources() # 데이터 화면 출력

# 리뷰 감성 예측 함수
def predict_sentiment(text):
    vector = vectorizer.transform([text]).toarray() # 벡터화
    scaled = scaler.transform(vector) # 정규화
    reshaped = scaled.reshape(1, 1, scaled.shape[1]) # 시계열 데이터 형식으로 변환
    score = model.predict(reshaped)[0][0] # 0.5 기준
    return "긍정" if score > 0.5 else "부정", score # 부정 (0.5 이하): 0, 긍정 (0.5 이상): 1



# 제목과 설명
st.markdown("<h1 class='title'>영화 리뷰 감성 분석기🎬</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>영화 리뷰 내용을 입력하면 감성(부정/긍정)을 예측합니다.</p>", unsafe_allow_html=True)

# 구분선
st.markdown("---")

# 입력 
review_text = st.text_area("리뷰 작성✍️:", height=120) 

# 예측 버튼
if st.button("예측하기✅"):
    if review_text: # 입력한 경우
        sentiment, score = predict_sentiment(review_text) # 감성, 점수
        
        # 결과 표시
        if sentiment == "긍정":
            result_html = f"""
            <div class='success-message' style='background-color: rgba(40, 167, 69, 0.1); border: 1px solid #28a745;'>
                <p>감성: 😊❤️ <span style='color: #28a745; font-weight: bold;'>{sentiment}</span> (점수: {score:.4f})</p>
            </div>
            """
        else:
            result_html = f"""
            <div class='success-message' style='background-color: rgba(220, 53, 69, 0.1); border: 1px solid #dc3545;'>
                <p>감성: 😔💔 <span style='color: #dc3545; font-weight: bold;'>{sentiment}</span> (점수: {score:.4f})</p>
            </div>
            """
        
        st.markdown(result_html, unsafe_allow_html=True) 
        # 문자열 저장
        
        # 점수 시각화
        st.progress(float(score))
        
    else: # 입력하지 않은 경우
        st.markdown(
            "<div class='warning-message' style='background-color: rgba(255, 193, 7, 0.1); border: 1px solid #ffc107;'>"
            "<p>⚠️ 리뷰 텍스트를 입력해주세요.</p>"
            "</div>",
            unsafe_allow_html=True
        )

# 푸터
st.markdown("---")
st.caption("© 2025 딥러닝 프로젝트")