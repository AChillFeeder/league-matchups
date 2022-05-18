const OpponentChoice = ({data, setOpponent}) => {
    return ( 
        <div>
            <ul>
                <li>Your champion: <strong>{data.summoner_champion.name}</strong></li>
                <li><img src={data.summoner_champion.image} alt={data.summoner_champion.name}/></li>
            </ul>
            {data.enemy_team_champions.map((champion) => {
                return (<ul key={champion.name} onClick={() => setOpponent(champion)}>
                    <li>Full name: {champion.name}</li>
                    <li><img src={champion.full_image} alt={champion.name} /></li>
                </ul>)
            })}
        </div>
     );
}
 
export default OpponentChoice;