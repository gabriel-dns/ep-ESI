

export default class Util {



  autenticacao () {
    var token = localStorage.getItem("token")
    var autenticado = localStorage.getItem("token") != 852 ? true : false
    console.log("Conteudo token")
    console.log(token)
    console.log("Teste token")
    console.log(autenticado)

    !autenticado ? window.location.href = "/": false
  
  }


}