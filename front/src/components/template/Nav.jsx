import './Nav.css'
import React, { Component, useState  } from 'react'
import { Link } from 'react-router-dom'
import Util from '../../util/util';

const util = new Util();

const initialState = {
    dadosMenu: { usuario: '', listaMenu: '' }
}

function encerrarSessao(){
    console.log("chegou aqui")
    util.logout();
}

export default class Menu extends Component {

    state = { ...initialState }



    componentWillMount() {
      var tipoUsuario =  util.controleDeAcesso()
      console.log("Tipo usuario:")
      console.log(tipoUsuario)
    

      var menuComponent 
      switch(tipoUsuario){
        case 'aluno':
            menuComponent = navAluno()
          break
        case 'orientador':
            menuComponent = navOrientador()
            break
        case 'CCP':
            menuComponent = navCCP()
            break
        default:
            menuComponent = navDefault()
            
      }
      this.setState(initialState.dadosMenu.listaMenu = menuComponent)



        //window.location.href = "/";
    }

    render() {
        return (
            <aside className="menu-area">
                { this.state.dadosMenu.listaMenu}
           
        </aside>
        )
    }
   
}
 


const navDefault = () => {
    return (
       
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/login">
             Login
            </Link>
          
        </nav>
  
    
)
}
const navAluno = () => {
    return (
       
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/relatorio">
              Relatorio
            </Link>
            <b className="logout" onClick={() => encerrarSessao()}>
             Sair
            </b>
            
        </nav>
 )
}

const navOrientador = () => {
    return (
        
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/alunos">
              Alunos
            </Link>
            <b className="logout" onClick={() => encerrarSessao()}>
             Sair
            </b>
        </nav>
  )
}
const navCCP = () => {
    return (
      
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/relatorio">
              Orientadores
            </Link>
            <b className="logout" onClick={() => encerrarSessao()}>
             Sair
            </b>
        </nav>
   )
}

