import React, { Component } from 'react'
import Main from '../template/Main'
import AcademicServices from '../../services/AcademicServices'
import Util from '../../util/util';

const util = new Util();
const academicServices = new AcademicServices()


const headerProps = {
    icon: '',
    title: 'CADASTRO DE DATA MAXIMA',
    subtitle: 'Tela de cadastro de data maxima'
}

const initialState = {
    dados: { dataMaxima: '' },
    list: [],

};


export default class DataMaxima extends Component {
    

    state = { ...initialState }

    async componentWillMount() {
        util.autenticacao()
        const urlParams = new URLSearchParams(window.location.search);
        const numeroUsp = urlParams.get('numerousp');
    }

    cadastrarData(dataMaxima){
       var response = academicServices.cadastrarDataMaxima();

       if(response.sucesso){
        alert('Data cadastrada com sucesso')
       }else{
        alert('Erro ao cadastrar')
       }
      
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
                            <label>Data maxima para entrega dos relatorios do semestre:</label>
                            <input type="text" className="form-control"
                                name="dataMaxima"
                                value={this.state.dados.dataMaxima}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite a data..." />
                        </div>
                    </div>
                  
                </div>

                <hr />
                <div className="row">
                    <div className="col-12 d-flex justify-content-end">
                        <button className="btn btn-primary"
                            onClick={e => this.cadastrarData(e)}>
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