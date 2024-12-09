import api from './api'

export default class AcademicServices {

  async getAlunos(numeroUsp){

    var orientador =''

    if(numeroUsp != null){
      console.log("Chamada da tela por CCP")
      orientador =numeroUsp
    }else{
      console.log("Chamada da tela por ORIENTADOR")
      orientador = localStorage.getItem("numeroUsp")
    }
    console.log('NUMERO USP ORIENTADO: '+orientador)

    const {data} = await api.get('/'+orientador+'/alunos', orientador)
    var dadosAluno =  []

    console.log("dados retorno: ")
    console.log(data)

    data.alunos.map(alu => {
      dadosAluno.push({
        "nome": alu.nome,
        "numeroUsp": alu.nusp
      })

    })


    return dadosAluno
  }

  async getOrientadores(){

    const {data} = await api.get('/professores')
    console.log("dados retorno: ")
    console.log(data)

    return data

  }
  async getdadosAlunos(numeroUsp){

    var aluno =''

    if(numeroUsp != null){
      console.log("Chamada da tela por ORIENTADOR/CCP")
      aluno =numeroUsp
    }else{
      console.log("Chamada da tela por ALUNO")
      aluno = localStorage.getItem("numeroUsp")
    }

    const {data} = await api.post('/aluno/dados?numero_usp=' + numeroUsp)
    console.log("get dadosAlunos dados retorno: ")
    console.log(data)

    return data.dados

  }
  async cadastrarDataMaxima(dataMaxima){

    var dadosEmail = {
      "subject": "Prazo de entrega de relatorio Definido!",
      "deadline": dataMaxima 
    }
    const {data} = await api.post('/send_report_email', dadosEmail)
    console.log("dados retorno: ")
    console.log(data)

    const {data2} = await api.post('/cadastrar/dataMaxima', dadosEmail)
    console.log("dados retorno: ")
    console.log(data2)
    

  }
  async cadastrarUsuario(numeroUsp, email,senha,nivel){

    var dadoscadastro = {
      "numerousp": numeroUsp,
      "email": email, 
      "senha": senha, 
      "nivel": nivel, 
    }

    console.log("testes -- ")
    console.log(dadoscadastro)

    const {data2} = await api.post('/usuarios', dadoscadastro)
    console.log("dados retorno: ")
    console.log(data2)
    

  }
  async atribuir(dados){

    var request = {
      "aluno": dados.numeroUSP_aluno,
      "orientador": dados.orientador 
    }
    console.log("Request")
    console.log(request)
    const {data} = await api.post('/atribuir', request)
    console.log("dados retorno: ")
    console.log(data)


  }


}