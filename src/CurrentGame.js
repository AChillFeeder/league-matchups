import React from 'react';
import ENVIRONMENT_VARIABLES from "./usables/ENVIRONMENT_VARIABLES.json";
import {HTTPget} from "./usables/EasyHTTP";
import OpponentChoice from './OpponentChoice';

const CurrentGame = () => {

    const [isLoading, setIsLoading] = React.useState(true);
    const [currentGameData, setCurrentGameData] = React.useState({});

    const getCurrentGame = () => {
        setIsLoading(true);
        console.log("fetching");
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/currentGame`)
        .then( data => {
                console.log(data);
                if(data.success){
                    setCurrentGameData(data);
                } else {
                    setCurrentGameData(false);
                }
                setIsLoading(false);
            }
        )
    }

    React.useEffect(() => {
        getCurrentGame();
    }, [])
    
    return ( 
        <div>
            {
            isLoading ? 
                <p>Loading...</p> : 
                currentGameData ? 
                    <OpponentChoice data={currentGameData}/> :
                    <p>Summoner isn't in game</p>
            }
        </div>
        // choice between picking opponent and current game menu
     );
}
 
export default CurrentGame;