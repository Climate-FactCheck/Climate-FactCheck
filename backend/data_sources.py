# backend/data_sources.py
import aiohttp
from typing import List, Dict, Any

async def get_climate_data(query: str) -> Dict[str, Any]:
    """
    기후 관련 데이터를 가져옵니다.
    실제 구현에서는 신뢰할 수 있는 기후 데이터 API나 데이터베이스에 연결해야 합니다.
    """
    # 예시 구현 - 실제로는 NASA, NOAA, WMO 등의 API 연결 필요
    return {
        "temperature_data": {
            "global_average": 14.9,
            "trend": "+0.18°C per decade"
        },
        "co2_levels": {
            "current_ppm": 420,
            "pre_industrial": 280
        }
    }

async def search_scientific_sources(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    주어진 쿼리와 관련된 과학적 출처를 검색합니다.
    실제 구현에서는 Google Scholar API, PubMed API, 또는 자체 데이터베이스 필요
    """
    # 예시 구현 - 실제로는 학술 검색 API 연결 필요
    return [
        {
            "title": "Climate Change 2021: The Physical Science Basis",
            "authors": "IPCC Working Group I",
            "url": "https://www.ipcc.ch/report/ar6/wg1/",
            "year": 2021,
            "citation_count": 4500
        }
    ]
