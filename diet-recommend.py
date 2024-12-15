import streamlit as st
import openai

# OpenAI API 설정
openai.api_key = ""  # 발급받은 API 키를 여기에 넣으세요

# 페이지 기본 설정
st.set_page_config(page_title="맞춤형 피트니스 추천 시스템", layout="wide", initial_sidebar_state="expanded")

# 사용자 정의 CSS 추가 (다크 모드 스타일 적용)
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;  /* 전체 배경 어둡게 */
        color: #ffffff;  /* 기본 텍스트를 밝게 */
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2 {
        color: #ffcc00;  /* 헤더 텍스트를 밝은 노란색으로 */
        font-weight: bold;
    }
    .block-container {
        padding: 1rem 2rem;
    }
    .stButton button {
        background-color: #ff6347;  /* 버튼을 밝은 색으로 */
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 1.3rem;
        font-weight: bold;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .stButton button:hover {
        background-color: #ff4500;
        color: white;
        transform: scale(1.05);
    }
    .stTextInput>div>input {
        background-color: #333333;  /* 입력 상자 어둡게 */
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1rem;
    }
    .stSelectbox>div>div>div>button {
        background-color: #333333;  /* 셀렉트 박스 어둡게 */
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1rem;
    }
    .stTable {
        margin-top: 2rem;
    }
    .stMarkdown p {
        color: white !important;  /* 마크다운 텍스트를 흰색으로 */
        font-size: 1.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# OpenAI API를 호출하는 함수
def get_recommendations(type, user_info):
    if type == "운동":
        prompt = f"{user_info}\n위 정보를 바탕으로 7일 운동 계획을 세우고 칼로리 소모량을 포함하여 추천해 주세요."
    elif type == "식단":
        prompt = f"{user_info}\n위 정보를 바탕으로 7일치 식단 계획을 아침, 점심, 저녁으로 나눠서 추천해 주세요."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a fitness and nutrition expert."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.7
    )

    return response.choices[0].message['content']

# 운동 및 식단 계획을 텍스트 형식으로 깔끔하게 출력하는 함수
def format_plan_to_text(plan_data):
    formatted_text = ""
    for day in plan_data:
        formatted_text += f"**{day['날짜']}**\n"
        formatted_text += f"- 운동 내용: {day['운동 내용']}\n"
        formatted_text += f"- 운동 시간: {day['운동 시간']}\n"
        formatted_text += f"- 칼로리 소모량: {day['칼로리 소모량']}\n\n"
    return formatted_text

# 타이틀 섹션
st.title("💪 맞춤형 피트니스 추천 시스템")

# 사용자 입력 받기
col1, col2 = st.columns(2)

with col1:
    st.header("📋 운동 계획 추천")
    height = st.number_input("키 (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("체중 (kg)", min_value=30, max_value=200, value=70)
    goal_weight = st.number_input("목표 체중 (kg)", min_value=30, max_value=200, value=65)
    age = st.number_input("나이", min_value=10, max_value=100, value=25)
    gender = st.selectbox("성별", ["남성", "여성"])
    activity_level = st.selectbox("활동 수준", ["저활동", "중간활동", "고활동"])

    user_info = (
        f"사용자 정보: 키 {height}cm, 체중 {weight}kg, 목표 체중 {goal_weight}kg, 나이 {age}, "
        f"성별 {gender}, 활동 수준 {activity_level}."
    )

    # 운동 계획 추천 버튼
    if st.button("🏃‍♂️ 운동 계획 추천 받기"):
        workout_plan = get_recommendations("운동", user_info)
        st.markdown(f"**AI 추천 운동 계획**\n\n{workout_plan}")

with col2:
    st.header("🍽️ 식단 계획 추천")
    if st.button("🍲 식단 계획 추천 받기"):
        diet_plan = get_recommendations("식단", user_info)
        st.markdown(f"**AI 추천 식단 계획**\n\n{diet_plan}")
