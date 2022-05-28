import React from 'react';
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import {HTTPget} from "../usables/EasyHTTP";

const Game = ({game, notes}) => {

    const [isLoading, setIsLoading] = React.useState(true)
    const [advancedData, setAdvancedData] = React.useState({})
    const [summonerAdvancedData, setSummonerAdvancedData] = React.useState({})
    const [opponentAdvancedData, setOpponentAdvancedData] = React.useState({})
    const [isVictorious, setIsVictorious] = React.useState(null)

    const [isVisible, setIsVisible] = React.useState(false);
    
    const advancedGameInformation = () => {
        setIsLoading(true);
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/gameInformation/${game.gameInformation.gameID}`)
        .then( data => {
                console.log(data);
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

    React.useEffect(
        () => {
            if(advancedData.info){
                advancedData.info.participants.map((participant) => {
                    if(participant.summonerName == game.playerChampion.summonerName){
                        console.log("Found summoner")
                        setSummonerAdvancedData(participant)
                    }
                    if(participant.summonerName == game.opponentChampion.summonerName){
                        // console.log("Found opponent")
                        setOpponentAdvancedData(participant)
                    }
                })
            }
        }, [advancedData]
    )

    const deleteNote = (noteID) => {
        HTTPget(`${ENVIRONMENT_VARIABLES.url}/deleteNote/${noteID}`)
        window.location.reload(false);
    }


    React.useEffect(
        () => {
            if(advancedData.info){
            let summonerTeam = advancedData.info.teams[0].teamId == summonerAdvancedData.teamID ? advancedData.info.teams[0] : advancedData.info.teams[1]
            let victory = summonerTeam.win
            console.log(victory)
            setIsVictorious(victory)
        }
    }, [advancedData])


    return ( 
        <div className='match-container' style={{border: "2px solid black"}} onClick={() => setIsVisible(!isVisible)}>

            <div key={game.gameInformation.id} className='match-data-container'>
                <ul id='generalInformation' style={ isVisible ? {} : { display: 'none' }}>
                    <h4><strong>General Information: </strong></h4>
                    <li>Game ID (database): {game.gameInformation.id}</li>
                    <li>userID: {game.gameInformation.userID}</li>
                    <li>Game Creation: {game.gameInformation.gameCreation}</li>
                    <li>Game ID (RiotAPI): {game.gameInformation.gameID}</li>
                    <br />
                    <li>Summoner Name: {game.playerChampion.summonerName}</li>
                    <li>Summoner ID: {game.playerChampion.summonerID}</li>
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

        <div className='toggle-game-information' style={ isVisible ? {} : { display: 'none' }}>
            <div className='match-notes-container'>
                <h4>Notes</h4>  
                {notes.map(note => {
                    return(
                        <ul key={note.id}  style={{border: "1px solid black"}}>
                            <li>game ID: {note.gameID}</li>
                            <li>Note ID: {note.id}</li>
                            <li>Note Content: {note.noteContent}</li>
                            <button onClick={()=>deleteNote(note.id)}>Delete Note</button>
                        </ul> 
                    ) 
                })}
            </div>

            {
                !isLoading ?
                <div className='match-advanced-information'>
                    
                <div>
                    
                    <h3>Victory: {isVictorious ? 'victory' : 'defeat'}</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Stat</th>
                                <th>Summoner</th>
                                <th>Opponent</th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Gold Earned: </td>
                            <td> {summonerAdvancedData.goldEarned} </td>
                            <td> {opponentAdvancedData.goldEarned} </td>
                        </tr>
                        <tr>
                            <td>Kills: </td>
                            <td> {summonerAdvancedData.kills} </td>
                            <td> {opponentAdvancedData.kills} </td>
                        </tr>
                        <tr>
                            <td>Deaths: </td>
                            <td> {summonerAdvancedData.deaths} </td>
                            <td> {opponentAdvancedData.deaths} </td>
                        </tr>
                        <tr>
                            <td>Vision score: </td>
                            <td> {summonerAdvancedData.visionScore} </td>
                            <td> {opponentAdvancedData.visionScore} </td>
                        </tr>
                        <tr>
                            <td>Turret takedowns: </td>
                            <td> {summonerAdvancedData.turretTakedowns} </td>
                            <td> {opponentAdvancedData.turretTakedowns} </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                    
                </div> :
                <p>No data yet</p>
            }
        </div>
        
        </div>    
    );
}
 
export default Game;
