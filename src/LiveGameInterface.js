const LiveGameInterface = ({playerChampion, opponentChampion, setOpponent}) => {
    return ( 
        <div>
            <h4>Summoner Champion</h4>
            <ul>
                <li>Name: {playerChampion.name}</li>
                <img src={playerChampion.full_image} alt={playerChampion.name} />
            </ul>
            <br />
            <h4>Opponent Champion</h4>
            <ul>
                <li>Name: {opponentChampion.name}</li>
                <img src={opponentChampion.full_image} alt={opponentChampion.name} />
            </ul>
            <button onClick={() => setOpponent(false)}>Return back</button>
        </div>
     );
}
 
export default LiveGameInterface;