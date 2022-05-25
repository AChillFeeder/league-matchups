import React from 'react';
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import {HTTPget} from "../usables/EasyHTTP";

const Game = ({game, notes}) => {

    const [isLoading, setIsLoading] = React.useState(true)
    const [advancedData, setAdvancedData] = React.useState({})
    
    const advancedGameInformation = () => {
        setIsLoading(true);
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gameInformation/${game.gameInformation.gameID}`)
        .then( data => {
                // console.log(data);
                setAdvancedData(data);
                setIsLoading(false);
            }
        )
    }

    React.useEffect(
        () => {
            advancedGameInformation()
        } 
    , [])

    return ( 
        <div className='match-container' style={{border: "2px solid black"}}>
            <div key={game.gameInformation.id} className='match-data-container'>
                <ul id='generalInformation'>
                    <h4><strong>General Information: </strong></h4>
                    <li>Victory: {game.gameInformation.victory}</li>
                    <li>Game ID (database): {game.gameInformation.id}</li>
                    <li>userID: {game.gameInformation.userID}</li>
                    <li>Game Creation: {game.gameInformation.gameCreation}</li>
                    <li>Game ID (RiotAPI): {game.gameInformation.gameID}</li>
                    <br />
                    <li>Opponent Summoner Name: {game.opponentChampion.summonerName}</li>
                    <li>Opponent Summoner ID: {game.opponentChampion.summonerID}</li>
                </ul>

                <ul id='playerChampion'>
                    <h4><strong>Player Champion: </strong></h4>
                    <li>Champion Name: {game.playerChampion.name}</li>
                    <img src={game.playerChampion.image} alt={`${game.playerChampion.name}`} />
                    <li>Champion Id: {game.playerChampion.id}</li>

                    {/* <img src={game.playerChampion.full_image} alt={`${game.playerChampion.name} full`} /> */}
                </ul>

                <ul id='opponentChampion'>
                    <h4><strong>Opponent Champion: </strong></h4>
                    <li>Champion Name: {game.opponentChampion.name}</li>
                    <img src={game.opponentChampion.image} alt={`${game.opponentChampion.name}`} />
                    <li>Champion ID: {game.opponentChampion.id}</li>

                    {/* <img src={game.opponentChampion.full_image} alt={`${game.playerChampion.name} full`} /> */}
                </ul>
            </div>

        <div className='toggle-game-information'>
            <div className='match-notes-container'>
                <h4>Notes</h4>  
                {notes.map(note => {
                    return(
                        <ul key={note.id}  style={{border: "1px solid black"}}>
                            <li>game ID: {note.gameID}</li>
                            <li>Note ID: {note.id}</li>
                            <li>Note Content: {note.noteContent}</li>
                        </ul> 
                    ) 
                })}
            </div>

            {
                !isLoading ?
                <div className='match-advanced-information'>
                    {advancedData.info.participants.map((participant)=>{
                        // console.log(`${participant.summonerName} <-> ${game.opponentChampion.summonerName}`)
                        if(participant.summonerName == game.opponentChampion.summonerName){
                            {console.log(participant)}
                            return (<div>
                                <h4>Opponent Advanced Data:</h4>
                                <ul>
                                    <li>Gold Earned: {participant.goldEarned}</li>
                                </ul>
                            </div>)
                        }
                    })}
                </div> :
                <p>No data yet</p>
            }
        </div>
        
        </div>    
    );
}
 
export default Game;
