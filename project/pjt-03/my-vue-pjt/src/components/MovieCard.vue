<script setup>
defineProps({
  movie: Object
})
</script>

<template>
  <div class="movie-card">
    <img
      :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
      :alt="movie.title"
    />
    <h3>{{ movie.title }}</h3>
    <p>Rate: {{ movie.vote_average }}</p>
    <RouterLink :to="`/movies/${movie.id}`" class="detail-btn">
     상세보기
    </RouterLink>
  </div>
</template>

<style scoped>
.detail-btn {
  display: inline-block;
  margin-top: 8px;
  padding: 6px 12px;
  background-color: #6610f2;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-size: 14px;
  transition: background 0.3s;
}
.detail-btn:hover {
  background-color: #0b5ed7;
}

.movie-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 15px;
  width: 200px;
  text-align: center;
}
.movie-card img {
  width: 100%;
  border-radius: 6px;
  margin-bottom: 8px;
}
</style>
