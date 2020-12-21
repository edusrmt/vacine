<template>
  <router-view />
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
* {
  font-family: Montserrat, Helvetica, Arial, sans-serif;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0 10vw 10vw 10vw;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#app > div {
  flex: 1;
}
</style>
