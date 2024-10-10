import './Nav.css'
import React from 'react'
import { Link } from 'react-router-dom'

export default props =>
    <aside className="menu-area">
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/teacher">
              Relatorio
            </Link>
            <Link to="/login">
             Login
            </Link>
        </nav>
    </aside>


const navDefault = () => {
    return (
         <aside className="menu-area">
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/login">
             Login
            </Link>
        </nav>
    </aside>)
}
const navAluno = () => {
    return (
         <aside className="menu-area">
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/teacher">
              Relatorio
            </Link>
            <Link to="/login">
             Sair
            </Link>
        </nav>
    </aside>)
}

const navOrientadorCCP = () => {
    return (
         <aside className="menu-area">
        <nav className="menu">
            <Link to="/">
                 Início
            </Link>
            <Link to="/teacher">
              Alunos
            </Link>
            <Link to="/login">
             Sair
            </Link>
        </nav>
    </aside>)
}

