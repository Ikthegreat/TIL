<template>
  <div class="FinalTax">
    <h2>결정세액 : {{ finalTax }} 만원</h2>
  </div>
</template>

<script>
export default {
  name: 'FinalTax',
  props: {
    taxBase: Number,
    taxReduction: Number,
    calculated: Number
  },
  computed: {
    finalTax() {
      if (this.calculated - this.taxReduction > 0) {
        return this.calculated - this.taxReduction
      }
      else {
        return 0
      }
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
