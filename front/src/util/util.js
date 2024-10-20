

export default class Util {



  autenticacao () {
    var numeroUsp = localStorage.getItem("numeroUsp")
    var autenticado = localStorage.getItem("numeroUsp") != null ? true : false
    console.log("Conteudo numeroUsp")
    console.log(numeroUsp)
    console.log("Teste numeroUsp")
    console.log(autenticado)

    !autenticado ? window.location.href = "/": false
  
  }

  controleDeAcesso(){
    var nivelUsuario = localStorage.getItem("niveluser")
    switch(nivelUsuario){
      case 'A':
        return 'aluno'
      case 'O':
        return 'orientador'
      case 'C':
        return 'CCP'
    }


  }

  logout(){
    console.log('LOGOUT')
    localStorage.removeItem("nome")
    localStorage.removeItem("email")
    localStorage.removeItem("numeroUsp")
    localStorage.removeItem("niveluser")
    window.location.href = "/"
    window.location.reload()
    
  }

}