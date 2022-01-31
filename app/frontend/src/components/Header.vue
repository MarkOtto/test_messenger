<template>
	<b-row class="header p-2">
		<div class="logo-wrapper m-auto d-flex justify-content-between align-items-center">
			<b-button @click="sidebarOpen" variant="outline-primary">
				<b-icon icon="border-width"></b-icon>
			</b-button>
			<h1 class="text-center m-0">LOGO</h1>
			<b-button variant="outline-warning" class="d-block" @click="signOut">Sing out</b-button>

		</div>
	</b-row>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    name: "HeaderChat",
    methods: {
      sidebarOpen() {
        let sidebarFlag = !this.isSidebarOpen
        this.$store.commit('toggleSidebar', sidebarFlag)
        this.$root.$emit('bv::toggle::collapse', 'sidebar1')
      },
      signOut(){
        localStorage.removeItem('chat-token')
        this.$router.push({path:'/', query:{login: 'required'}})
			}
    },
    computed:{
      ...mapGetters(['isSidebarOpen'])
    },
  }
</script>

<style scoped>

</style>