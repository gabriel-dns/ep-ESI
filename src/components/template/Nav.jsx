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
              Professores
            </Link>
            <Link to="/statisticPage">
            Estatisticas
            </Link>
            <Link to="/login">
             Login
            </Link>
            <Link to="/discipline">
             Disciplinas
            </Link>
        </nav>
    </aside>