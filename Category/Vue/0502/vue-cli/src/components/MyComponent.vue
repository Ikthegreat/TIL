<template>
  <div>
    <h1>This is Component</h1>
    <MyChild />
    <MyChild />
  </div>
</template>

<script>
import MyChild from './MyChild.vue'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  }

}

</script>

<style>

</style>