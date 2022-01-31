<template>
	<b-modal id="current"  hide-header-close centered>
		<template #modal-title>
			{{getCurrentMessage.title}}
		</template>
		{{getCurrentMessage.body}}
		<template #modal-footer>
			<b-button @click="closeModal">Close</b-button>
		</template>
	</b-modal>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    name: "CurrentMessageModal",
    computed: {
      ...mapGetters(['getCurrentMessage']),
    },
		methods:{
      closeModal(){
        this.$bvModal.hide('current')
			}
		},
		watch:{
      getCurrentMessage(){}
		}
  }
</script>

<style scoped>

</style>