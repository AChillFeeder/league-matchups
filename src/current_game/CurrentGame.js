import React from 'react';
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import {HTTPget} from "../usables/EasyHTTP";
import OpponentChoice from './OpponentChoice';
import LiveGameInterface from './LiveGameInterface';

const CurrentGame = () => {

    const [isLoading, setIsLoading] = React.useState(true);
    const [currentGameData, setCurrentGameData] = React.useState({});
    const [selectedOpponent, setSelectedOpponent] = React.useState(false);

    const getCurrentGame = () => {
        setIsLoading(true);
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

    React.useEffect(() => {
        // console.log("selected Opponent => ");
        // console.log(selectedOpponent);
    }, [selectedOpponent])
    
    return ( 
        <div>
            {
            isLoading ? 
                <p>Loading...</p> : 
                !currentGameData ? 
                    <p>Summoner isn't in game</p> :
                    selectedOpponent ?
                        <LiveGameInterface data={currentGameData} opponentChampion={selectedOpponent} setOpponent={setSelectedOpponent}/> :
                        <OpponentChoice data={currentGameData} setOpponent={setSelectedOpponent}/> 
            }
        </div>
        // choice between picking opponent and current game menu
     );
}
 
export default CurrentGame;