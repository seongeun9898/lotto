import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="골프장 테마 4볼 로또 시뮬레이터", layout="wide")

# CSS 스타일
st.markdown("""
<style>
    .ball {
        display: inline-block;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #ff9800;
        color: white;
        text-align: center;
        line-height: 100px;
        font-size: 28px;
        font-weight: bold;
        margin: 0 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .golf-course {
        width: 100%;
        height: 200px;
        background: linear-gradient(to bottom, #7cba3d, #5a8c2d);
        border-radius: 50% 50% 0 0 / 100% 100% 0 0;
        position: relative;
        overflow: hidden;
    }
    .tree {
        position: absolute;
        bottom: 0;
        width: 60px;
        height: 120px;
    }
    .tree::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 10px;
        height: 30px;
        background-color: #8B4513;
    }
    .tree::after {
        content: '';
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 30px solid transparent;
        border-right: 30px solid transparent;
        border-bottom: 90px solid #228B22;
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.title("골프장 테마 4볼 로또 시뮬레이터")

# 골프장 배경
st.markdown('<div class="golf-course">' + 
            ''.join([f'<div class="tree" style="left: {random.randint(0, 100)}%;"></div>' for _ in range(5)]) +
            '</div>', unsafe_allow_html=True)

# 4개의 공에 대한 범위 입력
cols = st.columns(4)
ball_ranges = []
for i, col in enumerate(cols, start=1):
    with col:
        st.subheader(f"{i}번 공")
        min_val = st.number_input(f"{i}번 공 최소값", min_value=1, max_value=99, value=1, key=f"min_{i}")
        max_val = st.number_input(f"{i}번 공 최대값", min_value=1, max_value=99, value=20*i, key=f"max_{i}")
        ball_ranges.append((min_val, max_val))

# 시작 버튼
if st.button("추첨 시작"):
    # 결과를 저장할 리스트
    results = [None] * 4
    
    # 각 공에 대해 추첨 진행
    for i in range(4):
        # 애니메이션 효과
        with st.empty():
            for _ in range(10):  # 10번의 임시 숫자 표시
                temp_result = random.randint(ball_ranges[i][0], ball_ranges[i][1])
                st.markdown(f'<div class="ball">{temp_result}</div>', unsafe_allow_html=True)
                time.sleep(0.1)
        
        # 최종 결과 선택 및 표시
        results[i] = random.randint(ball_ranges[i][0], ball_ranges[i][1])
    
    # 최종 결과 표시
    st.markdown('<div>' + 
                ''.join([f'<div class="ball">{result}</div>' for result in results]) + 
                '</div>', unsafe_allow_html=True)

# 설명
st.markdown("""
## 사용 방법
1. 각 공의 최소값과 최대값을 설정합니다.
2. '추첨 시작' 버튼을 클릭합니다.
3. 각 공에 대한 추첨 결과가 순차적으로 표시됩니다.
4. 최종 결과가 화면에 나타납니다.

이 시뮬레이터는 실제 로또 추첨과는 무관하며, 단순한 재미를 위한 것입니다.
""")

