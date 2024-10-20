import api from './api'

export default class UserServices {


  async login (dados) {

     const requestJson = JSON.stringify(dados);

    const {data} = await api.post('/login', requestJson)
    var response = data
    console.log('--------------TESTE RETORNO-------------')
    console.log(data)

    //config Para testes locais com jsonServer
     if(process.env.REACT_APP_AMBIENTE == 'dev'){
      console.log("DEV")
        response = data.filter(lista => (lista.email == dados.email))
        response =response[0]
     }

     if (response.numero_usp != null) {
       localStorage.setItem("email", response.email)
       localStorage.setItem("numeroUsp", response.numero_usp)
       localStorage.setItem("niveluser", response.nivel)
       window.location.href = "/"
     }else{
       alert('Email ou senha Incorreto')
     }
 

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
    localStorage.removeItem("email")
    localStorage.removeItem("numeroUsp")
    localStorage.removeItem("niveluser")
  
    
  }


}