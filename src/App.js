import './App.css';
import Navbar from './Navbar.js';
import Home from './Home.js';
import NewGame from './NewGame.js';

import Login from './account/Login.js'
import Register from './account/Register.js'

import GameDetails from './previousGames/GameDetails.js'

import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

function App() {
  return (
    <Router>
        <div className="App">
            <div className="content">
                <Switch>
                    <Route exact path='/'>
                        <Login></Login>
                    </Route>
                    <Route exact path='/register'>
                        <Register></Register>
                    </Route>
                    <Route exact path='/home'>
                        <Navbar></Navbar>
                        <Home></Home>
                    </Route>
                    <Route exact path='/new-game'>
                        <Navbar></Navbar>
                        <NewGame></NewGame>
                    </Route>
                    <Route exact path='/game/:id'>
                        <Navbar></Navbar>
                        <GameDetails></GameDetails>
                    </Route>
                </Switch>
            </div>
        </div>
    </Router>
  );
}

export default App;
