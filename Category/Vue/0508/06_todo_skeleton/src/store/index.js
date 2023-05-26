// import { indexOf } from 'core-js/core/array'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    alltodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      return state.todos.filter(todo => todo.isCompleted).length
    },
    uncompletedTodosCount(state) {
      return state.todos.filter(todo => !todo.isCompleted).length
    },
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      // const todoIndex = state.todos.indexOf(todoItem)
      // state.todos.splice(todoIndex, 1)
      state.todos.splice(state.todos.indexOf(todoItem), 1)
    },
    UPDATE_TODO(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    LOAD_TODOS(state) {
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)

      state.todos = parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    updateTodo(context, todoItem) {
      context.commit('UPDATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    },
  },
  modules: {
  }
})
