<template>
	<div class="app-main-layout">
		<header-chat/>
		<sidebar/>
		<div class="content-wrapper" :class="{'sidebar-open': isSidebarOpen}">
			<router-view/>
		</div>
	</div>
</template>

<script>

  import HeaderChat from "../components/Header";
  import Sidebar from "../components/Sidebar";
  import {mapGetters} from 'vuex'

  export default {
    name: "Main",
    components: {Sidebar, HeaderChat},
    data() {
      return {
        isOpen: true
      };
    },
    computed: {
      ...mapGetters(['isSidebarOpen'])
    },
    created() {
    },
  }
</script>

<style scoped>

</style>
