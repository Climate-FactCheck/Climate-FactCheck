# frontend/components/results_display.py
import streamlit as st
from typing import Dict, Any

def display_factcheck_result(result: Dict[str, Any]) -> None:
    """
    팩트체크 결과를 표시합니다.
    
    Args:
        result: 팩트체크 API 응답 결과
    """
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