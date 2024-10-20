import React, { Component } from 'react'
import Main from '../template/Main'
import AcademicServices from '../../services/AcademicServices'
import Util from '../../util/util';

const util = new Util();
const academicServices = new AcademicServices()



const headerProps = {
    icon: '',
    title: 'Alunos',
    subtitle: 'Tela de Listagem de alunos'
}

const initialState = {
    user: { name: '', email: '' },
    list: []
}


export default class Orientadores extends Component {
    

    state = { ...initialState }

   async componentWillMount() {
        util.autenticacao()
        var  orientadoresResponse = await academicServices.getOrientadores()
        console.log("Lista de Alunos" + orientadoresResponse)
        this.setState({ list: orientadoresResponse })
    }

    consultarAlunos(numeroUsp){
        console.log("Numero usp: " + numeroUsp)
        window.location.href = "/alunos?numerousp="+numeroUsp

    }






 

    renderTable() {
        return (
            <table className="table mt-4">
                <thead>
                    <tr>
                        <th>Numero USP </th>
                        <th>Nome</th>
                        <th>Dados</th>
                    </tr>
                </thead>
                <tbody>
                    {this.renderRows()}
                </tbody>
            </table>
        )
    }

    renderRows() {
        return this.state.list.map(user => {
            let styles = {
                width: '35px'
              };
            return (
                <tr key={user.numeroUsp}>
                    <td>{user.numeroUsp}</td>
                    <td>{user.name}</td>
                {/* <td> <img style={styles}  src={curriculo}/>  </td> */}
                    <td>
                        <button className="btn btn-warning"
                            onClick={() => this.consultarAlunos(user.numeroUsp)}>
                            <i className="fa fa-pencil"></i>
                        </button>
                    </td>
                </tr>
            )
        })
    }
    
    render() {
        return (
            <Main {...headerProps}>
                {this.renderTable()}
            </Main>
        )
    }
}