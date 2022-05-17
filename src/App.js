
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Register from './user_management/Register';
import Login from './user_management/Login';

import Navbar from './Navbar';
import Home from './home_components/Home';
import CurrentGame from './CurrentGame';

const App = () => {
  return (
    <Router>
        <div className="App">
        
        <div className="content">
            <Switch>
                <Route exact path="/">
                    <Login />
                </Route>
                <Route path="/register">
                    <Register />
                </Route>
                <Route path="/home">
                    <Navbar />
                    <Home />
                </Route>
                <Route path="/currentGame">
                    <Navbar />
                    <CurrentGame />
                </Route>
                <Route path="*">
                    {/* <NotFound /> */}
                </Route>
            </Switch>
        </div>
        </div>
    </Router>
    );
}

export default App;