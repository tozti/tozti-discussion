<template>

<article class="media">
  <div class="media-content">
    <div class="content">
      <p>
        <small> {{name1}} a répondu à un <a>message de {{name2}}</a>, {{date}} </small>
      </p>
    </div>
  </div>
</article>

</template>


<script>
export default {
    props: ['name1','name2','date','idMessage']
}
</script>

<style>
</style>