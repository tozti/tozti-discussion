<template>
	<t-taxonomy-item
		icon="message"
		:loading="loading"
		:title="title"
		:date="date"
		:to="handle"
		:subtitle="date"
		:resource="resource"
		:root="root"
	/>
</template>

<script>
	import { resourceMixin } from 'tozti'

	export default {
		mixins: [ resourceMixin ],

		props: {
			handle: String,
			root: {
				type: Object,
				default: null
			}
		},

		data() {
			return {
				title: '',
				date: '',
			}
		},

		watch: {
			loading() {
				this.title = this.resource.body.name
				this.date = this.resource.meta['last-modified']
				this.url = this.resource.meta['last-modified']
			}
		}
	}
</script>
