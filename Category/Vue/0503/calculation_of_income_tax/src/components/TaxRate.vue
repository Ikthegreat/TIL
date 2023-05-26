<template>
  <div class="TaxRate">
    <h2>산출세액 : {{ Math.round(taxBase * taxPercent - proGressive) }} 만원</h2>
    <h2>세액감면 : (-) {{ taxReduction }} 만원</h2>
    <hr>
    <FinalTax
      :taxBase="taxBase"
      :taxReduction="taxReduction"
      :calculated="Math.round(taxBase * taxPercent - proGressive)"
    />
  </div>
</template>

<script>
import FinalTax from '@/components/FinalTax'

export default {
  name: 'TaxRate',
  props: {
    taxBase: Number,
    taxReduction: Number,
  },
  components: {
    FinalTax,
  },
  computed: {
    taxPercent: function(){
      if (this.taxBase <= 1200) {
        return 0.06
      }
      else if (1200 < this.taxBase <= 4600) {
        return 0.15
      }
      else if (4600 < this.taxBase && this.taxBase <= 8800) {
        return 0.24
      }
      else if (8800 < this.taxBase && this.taxBase <= 15000) {
        return 0.35
      }
      else if (15000 < this.taxBase && this.taxBase <= 30000) {
        return 0.38
      }
      else if (30000 < this.taxBase && this.taxBase <= 50000) {
        return 0.4
      }
      else if (50000 < this.taxBase && this.taxBase <= 100000) {
        return 0.42
      }
      else {
        return 0.45
      }
    },
      proGressive: function(){
      if (this.taxBase <= 1200) {
        return 0
      }
      else if (1200 < this.taxBase <= 4600) {
        return 108
      }
      else if (4600 < this.taxBase && this.taxBase <= 8800) {
        return 522
      }
      else if (8800 < this.taxBase && this.taxBase <= 15000) {
        return 1490
      }
      else if (15000 < this.taxBase && this.taxBase <= 30000) {
        return 1940
      }
      else if (30000 < this.taxBase && this.taxBase <= 50000) {
        return 2540
      }
      else if (50000 < this.taxBase && this.taxBase <= 100000) {
        return 3540
      }
      else {
        return 6540
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
