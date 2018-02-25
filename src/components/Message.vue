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
           <small><a>Marquer comme important</a> · <button style="font-size : 12px" class="button is-text" v-on:click="toggleAnswer()"> <a> répondre </a> </button> · <a>Créer un fil à partir de commentaire</a> </small>
         </p>
       <template v-if="message.nbAnswers>0">
         <button class="button is-text" v-on:click="toggleAnswer()"> {{message.nbAnswers}} réponses</button>
       <br />
       <br />
       </template>
       </div>
      </div>
   </article>

   <template v-if="showAnswer">
      <div v-for="answer in message.answers">
         <answer v-bind:answer="answer" />
      </div>
      <answer-textfield name="Bobby" @message-updated="updateMessage" @message-posted="postMessage" />
   </template>
   <br />
</template>

<template v-if="message.typ<1">
   <notif v-bind:name1="message.name" v-bind:name2="message.name2" v-bind:date="message.date" v-bind:idMessage="none" />
   <br />
</template>

</div>
</template>

<script>

import Answer from './Answer.vue'
import AnswerTextfield from './Answer_textfield.vue'
import Notif from './notif_message.vue'

export default {

   props: ['message'],
    
   data() {
      return {
	 showAnswer :false,
	 nM: false,
	 newAnswer: "",
	 nMA: false,
	 answerNotif:{name:"",date:"",name2:""}
      }
   },

   components: {
      Answer,
      AnswerTextfield,
      Notif
   },

   methods: {
      toggleAnswer() {
        this.showAnswer= !this.showAnswer
      },
      updateMessage(newAnswer) {
        this.newAnswer = newAnswer;
      },
      postMessage(nM) {
        this.nM=nM;
        if (this.nM===true)
        {
           this.message.answers.push({name:"Bobby", text:this.newAnswer, date:"A l'instant"});
	   this.answerNotif={name:"Bobby",date:"A l'instant",name2:this.message.name};
	   this.nMA=true;
	   this.message.nbAnswers=this.message.nbAnswers+1;
        }
      }
   },
   
   watch: {
      answerNotif() {
         this.$emit('notif-updated', this.answerNotif);
      },
      nMA() {
         this.$emit('answer-posted', this.nMA);
         this.nMA=false;
      }
   }
   
}
</script>
