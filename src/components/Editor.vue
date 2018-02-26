<template>
    <section :class="['editor', 'media', { floating: isFloating }]">
        <figure class="media-left">
            <p class="image is-64x64">
                <!-- TODO(liautaud): Add the actual avatar -->
                <img src="https://placeimg.com/128/128/people">
            </p>
        </figure>
        
        <div class="media-content">
            <div class="content">
                <p class="author">
                    <strong>{{ tozti.me.body.name }}</strong>
                </p>
                
                <textarea class="textarea" placeholder="Saisissez votre message"></textarea>
            </div>

            <div class="level">
                <div class="level-left toolbox">
                    <a href="#" class="button is-light"><i class="material-icons">format_bold</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">format_italic</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">format_underlined</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">functions</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">attach_file</i></a>
                    <a href="#" class="button is-light"><i class="material-icons">person</i></a>
                </div>

                <div class="level-right">
                    <a href="#" class="button is-primary"><i class="material-icons">send</i>&nbsp; Envoyer</a>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        props: ['isFloating']
    }
</script>