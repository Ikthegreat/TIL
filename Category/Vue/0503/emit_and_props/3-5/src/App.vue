<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent
      :appData="appData"
      @parent-input="getParent"
      @child-input="getChild"
    />
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data() {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    getParent(parentInputData) {
      this.parentData = parentInputData
    },
    getChild(childInputData) {
      this.childData = childInputData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border-color: green;
  border-width: 2px;
  border-style: solid;
}
</style>
