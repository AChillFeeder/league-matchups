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
                            <p key={Math.ceil(Math.random()*100)}><span>Note#{game["notes"].indexOf(note)+1}</span>: {note}</p>
                            ))
                        }
                </div>
                <div className="tags">
                    <h3>Tags: </h3>
                    {
                        game["tags"].map((tag)=>(
                            <p key={Math.ceil(Math.random()*100)}>{tag}</p>
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