import { useState } from 'react';
import { Redirect } from 'react-router';
import ChampionThumbnail from '../usables/ChampionThumbnail.js';

const PreviousGames = ({games}) => {
    
    const [showDetails, setShowDetails] = useState(null);

    return ( 
        <div className="previous-games">
            {
                games.map((game) => (
                    <div 
                    style={{
                        backgroundColor: game['win'] ? 'rgba(49, 190, 73, 0.100)' : 'rgba(184, 68, 68, 0.100)'
                    }}
                    className="game" 
                    key={game["id"]}
                    onClick={() => {
                        // show details
                        setShowDetails(game)
                    }}
                    >
                        {/* Your champion */}
                        <ChampionThumbnail championName={game["player-champion"]}/>
                        
                        {/* Enemy champion */}
                        <ChampionThumbnail championName={game["lane-opponent"]}/>
                        
                        <h3
                           style={{color: game['win'] ? 'green' : 'red'}}
                        >
                            {game["win"] ? 'Victory' : 'Defeat'}
                        </h3>

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