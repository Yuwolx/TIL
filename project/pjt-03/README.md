# pjt-03

## 새로 알게된 점
### axios란?
Axios는 브라우저와 Node.js 환경에서 모두 사용할 수 있는 Promise 기반의 HTTP 클라이언트 라이브러리

- 즉, 외부 API(TMDB, Youtube, OpenWeather, Django API 등)와 통신할 때 데이터를 요청하고 응답받는 도구
- API 호출을 훨씬 간단하고 직관적으로 만들어줌
- `.env` 파일과 함께 사용하면, API Key를 코드에 직접 노출하지 않고 안전하게 관리 가능


### YoutubeReviewModal.vue
- Modal(모달)은 현재 페이지 위에 겹쳐서 나타나는 대화 상자(UI)를 말함
- Vue에서는 일반적으로 v-if / v-show로 모달의 열림/닫힘 상태를 제어함

- 구현 흐름
  1. 검색 결과 출력
      - ReviewSearchView.vue에서 Youtube API로 응답받은 영상 목록을 YoutubeCard 컴포넌트로 보여준다.
  2. 영상 클릭 이벤트 발생
      - 사용자가 특정 카드를 클릭하면 선택된 영상 ID가 상위 컴포넌트에 전달된다.
  3. 모달 열기
      - 선택된 영상 ID를 props로 YoutubeReviewModal.vue에 넘긴다.
      - 모달이 열리면 Youtube iframe을 embed 해서 해당 영상을 재생한다.
  4. 모달 닫기
      - 닫기 버튼 또는 배경 클릭 이벤트로 모달을 닫는다.


### .env 파일 활용법
- API Key를 직접 코드에 쓰면 보안상 위험
- `import.meta.env`를 통해 .env에 숨겨둔 값을 불러올 수 있음


### Axios와 Fetch 차이점
- fetch는 내장 함수라 가볍게 쓸 수 있지만, 응답을 JSON으로 변환할 때 .json() 호출이 필요하고 에러 처리도 불편함
- Axios는 응답을 자동으로 JSON으로 파싱하고, 기본 설정을 인스턴스로 관리할 수 있어 더 효율적임


## 어려웠던 점
- 비동기 처리와 로딩 상태
  - API 응답을 기다리는 동안 화면이 비는 문제가 있음
  - 사용자 경험(UX)을 고려하면 스피너나 로딩 메시지를 보여줘야 한다는 점이 중요해보임
