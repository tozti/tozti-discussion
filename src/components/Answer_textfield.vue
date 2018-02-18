<template>

<div style="text-align: left;padding-left: 60px">

<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
	<strong> {{ anstextfield_name }} </strong>
      </p>
    </div>
    
    <div class="field">
      <p class="control">
        <textarea rows="4" cols="50" v-model="val" placeholder="ajoutez plusieurs lignes"></textarea>
      </p>
    </div>
    <div class="file has-name">
      <label class="file-label">
	<input class="file-input" type="file" name="resume">
	<span class="file-cta">
	  <span class="file-icon">
            <i class="fas fa-upload"></i>
	  </span>
	  <span class="file-label">
            Choose a file…
	  </span>
	</span>
	<span class="file-name">
	</span>
      </label>
    </div>
    <div class="field">
      <p class="control">
        <button class="button" v-on:click="posterMessage()">Poster un commentaire</button>
      </p>
    </div>
  </div>
</article>

</div>

</template>

<script>

export default{
  props: ['anstextfield_name', 'anstextfield_newmessage'],
  created() {
    this.val = this.anstextfield_newmessage,
    this.nM=false
  },
  data() {
    return {
      val: '',
      nM:false
    }
  },
  watch: {
    val() {
      this.$emit('message-updated', this.val);
    },
    nM() {
      this.$emit('message-posted', this.nM);
      this.nM=false;
    }
  },
   methods: {
    posterMessage() {
       this.nM=true
    },
    
  }
}

</script>