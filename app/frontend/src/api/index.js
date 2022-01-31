import axios from "axios";


let options = {
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  withCredentials: true
}
const Axios = axios.create(options)
console.log(localStorage.getItem('chat-token'))
let token = localStorage.getItem('chat-token')


if (token) {
  Axios.defaults.headers['Authorization'] = 'token ' + token
}


const post = (url, formData) => Axios.post(url, formData);
const update = (url, formData) => Axios.put(url, formData);
const remove = (url, formData) => Axios.delete(url, formData);
const get = (url) => Axios.get(url);

export default {
  post,
  update,
  remove,
  get
}