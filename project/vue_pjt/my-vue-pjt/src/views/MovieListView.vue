<script setup>
import { ref, onMounted } from 'vue'
import tmdb from '../api/tmdb'
import MovieCard from '../components/MovieCard.vue'

const movies = ref([])

onMounted(async () => {
  const res = await tmdb.get('/movie/top_rated')
  movies.value = res.data.results
})
</script>
<template>
  <div class="movie-list">
    <h1 class="page-title">🍿 Top Rated Movies</h1>
    <div class="card-container">
      <MovieCard
        v-for="m in movies"
        :key="m.id"
        :movie="m"
      />
    </div>
  </div>
</template>

<style scoped>
.page-title {
  text-align: center;
  font-size: 36px;
  font-weight: 800;
  margin: 30px 0;
  color: #6610f2;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
  letter-spacing: 2px;
  border-bottom: 3px solid #6610f2;
  display: inline-block;
  padding-bottom: 10px;
}
.movie-list {
  text-align: center;
}
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}
</style>
