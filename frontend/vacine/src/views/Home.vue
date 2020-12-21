<template>
<div class="home">
  <img src="../assets/medicine.svg" alt="Ilustração com dois médicos" />
  <img class="logo" src="../assets/logo.png" alt="Logotipo do Vacine" />
  <div>
    <button class="primary">Cadastrar-se</button>
    <button class="secondary">Entrar</button>
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

button.primary {
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