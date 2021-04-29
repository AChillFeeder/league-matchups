import {useLocation} from 'react-router-dom';
import ChampionPortrait from '../usables/ChampionPortrait.js';

const GameDetails = () => {
    const {state} = useLocation();
    const game = state.game
    return (
        <div className="game-details">
            <div className="content">

                {/* Your champion */}
                <ChampionPortrait championName={game["player-champion"]}/>
                

                <div className="notes">
                    {
                        game["notes"].map((note)=>(
                            <p key={Math.ceil(Math.random()*100)}>-Note#{game["notes"].indexOf(note) + 1}: {note}</p>
                            ))
                        }
                </div>

                {/* Enemy champion */}
                <ChampionPortrait championName={game["lane-opponent"]}/>
            </div>
        </div>
     );
}
 
export default GameDetails;