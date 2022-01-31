<template>
	<b-row class="d-flex align-items-center p-4">
		<b-col>
			<vue-good-table
				:columns="messagesColumn"
				:rows="getInbox"
				:pagination-options="{
					enabled: true,
					perPage: 10,
					mode: 'records',
					perPageDropdown: [10, 15]}"
			>

				<template slot="table-row" slot-scope="props">
					<div v-if="props.column.field === 'actions'" class="d-flex justify-content-center">
						<b-button size="sm" variant="success" class="m-1" @click="readCurrentMessage(props.row.id)">View</b-button>
					</div>
				</template>
			</vue-good-table>
		</b-col>
		<current-message-modal/>
	</b-row>
</template>

<script>
  import {mapGetters} from 'vuex'
  import CurrentMessageModal from "../components/CurrentMessageModal";

  export default {
    name: "Inbox",
    components: {CurrentMessageModal},
    data() {
      return {
        columns: [
          {
            label: 'To',
            field: 'user_to.username',
          },
          {
            label: 'Message Title',
            field: 'title',
          },
          {
            label: 'Actions',
            field: 'actions',
            tdClass: "text-right",
            thClass: "text-right"
          },
        ],
        rows: [
          {id: 1, name: "John", age: 20, createdAt: '', score: 0.03343},
          {id: 2, name: "Jane", age: 24, createdAt: '2011-10-31', score: 0.03343},
          {id: 3, name: "Susan", age: 16, createdAt: '2011-10-30', score: 0.03343},
          {id: 4, name: "Chris", age: 55, createdAt: '2011-10-11', score: 0.03343},
          {id: 5, name: "Dan", age: 40, createdAt: '2011-10-21', score: 0.03343},
          {id: 6, name: "John", age: 20, createdAt: '2011-10-31', score: 0.03343},
        ],
      }
    },
    methods: {
      readCurrentMessage(id) {
        this.$store.dispatch('GET_CURRENT_MESSAGE', id)
        this.$bvModal.show('current')
      },
    },
		async mounted(){
      await this.$store.dispatch('GET_INBOX', 'inbox')
		},
    computed: {
      ...mapGetters(['getInbox', 'messageType', 'getCurrentMessage']),
      messagesColumn() {
        if (this.messageType === 'sent') {
          return [
            {
              label: 'To',
              field: 'user_to.username',
            },
            {
              label: 'Message Title',
              field: 'title',
            },
            {
              label: 'Actions',
              field: 'actions',
              tdClass: "text-right",
              thClass: "text-right"
            },
          ]
        } else if (this.messageType === 'inbox') {
          return [
            {
              label: 'From',
              field: 'user_from.username',
            },
            {
              label: 'Message Title',
              field: 'title',
            },
            {
              label: 'Actions',
              field: 'actions',
              tdClass: "text-right",
              thClass: "text-right"
            },
          ]
        }
      }
    }
  }
</script>

<style scoped>

</style>