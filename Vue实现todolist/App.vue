<template>
  <div>
    <div>
      <form action="">
        <input v-model="inputValue" type="text">
        <button @click="handleSubmit" type="submit">提交</button>
      </form>
    </div>
    <ul>
      <todo-item v-for="(item, index) of list" :content="item"
      :key="index" :index="index" @delete="handleDelete"
      ></todo-item>
    </ul>
  </div>
</template>
<script>
import Hello from './components/Hello'
export default {
  components: {
    'todo-item': Hello
  },
  data () {
    return {
      inputValue: '',
      list: []
    }
  },
  methods: {
    handleSubmit () {
      this.list.push(this.inputValue)
      this.inputValue = ''
    },
    handleDelete (index) {
      this.list.splice(index, 1)
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
