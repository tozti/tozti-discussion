<template>
<div>
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

<template v-if="Message_nbAnswers>0">

<button class="button is-text" v-on:click="afficherReponse()"> {{Message_nbAnswers}} réponses</button>

<template v-if="affRep">

<div v-for="answer in Message_answers">
   <answer-bla v-bind:Answer_name="answer.name" v-bind:Answer_text="answer.text" v-bind:Answer_date="answer.date" />
</div>

</template>

</template>

</div>
</template>

<script>

import Answer from './Answer.vue'

export default {
    props: ['Message_name','Message_date','Message_text','Message_answers','Message_nbAnswers'],
    methods: {
      afficherReponse() {
        if (this.affRep===true){
           this.affRep = false
        }
        else{
           this.affRep = true
        }
      }
    },
    data() {
    	return {
	    affRep :false
	}
    },
    components: {
	'answer-bla': Answer
    },
}
</script>