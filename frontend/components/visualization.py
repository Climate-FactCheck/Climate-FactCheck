# frontend/components/visualization.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, Any, List

def render_climate_trend_chart(data: Dict[str, Any]) -> None:
    """
    기후 추세 데이터를 시각화합니다.
    
    Args:
        data: 기후 추세 데이터
    """
    # 예시 데이터
    if "temperature_data" in data and "historical" in data["temperature_data"]:
        hist_data = data["temperature_data"]["historical"]
        
        # 데이터프레임 변환
        df = pd.DataFrame(hist_data)
        
        # 차트 생성
        fig = px.line(
            df, 
            x="year", 
            y="anomaly", 
            title="전 지구 온도 변화 추이 (1880-현재)",
            labels={"year": "연도", "anomaly": "온도 편차 (°C)"}
        )
        
        # 기준선 추가
        fig.add_hline(y=0, line_dash="dash", line_color="grey")
        
        # 차트 표시
        st.plotly_chart(fig, use_container_width=True)
