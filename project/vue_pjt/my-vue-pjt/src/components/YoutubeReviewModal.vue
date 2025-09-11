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
      <iframe
        width="560"
        height="315"
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
      <button class="close-btn" @click="$emit('close')">닫기</button>
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
  background: #fff;
  padding: 20px;
  border-radius: 12px;
}
.close-btn {
  margin-top: 10px;
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  background-color: #6610f2;
  color: white;
  cursor: pointer;
}
.close-btn:hover {
  background-color: #520dc2;
}
</style>
