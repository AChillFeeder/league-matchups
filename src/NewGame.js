import useFetch from './usables/useFetch.js';
import NotesForm from './currentGame/NotesForm.js';
import OpponentsChoice from './currentGame/OpponentsChoice.js';
import { useState } from 'react';
import { ReactSession } from 'react-client-session';
import { useHistory } from 'react-router';

const NewGame = () => {

    const {data: current_game, isLoading, fetch_error} = useFetch(`http://localhost/currentGame`)

    const [isChoosing, setIsChoosing] = useState(true);
    const [championChoice, setChampionChoice] = useState(null);

    return ( 
        <div className="new-game">
            {
                (current_game && !("error" in current_game)) 
                && // Current_game data should NOT be null AND there should be no errors
                ( 
                    isChoosing ? 
                        <OpponentsChoice // if isChoosing => Opponent choice 
                            opponents={current_game["opponents"]} 
                            setIsChoosing={setIsChoosing}
                            setChampionChoice={setChampionChoice}
                        /> 
                        : 
                        // if isChoosing is false => Notes taking
                        <NotesForm 
                            championChoice={championChoice}
                            summonerInGame={current_game["summonerInGame"]}
                        />
                )
            }

            {
                isLoading && <p>Loading...</p>
            }
            {
                ((current_game && current_game["error"]) || fetch_error) && <p>Error: {current_game["error"] || fetch_error}</p>
            }
        </div>
     );
}
 
export default NewGame;