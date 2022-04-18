import {Link} from 'react-router-dom';
import { useState } from "react";
import { useHistory } from "react-router";

const Register = () => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [summoner, setSummoner] = useState('')
    const [error, setError] = useState(null);

    const history = useHistory();

    const handleSubmit = (event) => {
        event.preventDefault();

        fetch(`/register`, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({"username": username, "password": password, "summonerName": summoner})
        }).then(response => response.json())
        .then((data) => {
            if(data.registered){
                history.push('/')
            }else{
                setError(data.message)
            }
        })


        event.target.reset();
    }

    return ( 
        <div className="register">
            {error && <p>error: {error}</p>}
            <form onSubmit={(event) => handleSubmit(event)}>
                <label htmlFor="username">Username:</label>
                <input type="text" name="username" placeholder="Enter your username" onChange={(e) => setUsername(e.target.value)} className="form-input"/>
                <label htmlFor="password">Password:</label>
                <input type="password" name="password" placeholder="Enter your password" onChange={(e) => setPassword(e.target.value)} className="form-input"/>
                <label htmlFor="summoner-name">Summoner-name:</label>
                <input type="text" name="summoner-name" placeholder="Enter your summoner name" onChange={(e) => setSummoner(e.target.value)} className="form-input"/>
                <button>Register</button>
                <Link to='/'>Already have an account?</Link>
            </form>
        </div>
     );
}
 
export default Register;