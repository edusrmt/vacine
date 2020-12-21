<template>
  <header>
    <BackButton>Entrar</BackButton>
  </header>
  <div class="sign-in">
    <img src="../assets/logo.png" alt="Logotipo do Vacine" class="logo" />
    
    <fieldset>
      <label for="email">E-MAIL</label>
      <input id="email" type="email" placeholder="meu@email.com" />
    </fieldset>
    
    <fieldset>
    <label for="password">SENHA</label>
    <input id="password" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" />
    </fieldset>

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

input {
  min-height: 48px;
  border: 1px solid #356AEA;
  border-radius: 5px;
  padding: 0 1rem;
  width: 100%;
  margin-bottom: 1rem;
}

label {
  color: #356AEA;
  font-weight: bold;
  font-size: 0.75rem;
}

fieldset {
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  border: none;
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

export default {
  name: 'SignIn',
  components: {
    BackButton,
    LinkButton
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