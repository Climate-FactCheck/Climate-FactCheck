# 기후변화 팩트체크 애플리케이션 실행 방법

## 1. 환경 설정

먼저 필요한 라이브러리를 설치합니다:

```bash
pip install -r requirements.txt
```

## 2. API 키 설정

.env 파일을 프로젝트 루트 디렉토리에 생성하고 필요한 API 키를 설정합니다:

```
# .env 파일
OPENAI_API_KEY=your_openai_api_key_here
```

## 3. 백엔드 서버 실행

다음 명령어로 FastAPI 백엔드 서버를 실행합니다:

```bash
cd climate_factcheck
uvicorn backend.main:app --reload
```

서버가 실행되면 다음 주소로 API 문서에 접근할 수 있습니다:

```
http://localhost:8000/docs
```

이 페이지에서 모든 API 엔드포인트를 확인하고 테스트할 수 있습니다.

## 4. 프론트엔드 실행

별도의 터미널 창에서 Streamlit 프론트엔드를 실행합니다:

```bash
cd climate_factcheck
streamlit run frontend/app.py
```

실행하면 다음과 같은 URL이 표시됩니다:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.0.X:8501
```

브라우저에서 제공된 URL을 열면 애플리케이션 UI가 표시됩니다.

## 5. 사용 방법

1. 텍스트 입력 필드에 검증하고 싶은 기후변화 관련 주장을 입력합니다.
2. 언어를 선택합니다 (한국어 또는 영어).
3. "팩트체크 시작" 버튼을 클릭합니다.
4. 분석 결과가 화면에 표시됩니다.

## 6. 개발 및 확장

이 애플리케이션은 다음과 같은 방향으로 확장 가능합니다:

1. 더 정확한 LLM 모델 연결 (예: GPT-4, Claude 등)
2. 기후 데이터베이스 확장 및 업데이트
3. 신뢰할 수 있는 기후 데이터 API 연결 (NASA, NOAA, IPCC 등)
4. 다국어 지원 확장
5. 사용자 피드백 시스템 구현
6. 시각화 컴포넌트 확장

## 7. 배포

개발이 완료되면 다음과 같은 플랫폼에 애플리케이션을 배포할 수 있습니다:

1. 백엔드: AWS Lambda, Google Cloud Functions, Azure Functions
2. 프론트엔드: Streamlit Cloud, Heroku, Vercel
3. 컨테이너화: Docker + Kubernetes

배포 시에는 환경 변수 관리, 자동화된 CI/CD 파이프라인 구축을 권장합니다.
