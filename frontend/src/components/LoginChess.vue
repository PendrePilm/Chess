<template>
  <div>
    <h2>Connexion</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email :</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Se connecter</button>
    </form>
    <p>
      Pas encore de compte ? <router-link to="/signup">S'inscrire</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/login/', {
          email: this.email,
          password: this.password,
        });
        console.log(response.data.message);

        // Rediriger vers la page MenuChess après une connexion réussie
        this.$router.push('/menu');
      } catch (error) {
        console.error("Erreur de connexion :", error.response ? error.response.data : error.message);
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
