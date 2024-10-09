import React, { Component, useState  } from 'react'
import Main from '../template/Main'
import './loginPage.css'
//import { NavLink, useNavigate } from 'react-router-dom'
import UserService from '../../services/UserService'

const userService = new UserService()

const headerProps = {
    icon: '',
    title: 'Bem vindo',
    subtitle: 'Sistema de pos graduação'
}
const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//const navigate = useNavigate()


 const initialState = {
    user: { senha: '', email: '', token: ' '},
    validators: { mailError : '', passErrors: ' ' }
}


//this.state.user.name
export default class login extends Component {

    state = { ...initialState }


    async login() {
        console.log('teste: ')
        const dados = { ...this.state.user }

        if(this.validaCamposLogin()){
            alert('Preecha devidamente seu email e senha!')
            return false
        }
        console.log(dados.email)
        console.log(dados.senha)
        var responseLogin = await userService.login(dados)

        userService.testeValores()

        console.log(responseLogin)





    }

    validaCamposLogin(){
        const validators = { ...this.state.validators }
        if(validators.mailError !='' || validators.passErrors !='') return true

        return false
    }
    updateField(event) {
        var label = event.target.name
        var value = event.target.value
        const user = { ...this.state.user }
        user[label] = value
        this.setState({ user })

        this.validaCampos(label, value)
    }

    validaCampos(label, value){
        if(label == 'email') this.validarEmail(value)
        else this.validarSenha(value)
    }
    validarSenha(senha){
        if(senha.length < 6){
            this.setState((prevState) => ({
                ...prevState,
                validators: { ...prevState.validators, passErrors: 'Senha Invalida' }
              }));
        }else{
            this.setState((prevState) => ({
                ...prevState,
                validators: { ...prevState.validators, passErrors: '' }
              }));
        }

    }
     validarEmail (email){

        if(regex.test(email)){
            this.setState((prevState) => ({
            ...prevState,
            validators: { ...prevState.validators, mailError: '' }
          }));
        }else{
            this.setState((prevState) => ({
                ...prevState,
                validators: { ...prevState.validators, mailError: 'Email invalido' }
              }));
        }
    }

    renderForm() {
        return (
            <div class="login-form col-md-4">
            <h3>Login</h3>
            <div>
             
              <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" name='email' placeholder="Digite seu email" onChange={e => this.updateField(e)} value={this.state.user.email} 
               
                required/>
              </div>
              <div class="mb-3">
                <b class='text-danger'>{this.state.validators.mailError}</b>
              </div>
        
           
              <div class="mb-3">
                <label for="password" class="form-label">Senha</label>
                <input type="password" class="form-control" name='senha' id="password" placeholder="Digite sua senha" onChange={e => this.updateField(e)} value={this.state.user.senha} required/>
              </div>
              <div class="mb-3">
                <b class='text-danger'>{this.state.validators.passErrors}</b>
              </div>
        
        
          
              <button 
              class="btn btn-primary w-100" 
              onClick={e => this.login(e)}
              >
                Entrar
                </button>
        
            </div>
          </div>
        )
    }
    render() {
        return (
            <Main {...headerProps}>
                {this.renderForm()}

            </Main>
        )
    }
}