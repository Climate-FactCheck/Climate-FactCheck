# frontend/app.py
import streamlit as st
import requests
import json
from typing import Dict, Any

# 환경 설정
API_URL = "http://localhost:8000/api"

# 페이지 설정
st.set_page_config(
    page_title="기후변화 팩트체커",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바
st.sidebar.title("기후변화 팩트체커")
st.sidebar.info(
    "이 애플리케이션은 기후변화에 관한 주장을 검증하고, "
    "과학적 근거를 바탕으로 팩트체크 결과를 제공합니다."
)

# 메인 컨텐츠
st.title("기후변화 팩트체커 🔍")
st.subheader("기후변화에 관한 주장을 입력하면 과학적 근거를 통해 검증해드립니다")

# 사용자 입력
with st.form(key="claim_form"):
    claim = st.text_area(
        "검증할 주장을 입력하세요:",
        height=100,
        placeholder="예: '지구 평균 온도는 지난 100년간 2도 상승했다'",
    )
    language = st.selectbox("언어 선택:", ["한국어", "영어"])
    lang_code = "ko" if language == "한국어" else "en"
    
    submit_button = st.form_submit_button(label="팩트체크 시작")

# 팩트체크 요청 및 결과 표시
if submit_button and claim:
    with st.spinner("팩트체크 중..."):
        try:
            # API 요청
            response = requests.post(
                f"{API_URL}/factcheck",
                json={"claim": claim, "language": lang_code}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # 결과 표시 섹션
                st.markdown("## 팩트체크 결과")
                
                # 진위 여부에 따른 색상과 아이콘 설정
                if result["is_factual"]:
                    st.success("✅ 사실입니다")
                    factual_status = "사실"
                    color = "green"
                elif result["confidence_score"] > 0.3:
                    st.warning("⚠️ 부분적으로 사실입니다")
                    factual_status = "부분적 사실"
                    color = "orange"
                else:
                    st.error("❌ 사실이 아닙니다")
                    factual_status = "거짓"
                    color = "red"
                
                # 신뢰도 표시
                confidence = int(result["confidence_score"] * 100)
                st.markdown(f"**신뢰도:** {confidence}%")
                
                # 신뢰도 게이지 차트
                st.progress(result["confidence_score"])
                
                # 설명
                st.markdown("### 설명")
                st.markdown(result["explanation"])
                
                # 수정된 진술 (있을 경우)
                if result["corrected_statement"]:
                    st.markdown("### 수정된 진술")
                    st.info(result["corrected_statement"])
                
                # 출처 표시
                st.markdown("### 참고 출처")
                for source in result["sources"]:
                    st.markdown(
                        f"- [{source['title']}]({source['url']}) "
                        f"(신뢰도: {int(source['credibility_score'] * 100)}%)"
                    )
            else:
                st.error(f"오류가 발생했습니다: {response.status_code}")
                st.json(response.json())
                
        except Exception as e:
            st.error(f"요청 처리 중 오류가 발생했습니다: {str(e)}")
            
# 사용 안내
if not submit_button:
    st.markdown("""
    ### 사용 방법
    1. 검증하고 싶은 기후변화 관련 주장을 입력하세요
    2. 언어를 선택하세요
    3. '팩트체크 시작' 버튼을 클릭하세요
    4. 팩트체크 결과와 과학적 근거를 확인하세요
    
    ### 주의사항
    - 가능한 한 명확하고 구체적인 주장을 입력하면 더 정확한 검증이 가능합니다
    - 검증 결과는 현재 이용 가능한 과학적 자료를 기반으로 합니다
    """)
