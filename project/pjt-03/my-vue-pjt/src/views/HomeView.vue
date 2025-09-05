<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="home-container">
    <!-- Hero 영역 -->
    <div class="hero">
      <h1>🎬 My Movie Project</h1>
      <p>
        최신 영화 정보와 예고편, 리뷰 영상까지 한 곳에서! <br />
        지금 인기 있는 영화와 날씨에 맞는 추천 영화도 확인해보세요.
      </p>
      <RouterLink to="/movies">
        <button class="start-btn">영화 보러 가기</button>
      </RouterLink>
    </div>

    <!-- Feature 보드 (버튼형 카드) -->
    <div class="features">
      <RouterLink to="/movies" class="feature-card">
        <h3>🔥 인기 영화</h3>
        <p>TMDB에서 제공하는 최고 평점 영화들을 만나보세요.</p>
      </RouterLink>

      <RouterLink to="/review-search" class="feature-card">
        <h3>🎥 예고편 & 리뷰</h3>
        <p>유튜브 연동으로 예고편과 다양한 리뷰 영상을 볼 수 있습니다.</p>
      </RouterLink>

      <RouterLink to="/recommended" class="feature-card">
        <h3>🌤 날씨 기반 추천</h3>
        <p>현재 날씨에 맞는 영화 장르를 추천해 드립니다.</p>
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
  text-align: center;
}

/* Hero */
.hero {
  background: linear-gradient(135deg, #FFF9BD, #6610f2);
  color: black;
  padding: 50px 20px;
  border-radius: 12px;
  margin-bottom: 40px;
}
.hero h1 {
  margin-bottom: 15px;
}
.hero p {
  margin-bottom: 25px;
  line-height: 1.6;
}
.start-btn {
  background-color: #ff4757;
  color: white;
  font-size: 18px;
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.start-btn:hover {
  background-color: #e84118;
}

/* Features */
.features {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.feature-card {
  flex: 1;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
}
.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.2);
}
.feature-card h3 {
  margin-bottom: 10px;
}
</style>
