<script setup>
defineProps({
  movie: Object
})
</script>

<template>
  <div class="movie-card">
    <!-- 포스터 영역 -->
    <div class="poster-box">
      <img
        :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
        :alt="movie.title"
      />
    </div>

    <!-- 텍스트 영역 -->
    <div class="info-box">
      <h3>{{ movie.title }}</h3>
      <p>Rate: {{ movie.vote_average }}</p>
    </div>

    <!-- 버튼 영역 -->
    <div class="btn-box">
      <RouterLink :to="`/movies/${movie.id}`" class="detail-btn">
        상세보기
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.movie-card {
  width: 200px;
  height: 420px; /* 카드 전체 높이 고정 */
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* 세 영역이 위/중간/아래로 배치 */
  text-align: center;
  background: white;
}

/* 포스터 박스 */
.poster-box {
  flex: 0 0 auto;
}
.poster-box img {
  width: 100%;
  height: 260px;     /* 포스터 높이 고정 */
  object-fit: cover; /* 비율 유지하며 잘라냄 */
  border-radius: 6px;
}

/* 정보 박스 */
.info-box {
  flex: 1 1 auto;
  margin: 10px 0;
}
.info-box h3 {
  font-size: 16px;
  margin-bottom: 6px;
}
.info-box p {
  font-size: 14px;
  color: #444;
}

/* 버튼 박스 */
.btn-box {
  flex: 0 0 auto;
}
.detail-btn {
  display: inline-block;
  padding: 6px 12px;
  background-color: #6610f2;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-size: 14px;
}
.detail-btn:hover {
  background-color: #520dc2;
}
</style>
