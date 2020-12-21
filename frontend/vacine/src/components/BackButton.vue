<template>
  <h1 @click="$router.back()">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
    </svg> <slot />
  </h1>
</template>

<style scoped>
svg {
  width: 2rem;
}

h1 {
  display: flex;
  align-items: center;
  font-size: 1.25rem;
  color: #356AEA;
}
</style>