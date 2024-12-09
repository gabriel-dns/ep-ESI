import React, { Component } from 'react'
import Main from '../template/Main'
import AcademicServices from '../../services/AcademicServices'
import Util from '../../util/util';

const util = new Util();
const academicServices = new AcademicServices()


const headerProps = {
    icon: '',
    title: 'CADASTRO DE USUARIOS',
    subtitle: 'Tela de cadastro de usuarios'
}

const initialState = {
    dados: { numeroUsp: "", emailCadastro:"", senhaCadastro:"", nivelCadastro:"" },
    list: [],

};


export default class CadastroUsuarios extends Component {
    

    state = { ...initialState }

    async componentWillMount() {
        util.autenticacao()
        const urlParams = new URLSearchParams(window.location.search);
        const numeroUsp = urlParams.get('numerousp');

        this.clear()
    }

    cadastrarUsuario(){
        console.log(this.state.dados)
       var response = academicServices.cadastrarUsuario(this.state.dados.numeroUsp,this.state.dados.emailCadastro, this.state.dados.senhaCadastro,this.state.dados.nivelCadastro);
 
        alert("Usuario cadastrado com sucesso")
      
    }

    updateField(event) {
        const dados = { ...this.state.dados }
        dados[event.target.name] = event.target.value
        this.setState({ dados })
    }

    clear() {
        this.setState({ dados: initialState.dados })
    }

    renderForm() {
        return (
            <div className="form">
                
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>numero Usp:</label>
                            <input type="text" className="form-control"
                                name="numeroUsp"
                                value={this.state.dados.numeroUsp}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite o numero Usp..." />
                        </div>
                    </div>
                  
                </div> 
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Email:</label>
                            <input type="text" className="form-control"
                                name="emailCadastro"
                                value={this.state.dados.emailCadastro}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite o email..." />
                        </div>
                    </div>
                  
                </div> 
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Senha</label>
                            <input type="password" className="form-control"
                                name="senhaCadastro"
                                value={this.state.dados.senhaCadastro}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite a senha..." />
                        </div>
                    </div>
                  
                </div>
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Tipo de Usuario</label>
                            <input type="text" className="form-control"
                                name="nivelCadastro"
                                value={this.state.dados.nivelCadastro}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite o tipo do usuario..." />
                        </div>
                    </div>
                  
                </div>

                <hr />
                <div className="row">
                    <div className="col-12 d-flex justify-content-end">
                        <button className="btn btn-primary"
                           onClick={() => this.cadastrarUsuario()}>
                            Cadastrar
                        </button>
                        <button className="btn btn-secondary ml-2"
                            onClick={e => this.clear(e)}>
                            Cancelar
                        </button>
                    </div>
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