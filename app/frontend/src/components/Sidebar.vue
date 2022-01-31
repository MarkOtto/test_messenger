<template>
	<div class="sidebar">
		<b-sidebar visible shadow id="sidebar1" no-header>
			<b-list-group>
				<b-list-group-item href="#" @click="handlerComposeMessage"
													 class="d-flex justify-content-between align-items-center">
					Compose
				</b-list-group-item>
				<b-list-group-item href="#" @click="handlerInbox" class="d-flex justify-content-between align-items-center">
					Inbox
				</b-list-group-item>
				<b-list-group-item href="#" @click="handlerSent" class="d-flex justify-content-between align-items-center">
					Sent
				</b-list-group-item>
			</b-list-group>
		</b-sidebar>
		<compose-modal/>
	</div>
</template>

<script>
  import ComposeModal from "./ComposeModal";

  export default {
    name: "Sidebar",
    components: {ComposeModal},
    methods: {
      handlerComposeMessage() {
        this.$bvModal.show('compose')
      },
      handlerInbox() {
        this.$store.dispatch('GET_INBOX', 'inbox')
      },
      handlerSent() {
        this.$store.dispatch('SENT_MESSAGES', 'sent')
      }
    }
  }
</script>

<style scoped>

</style>