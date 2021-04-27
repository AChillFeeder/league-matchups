import { useState } from 'react';
import { Redirect } from 'react-router';
import ChampionPortrait from '../usables/ChampionPortrait.js';

const PreviousGames = ({games}) => {
    
    const [showDetails, setShowDetails] = useState(null);

    return ( 
        <div className="previous-games">
            Here is the preview of your past few games.
            {
                games.map((game) => (
                    <div 
                    className="game" 
                    key={game["id"]}
                    onClick={() => {
                        // show details
                        setShowDetails(game)
                    }}
                    >
                        {/* Your champion */}
                        <ChampionPortrait championName={game["player-champion"]}/>
                        
                        {/* Enemy champion */}
                        <ChampionPortrait championName={game["lane-opponent"]}/>
                        
                        <h3>Outcome: {game["win"] ? 'victory' : 'defeat'}</h3>

                        <p>Number of notes: {game["notes"].length}</p>
                                
                        {
                            showDetails && 
                            <Redirect to={{
                                pathname: '/game/' + showDetails["id"],
                                state: { game: showDetails }
                            }} />
                        }

                    </div>
                ))
            }
        </div>
     );
}
 
export default PreviousGames;