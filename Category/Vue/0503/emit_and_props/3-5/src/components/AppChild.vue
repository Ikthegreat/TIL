<template>
  <div class="AppChild">
    <h1>AppChild</h1>
    <input type="text" v-model="childData" @input="childInput">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: String,
    parentData: String,
  },
  data() {
    return {
      childData: '',
    }
  },
  methods: {
    childInput() {
      this.$emit('child-input', this.childData)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.AppChild {
  border-style: solid;
  border-width: 2px;
  border-color: blue;
}
</style>
