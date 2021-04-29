import ChampionPortrait from '../usables/ChampionPortrait.js';

const OpponentsChoice = ({opponents, setIsChoosing, setChampionChoice}) => {
    return ( 
        <div className="opponents-choice">
            {Object.keys(opponents).map((player_name) => (
                <div 
                className="opponent-choice"
                key={opponents[player_name]}
                onClick={(event) => {
                    setIsChoosing(false)
                    setChampionChoice(opponents[player_name])    
                }}
                >
                    <ChampionPortrait championName={opponents[player_name]}/>
                    <h3>{opponents[player_name]}</h3>
                </div>
            ))}
        </div>
     );
}
 
export default OpponentsChoice;