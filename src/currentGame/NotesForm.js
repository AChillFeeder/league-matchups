import { useState } from 'react';
import ChampionPortrait from '../usables/ChampionPortrait.js';
import {ReactSession} from 'react-client-session';

const NotesForm = ({championChoice, playerChampion}) => {

    let [inputs, setInputs] = useState([])
    let [check, setCheck] = useState(false)
    let inputsValue = [];
    var summonerName = ReactSession.get("summonerName");

    function manageSubmit(event){
        event.preventDefault()

        let request = {
            "player-champion": playerChampion,
            "lane-opponent": championChoice,
            "win": check,
            "summoner-name": summonerName,
            "notes": inputsValue
        }

        fetch(`http://192.168.1.150:8000/${summonerName}/games`, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(request)
        }).then(() => {
            console.log('Game has been submitted');
        })

        event.target.reset()
    }

    return ( 
        <div className="notes-form">
            <h3>Your champion: {playerChampion}</h3>
            <ChampionPortrait championName={playerChampion}/>
            <h3>Opponent champion: {championChoice}</h3>
            <ChampionPortrait championName={championChoice}/>

            <form onSubmit={manageSubmit}>
                <h3>Add notes: </h3>
                
                {inputs.map((input)=>(
                    <input 
                        key={input} 
                        id={input} 
                        className="notes"
                        autoComplete="off"
                        onChange={(event) => {
                            inputsValue[input] = event.target.value;
                        }}
                    />
                ))}

                <button onClick={(event) => {
                    event.preventDefault();
                    // setInput is needed for the component to update and show new inputs
                    setInputs(inputs.concat([inputs.length])); 
                }}>
                    New note
                </button>

                <label htmlFor="victory">Victory: </label>
                <input 
                    type="checkbox" 
                    name="victory" 
                    id="victory"
                    defaultChecked={false}
                    onChange={() => setCheck(!check)}
                />
                <button>Submit</button>
            </form>
        </div>
     );
}
 
export default NotesForm;