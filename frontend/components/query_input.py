# frontend/components/query_input.py
import streamlit as st
from typing import Tuple

def render_query_input() -> Tuple[str, str]:
    """
    사용자 쿼리 입력 컴포넌트를 렌더링하고 입력값을 반환합니다.
    
    Returns:
        Tuple[str, str]: (claim, language_code)
    """
    with st.form(key="claim_form"):
        claim = st.text_area(
            "검증할 주장을 입력하세요:",
            height=100,
            placeholder="예: '지구 평균 온도는 지난 100년간 2도 상승했다'",
        )
        
        language = st.selectbox("언어 선택:", ["한국어", "영어"])
        lang_code = "ko" if language == "한국어" else "en"
        
        submit_button = st.form_submit_button(label="팩트체크 시작")
        
    return claim if submit_button else "", lang_code
