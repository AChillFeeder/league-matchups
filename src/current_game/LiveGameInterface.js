import {HTTPget, HTTPpost} from "../usables/EasyHTTP";
import ENVIRONMENT_VARIABLES from "../usables/ENVIRONMENT_VARIABLES.json";
import NotesForm from "./NotesForm";
import React from 'react';

const LiveGameInterface = ({data, opponentSummoner, setOpponent}) => {

    const [notes, setNotes] = React.useState([]);
    const [pastNotes, setPastNotes] = React.useState([]);

    const saveGame = () => {
        HTTPpost(`${ENVIRONMENT_VARIABLES.url}/gamesHistory`, {
            //playerChampion:int [ID], laneOpponent:int [ID], win:int [0/1], gameCreation and gameID
            "playerChampion": data.summoner.champion.id,
            "laneOpponentChampion": opponentSummoner.champion.id,
            "laneOpponentSummonerID": opponentSummoner.summonerID,
            "laneOpponentSummonerName": opponentSummoner.summonerName,
            "win": 1,
            "gameCreation": data.game_creation,
            "gameID": data.gameID,
            "summonerName":data.summoner.summonerName,
            "summonerID":data.summoner.summonerID,
            "notes": notes
        })
        .then( () => console.log("success") ) // redirect to Home
    }

    React.useEffect(
        () => {
            HTTPget(`${ENVIRONMENT_VARIABLES.url}/getNotesByMatchup/${data.summoner.champion.id}/${opponentSummoner.champion.id}`)
                .then( data => {
                    setPastNotes(data.message);
                })
            }, []
    )

    React.useEffect(
        () => console.log(data), []
    )

    return ( 
        <div>
            <h4>Game Information:</h4>
            <ul>
                <li>Game creation: {data.game_creation}</li>
                <li>Game ID: {data.gameID}</li>
            </ul>
            <table>
                <tr>
                    <th></th>
                    <th>Summoner Information</th>
                    <th>Opponent Information</th>
                </tr>
                <tr>
                    <td colSpan={3}>General Information</td>
                </tr>
                <tr>
                    <td>Summoner Name: </td>
                    <td>{data.summoner.summonerName}</td>
                    <td>{opponentSummoner.summonerName}</td>
                </tr>
                <tr>
                    <td>Summoner ID: </td>
                    <td>{data.summoner.summonerID}</td>
                    <td>{opponentSummoner.summonerID}</td>
                </tr>
                <tr>
                    <td>Spell 1 ID: </td>
                    <td>{data.summoner.spell1Id}</td>
                    <td>{opponentSummoner.spell1Id}</td>
                </tr>
                <tr>
                    <td>Spell 2 ID: </td>
                    <td>{data.summoner.spell2Id}</td>
                    <td>{opponentSummoner.spell2Id}</td>
                </tr>
                <tr>
                    <td colSpan={3}>Champion</td>
                </tr>
                <tr>
                    <td>Name: </td>
                    <td>{data.summoner.champion.name}</td>
                    <td>{opponentSummoner.champion.name}</td>
                </tr>
                <tr>
                    <td>Image: </td>
                    <td><img src={data.summoner.champion.full_image} alt={data.summoner.champion.name} /></td>
                    <td><img src={opponentSummoner.champion.full_image} alt={opponentSummoner.champion.name} /></td>
                </tr>
                <tr>
                    <td>Name: </td>
                    <td>{data.summoner.champion.name}</td>
                    <td>{opponentSummoner.champion.name}</td>
                </tr>
                <tr>
                    <td>Champion ID: </td>
                    <td>{data.summoner.champion.id}</td>
                    <td>{opponentSummoner.champion.id}</td>
                </tr>
                <tr>
                    <td colSpan={3}>Runes</td>
                </tr>
                <tr>
                    <td>Runes</td>
                    <td>{data.summoner.perks.perkStyle} - {data.summoner.perks.perkSubStyle}</td>
                    <td>{opponentSummoner.perks.perkStyle} - {opponentSummoner.perks.perkSubStyle}</td>
                </tr>
            </table>
            
            <br />

            <h5>General Tips (death recap)</h5>
            {opponentSummoner.champion.enemy_tips.map((tip) => {
                return (
                    <li>{tip}</li>
                )
            })}
            <h5>Tips (From LeagueMatchups)</h5>
            {pastNotes.map((note) => {
                return (
                    <ul>
                        <li><strong>Content:</strong>{note.noteContent}</li>
                        <li><strong>Popularity:</strong>{note.popularity}</li>
                    </ul>
                )
            })}

            <h5>Abilities</h5>
            <table id="spells">
                    <tr>
                        <th>Image</th>
                        <th>Cooldowns</th>
                        <th>Costs</th>
                        <th>Description</th>
                    </tr>
                {opponentSummoner.champion.spells.map((spell) => {
                    return (
                        <tr>
                            <td><img src={spell.image_info}/></td>
                            <td>{spell.cooldowns[0]}/{spell.cooldowns[1]}/{spell.cooldowns[2]}/{spell.cooldowns[3]}/{spell.cooldowns[4]}</td>
                            <td>{spell.costs[0]}/{spell.costs[1]}/{spell.costs[2]}/{spell.costs[3]}/{spell.costs[4]}</td>
                            <td>{spell.description}</td>
                        </tr>
                    )
                })}
            </table>
            <NotesForm setNotes={setNotes}/>
            <button onClick={() => setOpponent(false)}>Return back</button>
            <button onClick={saveGame}>Save game</button>
        </div>
     );
}
 
export default LiveGameInterface;