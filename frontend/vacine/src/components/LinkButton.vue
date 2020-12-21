<template>
  <router-link :to="to" :class="type">
    <slot />
  </router-link>
</template>

<style scoped>
a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 48px;
  border-style: none;
  border-radius: 5px;
  font-size: 18px;
  text-decoration: none;
}

a.primary {
  background-color: #356AEA;
  color: #FFFFFF;
}

a.secondary {
  background-color: #FFFFFF;
  border: 1px solid #356AEA;
  color: #356AEA;
}
</style>

<script>
export default {
  name: 'LinkButton',
  props: {
    to: String,
    type: String
  }
}
</script>