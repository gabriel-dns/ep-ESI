import React, { Component } from 'react'
import axios from 'axios'
import Main from '../template/Main'

import './discipline.css'

const headerProps = {
    icon: '',
    title: 'Disciplinas',
    subtitle: 'Busca por Disciplinas, bibliografia e descrição'
}


const baseUrl = 'http://localhost:3001/disciplinas'
const initialState = {
    user: { name: '', email: '' },
    list: []
}

export default class Teacher extends Component {

    state = { ...initialState }
    

    //  componentWillMount() {
    //      axios(baseUrl).then(resp => {
    //          this.setState({ list: resp.data.filter(lista => (lista.id == 852)) })
    //      })
    //  }

    clear() {
        this.setState({ user: initialState.user })
    }

    find() {
        // console.log(this.state.user.name)

         axios(baseUrl).then(resp => {
             this.setState({ list: resp.data.filter(lista => (lista.id == this.state.user.name)) })
         })
        
    }

    getUpdatedList(user, add = true) {
        const list = this.state.list.filter(u => u.id !== user.id)
        if(add) list.unshift(user)
        return list
    }

    updateField(event) {
        const user = { ...this.state.user }
        user[event.target.name] = event.target.value
        this.setState({ user })
    }

    renderForm() {
        return (
            <div className="form">
                <div className="row">
                    <div className="col-12 col-md-6">
                        <div className="form-group">
                            <label>Codigo da Disciplina</label>
                            <input type="text" className="form-control"
                                name="name"
                                value={this.state.user.name}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite o codigo..." />
                        </div>
                    </div>

                    
                </div>

                <hr />
                <div className="row">
                    <div className="col-12 d-flex justify-content-end">
                        <button className="btn btn-primary"
                            onClick={e => this.find(e)}>
                            Buscar
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

    load(user) {
        this.setState({ user })
    }

    remove(user) {
        axios.delete(`${baseUrl}/${user.id}`).then(resp => {
            const list = this.getUpdatedList(user, false)
            this.setState({ list })
        })
    }

    renderTable() {
        return (
            <div>      
            
            
                    {this.renderRows()}
          
            </div>
        )
    }

    renderRows() {
         var teste =  this.state.list
         console.log("teste")
         if(teste != undefined)

        return this.state.list.map(user => {
            // console.log(this.state.list[0].disciplinas)
            // console.log(user)
            // console.log(user.disciplinas)

    
                return (
                    <div className='disciplina'>
                        
                        <h1><spam>Disciplina: </spam> {user.nome}</h1>
                        <h1><spam>Oferecimento: </spam> {user.professor}</h1>
                        <h1><spam>Turmas: </spam> {user.turmas}</h1>
                        <h1><spam>Livro Texto: </spam>Matematica Aplicada conceitos e...</h1>
                        <h2><b>Descrição Detalhada: </b> <br/>{user.desc} ...<spam>ver mais</spam> </h2>
                        {/* <td>{user.id}</td>
                        <td>{user.disciplina}</td>
                        <td>{user.nota}</td> */}
                       
                    </div>
    
                )
         
          
        }
        
        )
    }
    
    render() {
        return (
            <Main {...headerProps}>
                {this.renderForm()}
                {this.renderTable()}
            </Main>
        )
    }
}