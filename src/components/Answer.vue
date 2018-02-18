<template>

<div style="text-align: left;padding-left: 60px">
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png" >
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong> {{ Answer_name }} </strong>, {{ Answer_date }}
        <br>
          <p style="white-space: pre-line;">{{ Answer_text }}</p>
        <br>
        <small><a>Marquer comme important</a> · <a>Répondre</a> · <a>Créer un fil à partir de commentaire</a> </small>
      </p> <br />
    </div>
   </div>
 </article>
</div>

</template>

<script>
export default {
    props: ['Answer_name','Answer_text','Answer_date']
}
</script>