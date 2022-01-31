<template>
	<b-modal id="compose" hide-footer hide-header-close centered>
		<template #modal-title>
			Compose Message
		</template>
		<b-form @submit.prevent="sendMessage" @reset.prevent="cancelMessage">

			<b-input-group prepend="To" class="mb-4">
				<b-form-input v-model="message.user" placeholder="To..."></b-form-input>
			</b-input-group>
			<b-input-group prepend="Title" class="mb-4">
				<b-form-input v-model="message.title" placeholder="Title"></b-form-input>
			</b-input-group>
			<b-form-textarea
				id="textarea"
				v-model="message.body"
				placeholder="Enter Your text here..."
				no-resize
				rows="3"
				max-rows="6"
			></b-form-textarea>
			<div class="d-flex justify-content-between mt-4">
				<b-button type="reset" variant="danger" class="align-self-end">Cancel</b-button>
				<b-button type="submit" variant="success" class="align-self-end">Send</b-button>

			</div>
		</b-form>
	</b-modal>
</template>

<script>
  export default {
    name: "ComposeModal",
    data() {
      return {
        message: {
          body: '',
          user: '',
          title:''
        }
      }
    },
    methods: {
     async sendMessage() {
				const response = await this.$store.dispatch('SEND_MESSAGE', this.message)
			 if (response?.success){
         this.$bvModal.hide('compose')
       }
      },
      cancelMessage() {
        this.message = {
          text: '',
          to: ''
        }
        this.$bvModal.hide('compose')
      }
    }
  }
</script>

<style scoped>

</style>