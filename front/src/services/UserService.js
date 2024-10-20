import api from './api'

export default class UserServices {


  async login (dados) {
    const {data} = await api.get('/login', dados)
    var response 
    //config Para testes locais com jsonServer
    if(process.env.REACT_APP_AMBIENTE == 'dev'){
       response = data.filter(lista => (lista.email == dados.email))
       response =response[0]
    }

    if (data) {
      localStorage.setItem("nome", response.nome)
      localStorage.setItem("email", response.email)
      localStorage.setItem("numeroUsp", response.numeroUsp)
      localStorage.setItem("niveluser", response.nivelUser)

    }
    window.location.href = "/"

  }
  autenticacao () {
    var numeroUsp = localStorage.getItem("numeroUsp")
    var retorno = localStorage.getItem("numeroUsp") != null ? true : false
    console.log("Conteudo numeroUsp")
    console.log(numeroUsp)
    console.log("Teste numeroUsp")
    console.log(retorno)
    return retorno
  }


  testeValores () {
    var testeValor = localStorage.getItem("niveluser")
    console.log("testando valores:")
    console.log(testeValor)

  }



  logout(){
    localStorage.removeItem("nome")
    localStorage.removeItem("email")
    localStorage.removeItem("numeroUsp")
  
    
  }


}