<template>
  <fieldset>
    <label :for="name">{{label}}</label>
    <input :id="name" :type="type" :placeholder="placeholder" :value="model" @change="changeValue"/>
  </fieldset>
</template>

<style scoped>
input {
  min-height: 48px;
  border: 1px solid #356AEA;
  border-radius: 5px;
  padding: 0 1rem;
  width: 100%;
  margin-bottom: 1rem;
  outline: none;
}

input:focus {
  box-shadow: 0 0 3px 1px#0089FF;
  border-color: #0089FF;
  transition: all .1s ease-in-out;
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
</style>

<script>
export default {
  name: 'Input',
  props: {
    name: String,
    type: String,
    placeholder: String,
    label: String,
    model: String
  },
  methods: {
    changeValue(e) {
      this.$emit('changeValue', e.target.value);
    }
  }
}
</script>