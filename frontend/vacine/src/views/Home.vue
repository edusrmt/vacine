<template>
<div class="home">
  <img src="../assets/medicine.svg" alt="Ilustração com dois médicos" />
  <img class="logo" src="../assets/logo.png" alt="Logotipo do Vacine" />
  <div>
    <LinkButton to="/cadastro" type="primary">Cadastrar-se</LinkButton>
    <LinkButton to="/entrar" type="secondary">Entrar</LinkButton>
  </div>
</div>
</template>

<style scoped>
div.home {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;
  padding-top: 3rem;
}

a.primary {
  margin-bottom: 1rem;
}

img {
  width: 100%;
}

img.logo {
  width: 80%;
  margin: 0 auto;
}
</style>

<script>
import LinkButton from '../components/LinkButton';

export default {
  name: 'Home',
  components: {
    LinkButton
  }
}
</script>