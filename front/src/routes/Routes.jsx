import React from 'react'
import { Switch, Route, Redirect } from 'react-router'
import Home from '../components/home/Home'
import Relatorio from '../components/relatorio/RelatorioPage'
import DataMaxima from '../components/dataMaxima/DataMaxima'
import Alunos from '../components/alunos/alunos'
import Orientadores from '../components/orientadores/orientadores'
import AtribuirOrientadores from '../components/AtribuirOrientadores/AtribuirOrientadores'
import Login from '../components/login/loginPage'
import UserServices from '../services/UserService';

const userService = new UserServices();



const Routes = () => (
    <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/relatorio' component={Relatorio} />
        <Route path='/alunos' component={Alunos} />
        <Route path='/orientadores' component={Orientadores} />
        <Route path='/login' component={Login} />
        <Route path='/datamaxima' component={DataMaxima} />
        <Route path='/atribuir' component={AtribuirOrientadores} />
        <Redirect from='*' to='/' />
    </Switch>
);





export default Routes;