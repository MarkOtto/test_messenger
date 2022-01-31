export default (to, from, next) => {
  if (!localStorage.getItem("chat-token")) {
    console.log('token')
    next('/login');
  }
  next()
};