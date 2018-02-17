<template>

<article class="media">
  <div class="media-content">
    <div class="content">
      <p>
        <small> {{Notif_name1}} a répondu à un <a>message de {{Notif_name2}}</a>, {{Notif_date}} </small>
      </p>
    </div>
   </div>
  </article>

</template>


<script>
export default {
    props: ['Notif_name1','Notif_name2','Notif_date','Notif_idMessage']
}
</script>

<style>
</style>