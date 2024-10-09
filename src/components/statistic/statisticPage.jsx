import React, { Component } from 'react'
import axios from 'axios'
import Main from '../template/Main'
import './statisticPage.css'

const headerProps = {
    icon: 'bi bi-activity',
    title: 'Estatisticas',
    subtitle: 'Dados acerca das Disciplinas'
}

const baseUrl = 'http://localhost:3001/medias'
const initialState = {
    user: { name: '', email: '' },
    list: []
}

export default class Teacher extends Component {

    state = { ...initialState }

    componentWillMount() {
        axios(baseUrl).then(resp => {
            this.setState({ list: resp.data })
        })
    }

    clear() {
        this.setState({ user: initialState.user })
    }

    save() {
        const user = this.state.user
        const method = user.id ? 'put' : 'post'
        const url = user.id ? `${baseUrl}/${user.id}` : baseUrl
        axios[method](url, user)
            .then(resp => {
                const list = this.getUpdatedList(resp.data)
                this.setState({ user: initialState.user, list })
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
           <div></div>
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
            <table className="table mt-4">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Disciplina</th>
                        <th>Media Geral</th>
                     
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
                backgroundColor: 'yellow',
                width: '10px'
              };
              styles.backgroundColor =user.color
              styles.width =100*user.media
            return (
                <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.disciplina}</td>
                    <td>{user.media}</td>
                    <td ><div style={styles} >_</div></td>
                    
                    
                </tr>
            )
        })
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