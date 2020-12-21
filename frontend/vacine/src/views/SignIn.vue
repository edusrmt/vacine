<template>
  <header>
    <BackButton>Entrar</BackButton>
  </header>
  <div class="sign-in">
    <img src="../assets/logo.png" alt="Logotipo do Vacine" class="logo" />

    <Input name="email" type="email" placeholder="meu@email.com" label="E-MAIL" />
    <Input name="password" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" label="SENHA" />

    <LinkButton @click="submitLogin" to="/entrar" type="primary">Entrar</LinkButton>
  </div>
</template>

<style scoped>
header {
  padding-top: 1rem;
  margin-left: -5vw;
}

div.sign-in {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: stretch;
  padding-top: 3rem;
}

img.logo {
  width: 80%;
  margin: 0 auto 3rem;
}
</style>

<script>
import axios from 'axios';

import LinkButton from '../components/LinkButton';
import BackButton from '../components/BackButton';
import Input from '../components/Input';

export default {
  name: 'SignIn',
  components: {
    BackButton,
    LinkButton,
    Input
  },
  setup() {
    function submitLogin(event) {
      event.preventDefault();
      axios.get('http://localhost:8000/pacientes/').then(res => console.log(res.data));
    }

    return {submitLogin};
  }
}
</script>