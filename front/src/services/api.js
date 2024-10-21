import axios from 'axios';

// Configuração básica
const api = axios.create({
  //baseURL: 'http://localhost:3001', 
  baseURL: 'http://127.0.0.1:5000/api', 
  //baseURL: 'http://localhost:4040',
  timeout: 10000,  
  headers: {
    'Content-Type': 'application/json'
  },
});

export default api;