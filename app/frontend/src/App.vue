<template>
	<div id="app">
		<component :is="layout">
			<router-view/>
		</component>
	</div>
</template>

<style lang="scss">
	#app {
	}
</style>
<script>
  import Sidebar from "./components/Sidebar";
  import HeaderChat from "./components/Header";
  import EmptyLayout from "@/layout/EmptyLayout";
  import MainLayout from "@/layout/MainLayout";

  export default {
    components: {HeaderChat, Sidebar, MainLayout, EmptyLayout},
    data() {
      return {
        windowWidth: window.innerWidth,
      }
    },
    computed: {
      layout() {
        console.log(this.$route.meta.layout, 'this.$route.meta.layout')
        return (this.$route.meta.layout || 'empty') + "-layout"
      }
    },
    watch: {
      windowWidth(newWidth, oldWidth) {
        if (newWidth < 720) {
          this.$store.commit('toggleSidebar', false)
          this.$root.$emit('bv::toggle::collapse', 'sidebar1')
        }
      }
    },
    methods: {
      onResize() {
        this.windowWidth = window.innerWidth
      }
    },
    mounted() {
      this.$nextTick(() => {
        window.addEventListener('resize', this.onResize);
      })
    },
  }
</script>