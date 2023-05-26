<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <h2>예약 페이지</h2>
    <h3>시간 선택</h3>
    <table>
      <tr v-for="i in 5" :key="i">
        <td v-for="j in 6" :key="j">
          <button :id="times[(i-1)*6+j-1]" v-on:click="onClick" v-bind:class="{ 'clicked': selected.includes(times[(i-1)*6+j-1]) }">
            {{ times[(i-1)*6+j-1] }}
          </button>
        </td>
      </tr>
    </table>
    <hr>
    <h3>선택 시간 : {{ selectedForview.join(" ") }}</h3>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {},
  methods: {
    onClick: function (event) {
      if (this.selected.length >= 5 && !this.selected.includes(event.target.id)) {
        alert('5타임 이상은 신청할 수 없습니다.')
        return
      }
      if (this.selected.includes(event.target.id)) {
        this.selected.splice(this.selected.indexOf(event.target.id), 1)
      }
      else {
        this.selected.push(event.target.id)
      }
    }
  },
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selected: [],
    }
  },
  computed: {
    selectedForview() {
      return this.selected.slice().sort()
    }

  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
table {
  border-collapse: collapse;
  margin: auto;
}
button {
  padding: auto;
  padding-left: 15px;
  padding-right: 15px;
  color: #84898C;
  border: none;
  background-color: white;
  font-weight: 500;
  /* #0F4C81 #84898C, #424242, #658dc63d */
}
.clicked {
  background-color: #658dc63d;
  color: #0F4C81;
}
</style>
