<template>

<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png" >
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong> {{ Message_name }} </strong>, {{ Message_date }}
        <br>
          <p style="white-space: pre-line;">{{ Message_text }}</p>
        <br>
        <small><a>Marquer comme important</a> · <a>Répondre</a> · <a>Créer un fil à partir de commentaire</a> </small>
      </p> <br />
    </div>
   </div>
</article>

</template>

<script>
export default {
    props: ['Message_name','Message_date','Message_text','Message_image']
}
</script>