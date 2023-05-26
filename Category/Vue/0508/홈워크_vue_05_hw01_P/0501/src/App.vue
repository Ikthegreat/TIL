<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  methods: {
    increase() {
      const increaseCount = this.counter
      this.$store.dispatch('increase', increaseCount)
    },
    decrease() {
      const decreaseCount = this.counter
      this.$store.dispatch('decrease', decreaseCount)
    }
  },
  computed: {
    counter: function() {
      return this.$store.state.counter
    },
    counterDouble() {
      return this.$store.getters.counterDouble
    }
  },
}
</script>

<style>
</style>