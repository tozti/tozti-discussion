<template>

<div id='all'>

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

<p><article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{name}}</strong>, samedi 03/02/2018 à 18:44
        <br>
       Salut il faut organiser la soirée Saint Valentin·e
        <br>
        <small><a>Marquer comme important</a> · <a>Créer un fil à partir de commentaire</a> </small>
      </p>
    </div>

   <button class="button is-text" onclick="myFunction()">2 réponses</button>
   <div id="answers" style="display: none;">

    <article class="media">
      <figure class="media-left">
        <p class="image is-48x48">
          <img src="https://bulma.io/images/placeholders/96x96.png">
        </p>
      </figure>      
      <div class="media-content">
        <div class="content">
          <p>
            <strong>Emmanuel Rodriguez</strong>, samedi 03/02/2018 à 19:14
            <br>
            Non mais vous êtes dingues la saint Valentine c'est pas le même jour que la saint Valentin c'est une hérésie sans nom!
            <br>
            <small><a>Marquer comme important</a> · <a>Créer un fil à partir de commentaire</a></small>
          </p>
        </div>
      </div>
    </article>

    <article class="media">
      <figure class="media-left">
        <p class="image is-48x48">
          <img src="https://bulma.io/images/placeholders/96x96.png">
        </p>
      </figure>
      <div class="media-content">
        <div class="content">
          <p>
            <strong>Lucas Perotin</strong>, samedi 03/02/2018 à 19:16
            <br>
	    j'appelle la police <strong>@anoiret</strong>
            <br>
            <small><a>Marquer comme important</a> · <a>Répondre</a> · <a>Créer un fil à partir de commentaire</a> </small>
          </p>
        </div>
      </div>
    </article>
   </div>
  </div>
  </article>
  
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{name}}</strong>, samedi 03/02/2018 à 18:46
        <br>
       Répondez ici pour les idées de décoration
        <br>
        <small><a>Marquer comme important</a> · <a>Répondre</a> · <a>Créer un fil à partir de commentaire</a> </small>
      </p>
    </div>
   </div>
 </article>


<article class="media">
  <div class="media-content">
    <div class="content">
      <p>
        <small> Emmanuel Rodriguez a répondu à un <a>message de {{name}}</a>, samedi 03/02/2018 à 19:14 </small>
      </p>
      <p>
	<small> Lucas Perotin a répondu à un <a>message de {{name}}</a>, samedi 03/02/2018 à 19:16 </small>
      </p>
    </div>
   </div>
  </article>
  
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/images/placeholders/128x128.png">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
	<strong> Mon nom </strong>
      </p>
    </div>  
    <div class="field">
      <p class="control">
        <textarea class="textarea" placeholder="Add a comment..."></textarea>
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
        <button class="button">Poster un commentaire</button>
      </p>
    </div>
  </div>
</article></p>
</div>
</template>

<script>
export default {
    name: 'all',
    data () {
        return {
	       title: 'Soirée Saint Valentin.e',
            name: 'Fenril Montorier'
        }
    }
}
</script>

<style scoped>
</style>