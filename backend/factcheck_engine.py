# backend/factcheck_engine.py
import json
import os
from typing import List
import aiohttp
from langchain.llms import OpenAI  # 실제 프로젝트에서는 원하는 LLM 선택
from langchain.prompts import PromptTemplate
from .models import FactCheckResponse, FactSource
from .data_sources import get_climate_data, search_scientific_sources

# 기후 사실 데이터베이스 로드
with open(os.path.join("data", "climate_facts.json"), "r", encoding="utf-8") as f:
    CLIMATE_FACTS = json.load(f)

async def check_climate_claim(claim: str, language: str = "ko") -> FactCheckResponse:
    """
    기후변화 관련 주장을 분석하고 팩트체크합니다.
    
    1. LLM을 사용하여 주장 분석
    2. 신뢰할 수 있는 데이터 소스에서 관련 정보 검색
    3. 주장의 사실 여부 및 신뢰도 평가
    4. 필요시 수정된 진술 제공
    """
    # 1. LLM으로 주장 분석 (Perplexity와 유사한 방식)
    prompt = PromptTemplate(
        input_variables=["claim"],
        template="""
        다음 기후변화 관련 주장을 분석하고 팩트체크해주세요:
        
        주장: {claim}
        
        이 주장이 과학적 사실에 기반하는지 평가하고, 신뢰할 수 있는 기후 과학 자료를 기반으로
        판단해주세요. 응답은 다음을 포함해야 합니다:
        1. 주장의 사실 여부 (참/거짓/부분적 참)
        2. 신뢰도 점수 (0~1)
        3. 주장에 대한 설명
        4. 필요시 수정된 진술
        5. 참고할 수 있는 과학적 출처
        """
    )
    
    # 2. 관련 기후 데이터 및 과학적 출처 검색
    climate_data = await get_climate_data(claim)
    scientific_sources = await search_scientific_sources(claim)
    
    # 3. LLM으로 최종 분석 수행
    # 참고: 실제 구현에서는 적절한 LLM과 프롬프트 엔지니어링 필요
    llm = OpenAI(temperature=0)
    analysis_result = llm(prompt.format(claim=claim))
    
    # 분석 결과를 구조화된 형식으로 변환
    # 참고: 실제 구현에서는 LLM 응답 파싱 로직 필요
    
    # 샘플 결과 (실제 구현에서는 LLM 응답을 파싱해야 함)
    result = FactCheckResponse(
        claim=claim,
        is_factual=True,  # 예시 값
        confidence_score=0.85,  # 예시 값
        explanation="이 주장은 IPCC 보고서 데이터와 일치합니다...",  # 예시 설명
        sources=[
            FactSource(
                title="IPCC Sixth Assessment Report",
                url="https://www.ipcc.ch/report/ar6/wg1/",
                credibility_score=0.95
            )
        ],
        corrected_statement=None  # 수정이 필요한 경우에만 값 제공
    )
    
    return result
