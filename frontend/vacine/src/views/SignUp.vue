<template>
  <header>
    <BackButton>Cadastro</BackButton>
  </header>
  <form>
    <span class="form-error">{{form_errors}}</span>
    <Input name="nome" type="text" placeholder="Ana Maria da Silva Santos" label="NOME COMPLETO" @changeValue="nome_completo = $event" :model="nome_completo" />
    <Input name="cpf" type="number" placeholder="123.456.789-10" label="CPF" @changeValue="cpf = $event" :model="cpf" />
    <Input name="nascimento" type="date" placeholder="01/01/2020" label="DATA DE NASCIMENTO" @changeValue="data_nascimento = $event" :model="data_nascimento" />
    <Input name="cns" type="number" placeholder="123 4567 8910 1112" label="CNS" @changeValue="cns = $event" :model="cns" />
    <Input name="email" type="email" placeholder="meu@email.com" label="E-MAIL" @changeValue="email = $event" :model="email" />
    <Input name="password" type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" label="SENHA" @changeValue="password = $event" :model="password" />
    <LinkButton @click="submitRegister" to="/cadastro" type="primary">Cadastrar-se</LinkButton>
  </form>
</template>

<style scoped>
header {
  padding-top: 1rem;
  margin-left: -5vw;
  margin-bottom: 1rem;
}

span.form-error {
  color: #FE6961;
  font-size: 0.75rem;
  margin-bottom: 1rem;
  display: block;
}
</style>

<script>
import axios from 'axios';

import BackButton from '../components/BackButton';
import LinkButton from '../components/LinkButton';
import Input from '../components/Input';

export default {
  name: 'SignUp',
  components: {
    BackButton,
    LinkButton,
    Input
  },
  data() {
    return {
      nome_completo: "",
      cpf: "",
      data_nascimento: "2000-01-01",
      cns: "",
      email: "",
      password: "",
      form_errors: ""
    };
  },
  methods: {
    submitRegister(event) {
      event.preventDefault();

      const form = {
        nome_completo: this.nome_completo,
        cpf: this.cpf,
        data_nascimento: this.data_nascimento,
        cns: this.cns,
        email: this.email,
        password: this.password
      };

      axios.post('http://localhost:8000/pacientes/', form)
        .then(res => {
          if (res.status == 201) {
            this.$router.push('/entrar');
          }
        })
        .catch(() =>  {
          this.form_errors = "Cadastro não realizado, verifique suas informações e tente novamente."
        });
    }
  }
}
</script>