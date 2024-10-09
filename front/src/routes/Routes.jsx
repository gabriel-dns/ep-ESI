import React from 'react'
import { Switch, Route, Redirect } from 'react-router'

import Home from '../components/home/Home'
import Teacher from '../components/teacher/TeacherPage'
import Statistic from '../components/statistic/statisticPage'
import Login from '../components/login/loginPage'
import DisciplinePage from '../components/discipline/disciplinePage'
import UserServices from '../services/UserService';

const userService = new UserServices();



const Routes = () => (
    <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/teacher' component={Teacher} />
        <Route path='/statisticPage' component={Statistic} /> */
        <Route path='/login' component={Login} />
        <Route path='/discipline' component={  DisciplinePage  } />
        <Redirect to='/' />
    </Switch>
);





export default Routes;