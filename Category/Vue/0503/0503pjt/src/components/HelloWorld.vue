<template>
  <div>
    <h1>{{ message }}</h1>
    <h1>{{ content }}</h1>
    <button @click="change">Button</button>
    <hr>
    <button @click="emitEvent">EMIT</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    message: String,
    content: String
  },
  methods: {
    emitEvent(){
      this.$emit('event-name')
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
</style>
