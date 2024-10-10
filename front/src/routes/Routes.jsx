import React from 'react'
import { Switch, Route, Redirect } from 'react-router'
import Home from '../components/home/Home'
import Relatorio from '../components/relatorio/RelatorioPage'
import Login from '../components/login/loginPage'
import UserServices from '../services/UserService';

const userService = new UserServices();



const Routes = () => (
    <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/teacher' component={Relatorio} />
        <Route path='/login' component={Login} />
        <Redirect from='*' to='/' />
    </Switch>
);





export default Routes;