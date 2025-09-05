<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import tmdb from '../api/tmdb'
import youtube from '../api/youtube'
import YoutubeTrailerModal from '../components/YoutubeTrailerModal.vue'

const route = useRoute()
const movie = ref(null)
const showTrailer = ref(false)
const videoId = ref(null)

onMounted(async () => {
  const res = await tmdb.get(`/movie/${route.params.movieId}`)
  movie.value = res.data
})

const fetchTrailer = async () => {
  if (!movie.value) return
  const res = await youtube.get('/search', {
    params: { q: `${movie.value.title} trailer` }
  })
  videoId.value = res.data.items[0]?.id.videoId
  showTrailer.value = true
}
</script>

<template>
  <div v-if="movie" class="detail-container">
    <img class="poster" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" />
    <div class="info">
      <h2>{{ movie.title }}</h2>
      <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
      <p><strong>평점:</strong> {{ movie.vote_average }}</p>
      <p><strong>줄거리:</strong> {{ movie.overview }}</p>
      <button class="youtube-btn" @click="fetchTrailer">
      <i class="fab fa-youtube"></i>
      </button>

    </div>
  </div>

  <YoutubeTrailerModal
    v-if="videoId"
    :videoId="videoId"
    :show="showTrailer"
    @close="showTrailer = false"
  />
</template>

<style scoped>
.youtube-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 40px;
  color: #ff0000; /* 유튜브 레드 */
  margin-top: 10px;
}
.youtube-btn:hover {
  color: #cc0000;
}
</style>
