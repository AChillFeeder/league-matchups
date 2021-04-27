import {useLocation} from 'react-router-dom';
import ChampionPortrait from '../usables/ChampionPortrait.js';

const GameDetails = () => {
    const {state} = useLocation();
    const game = state.game
    return (
        <div className="game-details">
            {/* Your champion */}
            <ChampionPortrait championName={game["player-champion"]}/>
            
            {/* Enemy champion */}
            <ChampionPortrait championName={game["lane-opponent"]}/>
            <h3> Outcome: {game["win"] ? 'Victory' : 'Defeat'} </h3>

            <p>Number of notes: {game["notes"].length}</p>    

            <div className="notes">
                {
                    game["notes"].map((note)=>(
                        <p>{note}</p>
                    ))
                }
            </div>

        </div>
     );
}
 
export default GameDetails;