<template>
    <article class="media event">
        <i class="material-icons">reply</i>
        <p>
        	<strong>{{ author.name }}</strong>
        	a répondu à <a href="#">un message</a> de
        	<strong>{{ parentAuthor.name }}</strong> il y a 
        	<small><timeago :since="message.meta.created"></timeago></small>.
        </p>
    </article>
</template>

<script>
	export default {
		props: ['message', 'author', 'parentMessage', 'parentAuthor']
	}
</script>