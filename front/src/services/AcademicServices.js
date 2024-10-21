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

    const {data} = await api.get('/orientadores')
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

    const {data} = await api.get('/dados', numeroUsp)
    console.log("getdadosAlunos dados retorno: ")
    console.log(data)

    return data
  
  }
  async cadastrarDataMaxima(dataMaxima){

    const {data} = await api.post('/cadastrarDataMaxima', dataMaxima)
    return data
  
  }



}