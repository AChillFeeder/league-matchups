const OpponentChoice = ({data, setOpponent}) => {
    return ( 
        <div>
            <ul>
                <li>Your champion: <strong>{data.summoner.champion.name}</strong></li>
                <li><img src={data.summoner.champion.image} alt={data.summoner.champion.name}/></li>
            </ul>
            {data.enemy_summoners.map((summoner) => {
                return (<ul key={summoner.champion.name} onClick={() => setOpponent(summoner)}>
                    <li>Full name: {summoner.champion.name}</li>
                    <li><img src={summoner.champion.full_image} alt={summoner.champion.name} /></li>
                </ul>)
            })}
        </div>
     );
}
 
export default OpponentChoice;