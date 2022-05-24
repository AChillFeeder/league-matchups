import {HTTPpost} from "../usables/EasyHTTP";
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";

const LiveGameInterface = ({data, opponentSummoner, setOpponent}) => {

    const saveGame = () => {
        HTTPpost(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`, {
            //playerChampion:int [ID], laneOpponent:int [ID], win:int [0/1], gameCreation and gameID
            "playerChampion": data.summoner_champion.id,
            "laneOpponent": opponentSummoner.id,
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
            <h4>Summoner:</h4>
            <ul>
                <h5>General Information</h5>
                <li>Summoner Name: {data.summoner.summonerName}</li>
                <li>Summoner ID: {data.summoner.summonerID}</li>
                <li>Spell1Id: {data.summoner.spell1Id}</li>
                <li>Spell2Id: {data.summoner.spell2Id}</li>

                <h5>Champion:</h5>
                <li>Name: {data.summoner.champion.name}</li>
                <img src={data.summoner.champion.full_image} alt={data.summoner.champion.name} />
                <li>Champion ID: {data.summoner.champion.id}</li>

                <h5>Perks</h5>
                <li>Primary runes path id: {data.summoner.perks.perkStyle}</li>
                <li>Secondary runes path id: {data.summoner.perks.perkSubStyle}</li>
            </ul>
            <br />
            <h4>Opponent Summoner:</h4>
            <ul>
                <h5>General Information</h5>
                <li>Summoner Name: {opponentSummoner.summonerName}</li>
                <li>Summoner ID: {opponentSummoner.summonerID}</li>
                <li>Spell1Id: {opponentSummoner.spell1Id}</li>
                <li>Spell2Id: {opponentSummoner.spell2Id}</li>

                <h5>Perks</h5>
                <li>Primary runes path id: {opponentSummoner.perks.perkStyle}</li>
                <li>Secondary runes path id: {opponentSummoner.perks.perkSubStyle}</li>

                <h5>Champion:</h5>
                <li>Name: {opponentSummoner.champion.name}</li>
                <img src={opponentSummoner.champion.full_image} alt={opponentSummoner.champion.name} />
                <li>Champion ID: {opponentSummoner.champion.id}</li>
                {opponentSummoner.champion.enemy_tips.map((tip) => {
                    return (
                        <li>{tip}</li>
                    )
                })}
                {opponentSummoner.champion.spells.map((spell) => {
                    return (
                        <ul>
                            <li><img src={spell.image_info}/></li>
                            <li>Cooldowns: {spell.cooldowns[0]}/{spell.cooldowns[1]}/{spell.cooldowns[2]}/{spell.cooldowns[3]}/{spell.cooldowns[4]}</li>
                            <li>Costs: {spell.costs[0]}/{spell.costs[1]}/{spell.costs[2]}/{spell.costs[3]}/{spell.costs[4]}</li>
                            <li>Description: {spell.description}</li>
                        </ul>
                    )
                })}
            </ul>
            <button onClick={() => setOpponent(false)}>Return back</button>
            <button onClick={saveGame}>Save game</button>
        </div>
     );
}
 
export default LiveGameInterface;