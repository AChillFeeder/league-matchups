import Game from "./Game";
const ListOfGames = ({games, notes, searchTerm}) => {

    const getNotesByID = (id) => { // filter notes by the game's id so that every game gets its' notes
        let filtered_array = [];
        notes.map((note) => {
            if(note.gameID === id){
                filtered_array.push(note);
            }
        })
        return filtered_array
    }

    function filteredGames(term) { // filter games based on search term
        let filtered_games = [];
        games.map((game) => {
            if( // If the search term is in the player's champion name or the opponent's
                game.playerChampion.name.toLowerCase().includes(term) ||
                game.opponentChampion.name.toLowerCase().includes(term)
                ){
                filtered_games.push(game);
            }
        })
        return filtered_games
    }

    return ( 
        <div className='listOfGames'>
            {/* {typeof games} */}
            { filteredGames(searchTerm).map((game) => (
                <Game key={game.id} game={game} notes={getNotesByID(game.id)}/>
            ))}
        </div>
     );
}
 
export default ListOfGames;