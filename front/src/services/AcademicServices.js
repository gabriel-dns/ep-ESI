import api from './api'

export default class AcademicServices {

  async getAlunos(){
    var orientador =localStorage.getItem("numeroUsp")

    const {data} = await api.get('/alunos', orientador)
    console.log("dados retorno: ")
    console.log(data)

    return data
  
    
  }
  async getdadosAlunos(numeroUsp){

    const {data} = await api.get('/dados', numeroUsp)
    console.log("getdadosAlunos dados retorno: ")
    console.log(data)

    return data
  
    
  }



}