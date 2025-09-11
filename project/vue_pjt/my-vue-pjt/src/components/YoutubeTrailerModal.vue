<script setup>
defineProps({
  videoId: String,
  show: Boolean
})
defineEmits(['close'])
</script>

<template>
  <div v-if="show" class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <!-- 닫기 버튼을 오른쪽 위 고정 -->
      <button class="close-btn" @click="$emit('close')">✕</button>
      <iframe
        class="video-frame"
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative; /* 닫기 버튼 위치 기준 */
  background: #fff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.video-frame {
  width: 560px;
  height: 315px;
  border-radius: 8px;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: #ff4757;
  color: white;
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  cursor: pointer;
  font-size: 18px;
  line-height: 32px;
  text-align: center;
  transition: background 0.3s;
}
.close-btn:hover {
  background: #e84118;
}
</style>
