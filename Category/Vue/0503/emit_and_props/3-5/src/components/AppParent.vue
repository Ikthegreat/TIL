<template>
  <div class="AppParent">
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input="parentInput">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChild
      :appData="appData"
      :parentData="parentData"
      @child-input="getChild"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  props: {
    appData: String,
  },
  components: {
    AppChild
  },
  data() {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    parentInput() {
      this.$emit('parent-input', this.parentData)
    },
    getChild(childInputData) {
      this.childData = childInputData
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
.AppParent {
  border-style: solid;
  border-color: red;
  border-width: 2px;
}
</style>
