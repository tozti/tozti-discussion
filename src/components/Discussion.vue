<template>

<div>
<header>
  <h1 style="text-align:center; font-size:26pt;">{{title}}</h1>
</header>

<nav class="level">
  <!-- Left side -->
  <div class="level-left" style="width:80%" align="left">
    <div id="app" class="container" style="width: 100%" align="left">  
        <b-pagination
            :total="200"
            :current="1"
            order="is-centered"
            size="is-small"
            :simple="false"
            :rounded="true"
            :per-page="20"
	    @change="pageChange(page)">
        </b-pagination>
    </div>
  </div>
  <!-- Right side -->
  <div class="level-right">
    <b-icon icon="alarm-light"></b-icon>
    <b-icon icon="account-key"></b-icon>
    <b-icon icon="settings"></b-icon>
  </div>
</nav>

<message-bla Message_name="Fenril" Message_text="Salut il faut organiser la soirée Saint Valentin·e" Message_date="samedi 03/02/2018 à 18:46" Message_image="https://bulma.io/images/placeholders/128x128.png" />

<button class="button is-text" v-on:click="afficherReponse()">2 réponses</button>

<template v-if="affRep">

   <answer-bla Answer_name="Manu" Answer_text=" Non mais vous êtes dingues la saint Valentine c'est pas le même jour que la saint Valentin c'est une hérésie sans nom!" Answer_date="samedi 03/02/2018 à 19:14" Answer_image="https://bulma.io/images/placeholders/128x128.png" />

   <answer-bla Answer_name="lucas" Answer_text="j'appelle la police @anoiret" Answer_date="samedi 03/02/2018 à 18:50" Answer_image="https://bulma.io/images/placeholders/128x128.png" />

</template>

<message-bla Message_name="Fenril" Message_text="Répondez ici pour les idées de décoration" Message_date="samedi 03/02/2018 à 18:46" Message_image="https://bulma.io/images/placeholders/128x128.png" />

<notif-bla Notif_name1="Manu" Notif_name2="Fenril" Notif_date="samedi 03/02/2018 à 19:14" Notif_idMessage="none" />

<notif-bla Notif_name1="Lucas" Notif_name2="Fenril" Notif_date="samedi 03/02/2018 à 19:16" Notif_idMessage="none" />

<template v-if="nM">

   <message-bla Message_name="bobby" v-bind:Message_text="textField_newmessage" Message_date="samedi 03/02/2018 à 19:14" Message_image="https://bulma.io/images/placeholders/128x128.png" />

</template>

<text-bla textfield_name="bobby" @message-updated="updateMessage" @message-posted="postMessage" />

</div>


</template>

<script>
import TextField from './TextField.vue'
import Message from './Message.vue'
import Answer from './Answer.vue'
import Notif from './notif_message.vue'

export default {
    data () {
        return {
	    title: 'Soirée Saint Valentin.e',
            name: 'Fenril Montorier',
	    message: 'Hello',
	    affRep: false,
	    textField_newmessage: "",
	    nM: false
        }
    },

    components: {
        'text-bla': TextField,
    	'message-bla': Message,
	'answer-bla': Answer,
	'notif-bla': Notif
    },

  methods: {
    afficherReponse() {
       if (this.affRep===true){
          this.affRep = false
       }
       else {
          this.affRep = true
       }
    },
    updateMessage(textField_newmessage) {
      this.textField_newmessage = textField_newmessage;
    },
    postMessage(nM) {
       this.nM=nM;
    }
  }
};



</script>

<style>
</style>