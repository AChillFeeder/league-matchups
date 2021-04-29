import { useState } from 'react';
import ChampionPortrait from '../usables/ChampionPortrait.js';
import {ReactSession} from 'react-client-session';
import {useHistory} from 'react-router-dom';

const NotesForm = ({championChoice, playerChampion}) => {

    let [inputs, setInputs] = useState([]) // manages number of inputs
    let [check, setCheck] = useState(false)
    let [tags, setTags] = useState([])
    
    var summonerName = ReactSession.get("summonerName");

    let history = useHistory();

    function manageSubmit(event){
        event.preventDefault()

        let inputsValue = [];
        inputs.map((input) => ( inputsValue.push(document.getElementById(String(input)).value)) )

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
        }).then(() => {
            event.target.reset()
            history.push('/home')
        })

    }

    function inputStyle(options) {
        return {
            borderRadius: 2,
            background: "none",
            border: "0",
            outline: "0",
            borderBottom: "1px solid var(--secondary-color)",
            padding: "5px",
            width: "80%",
            alignSelf: "center",
        }
    }

    return ( 
        <div className="notes-form">
            <div className="champion-card">
                <ChampionPortrait championName={playerChampion}/>
                <h3>{playerChampion}</h3>
            </div>

            <form onSubmit={manageSubmit}>
                <h2>Add notes: </h2>

                <button 
                    onClick={(event) => {
                        event.preventDefault();
                        // setInput is needed for the component to update and show new inputs
                        setInputs(inputs.concat([inputs.length])); 
                    }}
                    className="add-note"
                >
                    New note
                </button>
                
                {inputs.map((input)=>(
                    <div className="input">
                        <input 
                            key={input} 
                            id={input} 
                            className="notes"
                            autoComplete="off"
                            placeholder="Your note..."
                            style={inputStyle()}
                            // onChange={(event) => {
                            //     let text = event.target.value;
                            //     let words = text.split(" ");
                            //     words.map((word) => {
                            //         if(word[0] === "@" && !tags.includes(word)){
                            //             setTags(tags.push(word))
                            //         }
                            //     })
                            // }}
                        />
                        {/* <div className="tags">
                            {tags && tags.map((tag) => (
                                <p className="tag">{tag}</p>
                            ))}
                            {console.log(tags)}
                        </div> */}
                    </div>
                ))}

                <label htmlFor="victory">Victory: </label>
                <input 
                    type="checkbox" 
                    name="victory" 
                    id="victory"
                    defaultChecked={false}
                    onChange={() => setCheck(!check)}
                />
                <button className="submit">Submit</button>
            </form>

            <div className="champion-card">
                <ChampionPortrait championName={championChoice}/>    
                <h3>{championChoice}</h3>
            </div>

        </div>
     );
}
 
export default NotesForm;