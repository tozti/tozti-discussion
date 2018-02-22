<template>
<div>

<template v-if="message.typ>0">
   <article class="media">
     <figure class="media-left">
       <p class="image is-64x64">
         <img src="https://bulma.io/images/placeholders/128x128.png" >
       </p>
     </figure>
     <div class="media-content">
       <div class="content">
         <p>
           <strong> {{ message.name }} </strong>, {{ message.date }}
           <br>
             <p style="white-space: pre-line;">{{ message.text }}</p>
           <br>
           <small><a>Marquer comme important</a> · <button class="button is-text" v-on:click="afficherReponse()"> <a> répondre </a> </button> · <a>Créer un fil à partir de commentaire</a> </small>
         </p> <br />
       </div>
      </div>
   </article>

   <template v-if="message.nbAnswers>0">
      <button class="button is-text" v-on:click="afficherReponse()"> {{message.nbAnswers}} réponses</button>
   </template>

   <template v-if="affRep">
      <div v-for="answer in message.answers">
         <answer-bla v-bind:Answer="answer" />
      </div>
      <anstext-bla anstextfield_name="bobby" @message-updated="updateMessage" @message-posted="postMessage" />
   </template>
</template>

<template v-if="message.typ<1">
   <notif-bla v-bind:Notif_name1="message.name" v-bind:Notif_name2="message.name2" v-bind:Notif_date="message.date" v-bind:Notif_idMessage="none" />
</template>

</div>
</template>

<script>

import Answer from './Answer.vue'
import Answer_textfield from './Answer_textfield.vue'
import Notif from './notif_message.vue'

export default {
    props: ['message'],
    methods: {
      afficherReponse() {
        if (this.affRep===true){
           this.affRep = false
        }
        else{
           this.affRep = true
        }
      },
      updateMessage(textField_newmessage) {
        this.textField_newmessage = textField_newmessage;
      },
      postMessage(nM) {
        this.nM=nM;
        if (this.nM===true)
        {
           this.message.answers.push({name:"Bobby", text:this.textField_newmessage, date:"A l'instant"});
        }
      }
    },
    data() {
    	return {
	    affRep :false,
	    nM: false,
	    textField_newmessage: ""
	}
    },
    components: {
	'answer-bla': Answer,
	'anstext-bla': Answer_textfield,
	'notif-bla': Notif
    },
}
</script>