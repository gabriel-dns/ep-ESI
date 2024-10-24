import React, { Component } from 'react'
import Main from '../template/Main'
import AcademicServices from '../../services/AcademicServices'
import Util from '../../util/util';

const util = new Util();
const academicServices = new AcademicServices()



const headerProps = {
    icon: '',
    title: 'CCP',
    subtitle: 'Tela de Atribuição de Orientadores'
}

const initialState = {
    dados: { numeroUSP_aluno: '', orientador: '' },
    list: [],

};



export default class AtribuirOrientadores extends Component {
    

    state = { ...initialState }

   async componentWillMount() {
        util.autenticacao()
        var  orientadoresResponse = await academicServices.getOrientadores()
        console.log("Lista de Orientadores" + orientadoresResponse)
        this.setState({ list: orientadoresResponse })
    }

    atribuirOrientador(){
        academicServices.atribuir(this.state.dados)
        alert('Orientador atribuido com Sucesso!')
        this.clear()

    }
    updateField(event) {
        const dados = { ...this.state.dados }
        dados[event.target.name] = event.target.value
        this.setState({ dados })
    }

    clear() {
        this.setState({ dados: initialState.dados })
        const selectElement = document.getElementById('orientador');
        selectElement.value = 'vazio';

    }


    renderForm() {
        return (
            <div className="form">
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Digite o numero USP do aluno:</label>
                            <input type="text" className="form-control"
                                name="numeroUSP_aluno"
                                value={this.state.dados.numeroUSP_aluno}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite a data..." />
                        </div>
                    </div>
                  
                </div>
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Orientador:</label>
                            <select id="orientador" name="orientador"  onChange={e => this.updateField(e)}  className="form-control">
                            <option value="vazio">Selecione</option>
                        {  this.state.list.map(dados => {
                            return <option value={dados.numeroUsp}>{dados.name}</option>
                        })}

                    </select>

                        </div>
                    </div>
                  
                </div>

                <hr />
                <div className="row">
                    <div className="col-12 d-flex justify-content-end">
                        <button className="btn btn-primary"
                           onClick={() => this.atribuirOrientador()}>
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
  

    renderOptions(){
        return(
            <div>
    <select id="opcoes" name="opcoes">
        {  this.state.list.map(dados => {
            return <option value={dados.numeroUsp}>{dados.name}</option>
        })}

    </select>


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