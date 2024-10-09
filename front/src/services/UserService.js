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
      localStorage.setItem("token", response.token)

      return true
    }
  }
  autenticacao () {
    var token = localStorage.getItem("token")
    var retorno = localStorage.getItem("token") != 852 ? true : false
    console.log("Conteudo token")
    console.log(token)
    console.log("Teste token")
    console.log(retorno)
    return retorno
  }


  testeValores () {
    var testeValor = localStorage.getItem("token")
    console.log(testeValor)

  }


}