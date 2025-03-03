<template>
  <div>
    <h2>Inscription</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email :</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="pseudo">Pseudo :</label>
        <input type="text" id="pseudo" v-model="pseudo" required />
      </div>
      <div>
        <label for="nom">Nom :</label>
        <input type="text" id="nom" v-model="nom" required />
      </div>
      <div>
        <label for="prenom">Prénom :</label>
        <input type="text" id="prenom" v-model="prenom" required />
      </div>
      <div>
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">S'inscrire</button>
    </form>
    <p>
      Déjà un compte ? <router-link to="/login">Se connecter</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: "",
      pseudo: "",
      nom: "",
      prenom: "",
      password: "",
    };
  },
  methods: {
  async register() {
    try {
      const dataToSend = {
        email: this.email,
        pseudo: this.pseudo,
        nom: this.nom,
        prenom: this.prenom,
        password: this.password,
      };
      console.log("Données d'inscription envoyées :", dataToSend);

      const response = await axios.post('http://localhost:8000/register/', dataToSend);
      alert(response.data.message); // Affiche un message de succès
    } catch (error) {
      console.error("Erreur d'inscription :", error.response ? error.response.data : error.message);
      alert("Erreur lors de l'inscription. Veuillez réessayer.");
    }
  },
},
};
</script>

<style scoped>
form {
  max-width: 300px;
  margin: 0 auto;
}
label {
  display: block;
  margin-bottom: 5px;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}
button {
  padding: 10px 15px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #369f6e;
}
</style>
