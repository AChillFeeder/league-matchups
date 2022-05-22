import {HTTPpost} from "../usables/EasyHTTP";
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";

const LiveGameInterface = ({data, opponentChampion, setOpponent}) => {

    const saveGame = () => {
        HTTPpost(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`, {
            //playerChampion:int [ID], laneOpponent:int [ID], win:int [0/1], gameCreation and gameID
            "playerChampion": data.summoner_champion.id,
            "laneOpponent": opponentChampion.id,
            "win": 1,
            "gameCreation": data.game_creation,
            "gameID": data.gameID,
            "notes": []
        })
        .then( () => console.log("success") ) // redirect to Home
    }

    return ( 
        <div>
            <h4>Game Information:</h4>
            <ul>
                <li>Game creation: {data.game_creation}</li>
                <li>Game ID: {data.gameID}</li>
            </ul>
            <h4>Summoner Champion</h4>
            <ul>
                <li>Name: {data.summoner_champion.name}</li>
                <img src={data.summoner_champion.full_image} alt={data.summoner_champion.name} />
                <li>Champion ID: {data.summoner_champion.id}</li>
            </ul>
            <br />
            <h4>Opponent Champion</h4>
            <ul>
                <li>Name: {opponentChampion.name}</li>
                <img src={opponentChampion.full_image} alt={opponentChampion.name} />
                <li>Champion ID: {opponentChampion.id}</li>
            </ul>
            <button onClick={() => setOpponent(false)}>Return back</button>
            <button onClick={saveGame}>Save game</button>
        </div>
     );
}
 
export default LiveGameInterface;