
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Register from './Register';
import Login from './Login';

import Navbar from './Navbar';
import Home from './Home';

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
                <Route path="/blogs/:id">
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