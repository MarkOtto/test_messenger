import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user:{},
    sidebar: true,
    messages: [],
    messageType: 'inbox',
    currentMessage: {}
  },
  mutations: {
    toggleSidebar(state, payload) {
      state.sidebar = payload
    },
    setMessages(state, payload) {
      state.messages = payload
    },
    setMessageType(state, payload) {
      state.messageType = payload
    },
    setCurrentMessage(state, payload) {
      state.currentMessage = payload
    }
  },
  actions: {
    async LOGIN({commit}, {username, password}) {
      try {
        const {data} = await api.post('http://89.108.78.225/back/api/token/', {username, password})
        localStorage.setItem('chat-token', data.token)
        console.log(data, 'login')
        return data
      } catch (e) {
        console.log(e)
      }
    },
    async SEND_MESSAGE({commit}, {body, user, title}) {
      try {
        const {data} = await api.post('http://89.108.78.225/back/api/send/', {message: {body, user, title}})
        return data
      } catch (e) {
        console.log(e)
      }
    },

    async GET_INBOX({commit}, payload) {
      try {
        const {data} = await api.get('http://89.108.78.225/back/api/inbox/?page=1')
        console.log(data, 'inbox')
        commit('setMessages', data.results)
        commit('setMessageType', payload)
      } catch (e) {
        console.log(e)
      }

    },

    async SENT_MESSAGES({commit}, payload) {
      try {
        const {data} = await api.get('http://89.108.78.225/back/api/sent/?page=1')
        commit('setMessages', data.results)
        commit('setMessageType', payload)
      } catch (e) {
        console.log(e)
      }
    },
    async GET_CURRENT_MESSAGE({commit}, payload) {
     try {
       const {data} = await api.get(`http://89.108.78.225/back/api/message/${payload}/`)
       commit('setCurrentMessage', data)
     }catch (e) {
       console.log(e)
     }
    },
    SIGN_OUT({commit}, payload) {
      localStorage.removeItem('chat-token')
    }

  },
  modules: {},
  getters: {
    isSidebarOpen: state => state.sidebar,
    getInbox: state => state.messages,
    messageType: state => state.messageType,
    getCurrentMessage: state => state.currentMessage

  }
})
