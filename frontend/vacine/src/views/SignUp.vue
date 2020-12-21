<template>
  <header>
    <BackButton>Cadastro</BackButton>
  </header>
</template>

<style scoped>
header {
  padding-top: 1rem;
  margin-left: -5vw;
}
</style>

<script>
import BackButton from '../components/BackButton';

export default {
  name: 'SignUp',
  components: {
    BackButton
  }
}
</script>