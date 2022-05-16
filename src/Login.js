import React from 'react';
import ENVIRONMENT_VARIABLES from "./ENVIRONMENT_VARIABLES.json";
import {HTTPget, HTTPpost} from "./EasyHTTP";


// send post request with user data
const Login = () => {

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
<<<<<<< HEAD
        .then( data => {
            if(data.success)  history.push("/home")
        })
=======
        .then( data =>
            console.log(data)
        )
>>>>>>> parent of 85a8f3a... Data properly retrieved in Home, ListOfGames and Games work, starting on Search function

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
