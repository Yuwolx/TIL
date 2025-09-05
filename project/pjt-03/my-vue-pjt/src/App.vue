<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="navbar">
    <nav>
      <RouterLink to="/" class="logo">🎬 My Movie</RouterLink>
      <ul class="nav-links">
        <li><RouterLink to="/movies">Movies</RouterLink></li>
        <li><RouterLink to="/review-search">Reviews</RouterLink></li>
        <li><RouterLink to="/recommended">Recommended</RouterLink></li>
      </ul>
    </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>
/* 상단 네비게이션 스타일 */
.navbar {
  background: linear-gradient(135deg, #FFF9BD, #6610f2);
  padding: 15px 30px;
  color: white;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-weight: bold;
  font-size: 20px;
  color: #37353E;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 20px;
  list-style: none;
}

.nav-links li a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 6px;
  transition: background 0.3s;
}

.nav-links li a:hover {
  background: rgba(255, 255, 255, 0.2);
}

a.router-link-exact-active {
  background: rgba(255, 255, 255, 0.3);
}
</style>
