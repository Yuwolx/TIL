<script setup>
import { ref } from 'vue'
import youtube from '../api/youtube'
import YoutubeCard from '../components/YoutubeCard.vue'
import YoutubeReviewModal from '../components/YoutubeReviewModal.vue'

const query = ref('')
const videos = ref([])
const showModal = ref(false)
const selectedVideoId = ref(null)

const search = async () => {
  if (!query.value) return

  const res = await youtube.get('/search', {
    params: {
      q: `${query.value} review`
    }
  })
  videos.value = res.data.items
}

// 카드 클릭 → 모달 열기
const openModal = (videoId) => {
  selectedVideoId.value = videoId
  showModal.value = true
}
</script>

<template>
  <div class="review-page">
    <h1 class="page-title">🎥 Reviews</h1>

    <div class="search-box">
      <input v-model="query" type="text" placeholder="검색어를 입력하세요" />
      <button @click="search">검색</button>
    </div>

    <div class="results">
      <YoutubeCard
        v-for="v in videos"
        :key="v.id.videoId"
        :video="v"
        @click="openModal(v.id.videoId)"
      />
    </div>

    <YoutubeReviewModal
      v-if="selectedVideoId"
      :videoId="selectedVideoId"
      :show="showModal"
      @close="showModal = false"
    />
  </div>
</template>


<style scoped>

.results {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.page-title {
  text-align: center;
  font-size: 32px;
  font-weight: bold;
  margin: 20px 0;
  color: #6610f2;
}

.search-box {
  text-align: center;
  margin-top: 20px;
}

.search-box input {
  width: 300px;
  padding: 8px;
  font-size: 16px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
}

.search-box button {
  padding: 8px 16px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  background-color: #6610f2;
  color: white;
  cursor: pointer;
}

.search-box button:hover {
  background-color: #520dc2;
}
</style>
