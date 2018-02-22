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

<div v-for="message in messages">
  <message v-bind:message="message" @notif-updated="updateNotif" @answer-posted="postNotif" />
</div>

<text-field name="bobby" @message-updated="updateMessage" @message-posted="postMessage" />

</div>

</template>

<script>
import TextField from './TextField.vue'
import Message from './Message.vue'

export default {
    data () {
        return {
	    title: 'Soirée Saint Valentin.e',
            author: 'Fenril Montorier',
	    messages: [
                {typ:1, name:'Fenril', text:"Salut il faut organiser la soirée Saint Valentin·e", date:"samedi 03/02/2018 à 18:45",
		         answers:[
				{ name:'Manu', text:"Non mais vous êtes dingues la saint Valentine c'est pas le même jour que la saint Valentin c'est une hérésie sans nom!", date:"samedi 03/02/2018 à 19:14"},
				{ name:'Lucas',text:"j'appelle la police @anoiret", date:"samedi 03/02/2018 à 19:16"}
			 ], nbAnswers:2, name2:"none"
		},
		{typ:1, name:"Fenril", text:"Répondez ici pour les idées de décoration", date:"samedi 03/02/2018 à 18:46", answers:[], nbAnswers:0, name2:"none"},
		{typ:0, name:"Manu", text:"none", date:"samedi 03/02/2018 à 19:14", answers:[], nbAnswers:0, name2:"Fenril"},
		{typ:0, name:"Lucas", text:"none", date:"samedi 03/02/2018 à 19:16", answers:[], nbAnswers:0, name2:"Fenril"}
	    ],
	    newmessage: "",
	    nM: false,
	    nMA: false,
	    answerNotif: {name:"", date:"", name2:""}
        }
    },

    components: {
        TextField,
    	Message
    },

  methods: {
    updateMessage(newmessage) {
      this.newmessage = newmessage;
    },
    postMessage(nM) {
       this.nM=nM;
       if (this.nM===true)
       {
           this.messages.push({typ:1, name:"Bobby", text:this.newmessage, date:"A l'instant", answers:[], nbAnswers:0, name2:"none"});
       }
    },
    updateNotif(answerNotif) {
	this.answerNotif = answerNotif ;
    },
    postNotif(nMA) {
       this.nMA=nMA;
       if (this.nMA===true)
       {
           this.messages.push({typ:0, name:this.answerNotif.name, text:"none", date:"A l'instant", answers:[], nbAnswers:0, name2:this.answerNotif.name2});
       }
    },
  }
  
};

</script>

<style>
</style>