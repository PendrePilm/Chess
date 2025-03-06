<template>
    <div class="play-container">
      <aside class="sidebar">
        <nav>
          <ul>
            <li><router-link to="/menu">Accueil</router-link></li>
            <li><router-link to="/parametres">Paramètres</router-link></li>
            <li><a href="#" @click.prevent="logout">Déconnexion</a></li>
          </ul>
        </nav>
      </aside>
      <div class="content">
        <h2>Jouer aux Échecs</h2>
        <div class="game-options">
          <div class="create-game">
            <h3>Créer une Nouvelle Partie</h3>
            <button @click="createGame">Créer une partie</button>
            <p v-if="gameCode">Code de la partie : {{ gameCode }}</p>
          </div>
          <div class="join-game">
            <h3>Rejoindre une Partie</h3>
            <form @submit.prevent="joinGame">
              <div class="form-group">
                <label for="gameCodeInput">Code de la partie :</label>
                <input type="text" id="gameCodeInput" v-model="gameCodeInput" required />
              </div>
              <button type="submit">Rejoindre la partie</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "PlayChess",
    data() {
      return {
        gameCode: '',
        gameCodeInput: '',
      };
    },
    methods: {
      createGame() {
        // Logique pour créer une partie et générer un code
        this.gameCode = 'ABCD1234'; // Exemple de code généré
        alert(`Partie créée avec le code : ${this.gameCode}`);
      },
      joinGame() {
        // Logique pour rejoindre une partie avec le code saisi
        alert(`Rejoindre la partie avec le code : ${this.gameCodeInput}`);
      },
      async logout() {
        try {
          await axios.post('http://localhost:8000/logout/');
          localStorage.removeItem('userPseudo');
          localStorage.removeItem('userEmail');
          localStorage.removeItem('userNom');
          localStorage.removeItem('userPrenom');
          this.$router.push('/login');
        } catch (error) {
          console.error("Erreur lors de la déconnexion :", error.response ? error.response.data : error.message);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .play-container {
    display: flex;
  }
  
  .sidebar {
    width: 200px;
    background-color: #1f1f1f;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.5);
  }
  
  .sidebar nav ul {
    list-style-type: none;
    padding: 0;
  }
  
  .sidebar nav ul li {
    margin: 15px 0;
  }
  
  .sidebar nav ul li a {
    color: #e0e0e0;
    text-decoration: none;
  }
  
  .sidebar nav ul li a:hover {
    text-decoration: underline;
  }
  
  .content {
    flex-grow: 1;
    padding: 20px;
    text-align: center;
  }
  
  .game-options {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  .create-game, .join-game {
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 8px;
    width: 45%;
  }
  
  button {
    padding: 10px 20px;
    background-color: #00ff00;
    color: #121212;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
  }
  
  button:hover {
    background-color: #00cc00;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    margin-bottom: 5px;
    display: block;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  </style>
  