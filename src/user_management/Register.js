import React from 'react';
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import {HTTPpost} from "../usables/EasyHTTP";

const Register = () => {
    const [usernameValue, setUsernameValue] = React.useState("")
    const [passwordValue, setPasswordValue] = React.useState("")
    const [summonerNameValue, setSummonerNameValue] = React.useState("")

    const handleUsernameInput = (event) => {
        setUsernameValue(event.target.value);
    }
    const handlePasswordInput = (event) => {
        setPasswordValue(event.target.value);
    }
    const handleSummonerNameInput = (event) => {
        setSummonerNameValue(event.target.value);
    }

    const handleLoginSubmit = (event) => {
        HTTPpost(`${ENVIRONMENT_VARIABLES.url}/register`, {
            "username": usernameValue, 
            "password": passwordValue,
            "summonerName": summonerNameValue
        }).then(
            response => console.log(response)
        )
        event.preventDefault();
    }

    return ( 
        <form onSubmit={handleLoginSubmit}>
            <label htmlFor="username">username</label>
            <input id="username" placeholder="Enter your username..." autoFocus onChange={handleUsernameInput} />
            <label htmlFor="password">password</label>
            <input id="password" placeholder="Enter your password..." onChange={handlePasswordInput} />
            <label htmlFor="summonerName">summoner name</label>
            <input id="summonerName" placeholder="Enter your summoner name..." onChange={handleSummonerNameInput} />
            <button type="submit" disabled={!usernameValue || !passwordValue || !summonerNameValue}>Register</button>
        </form>
    );
}
 
export default Register;
