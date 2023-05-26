<template>
  <div class="InCome">
    <p>
      연봉 입력 (만원): <input type="number" v-model="inCome">
    </p>
    <p>
      세액감면액 (만원): <input type="number" v-model="taxReduction">
    </p>
    <hr>
    <h2>종합소득금액 : {{ inCome }} 만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{ taxBase }} 만원</h2>
    <hr>
    <Taxrate
      :taxBase="taxBase"
      :taxReduction="taxReduction"
    />
  </div>
</template>

<script>
import Taxrate from '@/components/TaxRate'

export default {
  name: 'InCome',
  props: {
  },
  components: {
    Taxrate
  },
  data() {
    return {
      inCome: '',
      taxReduction: '',
    }
  },
  computed: {
    taxBase: function() {
        if (this.inCome - 150 > 0) {
          return this.inCome - 150
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
