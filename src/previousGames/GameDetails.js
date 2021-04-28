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
                
                <h3
                    style={{color: game['win'] ? 'green' : 'red'}}
                    >
                    {game["win"] ? 'Victory' : 'Defeat'}
                </h3>

                <div className="notes">
                    {
                        game["notes"].map((note)=>(
                            <p>{note}</p>
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