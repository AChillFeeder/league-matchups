import React from 'react';
import ENVIRONMENT_VARIABLES from "./ENVIRONMENT_VARIABLES.json";
import {HTTPget, HTTPpost} from "./EasyHTTP";
import { useHistory } from 'react-router-dom';


// send post request with user data
const Login = () => {

    let history = useHistory();

    const [usernameValue, setUsernameValue] = React.useState("")
    const [passwordValue, setPasswordValue] = React.useState("")

    const handleUsernameInput = (event) => {
        setUsernameValue(event.target.value);
    }
    const handlePasswordInput = (event) => {
        setPasswordValue(event.target.value);
    }

    const handleLoginSubmit = (event) => {
        HTTPpost(`${ENVIRONMENT_VARIABLES.url}/connect`, {"username": usernameValue, "password": passwordValue})
        .then( data => {
            if(data.success)  history.push("/home")
        })

        event.preventDefault();
    }

    return ( 
        <form onSubmit={handleLoginSubmit}>
            <label htmlFor="username">username</label>
            <input id="username" placeholder="Enter your username..." autoFocus onChange={handleUsernameInput} />
            <label htmlFor="password">password</label>
            <input id="password" placeholder="Enter your password..." onChange={handlePasswordInput} />
            <button type="submit" disabled={!usernameValue || !passwordValue}>Login</button>
        </form>
    );
}
 
export default Login;
