<template>
	<b-row class="m-auto container">
		<b-col lg="4" md="8" sm="10" class="m-auto">
			<b-card>
				<b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
					<b-form-group
						id="input-group-1"
						label="Email address:"
						label-for="input-1"
					>
						<b-form-input
							id="input-1"
							v-model="form.username"
							type="text"
							placeholder="Email..."
							required
						></b-form-input>
					</b-form-group>

					<b-form-group
						id="input-group-1"
						label="Password:"
						label-for="input-2"
					>
						<b-form-input
							id="input-2"
							v-model="form.password"
							type="password"
							placeholder="Password..."
							required
						></b-form-input>
					</b-form-group>
						<b-button type="submit" variant="outline-info" class="col-12 mt-4 d-block">Login</b-button>
				</b-form>

			</b-card>
		</b-col>

	</b-row>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        form: {username: '', password: ''},
        show: true
      }
    },
    methods: {
     async onSubmit(event) {
		const response = 	await this.$store.dispatch("LOGIN", this.form)
			 if (response && response.token){
         this.$router.push({path: 'inbox', query: {location: 'received'}})
			 }
      },
      onReset(event) {
        // Reset our form values
        this.form.email = ''
        this.form.password = ''
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style scoped>

</style>